import ctypes
import logging
import typing
import os
import time
from multiprocessing import Lock, shared_memory

DELAY_TIME_INSERT = 100000000    # 插入数据会过滤 100 ms 以前的数据
DELAY_TIME_VISABLE = 300000000    # 显示会滞后 300 ms


class IndexNode(ctypes.Structure):
    _fields_ = [
        ('prev', ctypes.c_uint64),
        ('next', ctypes.c_uint64),
        ('current', ctypes.c_uint64),
        ('time_stamp_ns', ctypes.c_uint64),
        ('valid', ctypes.c_uint8),
        ]

    def __init__(self, prev:int, next:int, current:int, time_stamp_ns:int, valid:int) -> None:
        '''
        双向链表节点数据结构
        :param prev:int 前一个 Node 的索引
        :param next:int 后一个 Node 的索引
        :param current:int 当前 Node 的索引
        :param time_stamp:int 当前节点的时间戳
        :param valid:int 当前节点是否是有效的
            - 0: 无效
            - 1: 有效
        '''
        self.prev = prev
        self.next = next
        self.current = current
        self.time_stamp_ns = time_stamp_ns
        self.valid = valid

    def ToBytes(self) -> 'bytes':
        '''
        转换为 bytes
        :return:bytes 该Node的Bytes表达
        '''
        prev_ = self.prev.to_bytes(length=8, byteorder='big', signed=False)
        next_ = self.next.to_bytes(length=8, byteorder='big', signed=False)
        current_ = self.current.to_bytes(length=8, byteorder='big', signed=False)
        time_stamp_ = self.time_stamp_ns.to_bytes(length=8, byteorder='big', signed=False)
        valid_ = self.valid.to_bytes(length=1, byteorder='big', signed=False)
        return prev_ + next_ + current_ + time_stamp_ + valid_

class SharedMemZoneSender(object):
    DATA_SIZE = 20480
    INDEX_SIZE = 32
    MAX_LIST_SIZE = int(1024*128)
    # MAX_LIST_SIZE = int(32)
    
    INVAILD_INDEX = 0xFFFFFFFFFFFFFFFF
    def __init__(self, lock=None, name: str='ZoneSender', create: bool=False, size:int=MAX_LIST_SIZE) -> None:
        '''
        ZoneSender 的共享内存类, 可以实现高性能的数据跨进程 IO
        :param lock:multiprocessing.Lock 写进程的互斥锁
        :param name:str 共享内存块的名字
        :param create:bool 是否要创建新的内存块，默认行情况下只能由管理进程创建
        :param size:int 要创建的内存块长度 默认是 128 MB
        '''
        self._logger = logging.getLogger('ShareMemNode')
        self._logger.debug('test1')
        if (create):
            self.sharedDataListMem = shared_memory.ShareableList(sequence=[bytes([0xFF]* SharedMemZoneSender.DATA_SIZE)]*size, name=name+'Data')
            self.sharedIndexListMem = shared_memory.ShareableList(sequence=[bytes([0xFF]* SharedMemZoneSender.INDEX_SIZE)]*size, name=name+'Index')
            self.latestIndexMem = shared_memory.SharedMemory(name=name+'LatestIndex', create=True, size=8)
            self.firstIndexMem = shared_memory.SharedMemory(name=name+'FirstIndex', create=True, size=8)
            self.readyWriteIndexMem = shared_memory.SharedMemory(name=name+'ReadyWriteIndex', create=True, size=8)
            self.isNewMem = shared_memory.SharedMemory(name=name+'IsNew', create=True, size=1)
            self._SetFirstIndex(0)
            self._SetLatsetIndex(SharedMemZoneSender.INVAILD_INDEX)
            self._SetReadyWriteIndex(0)
            self._SetIsNew(1)
        else:
            self.sharedDataListMem = shared_memory.ShareableList(name=name+'Data')
            self.sharedIndexListMem = shared_memory.ShareableList(name=name+'Index')
            self.latestIndexMem = shared_memory.SharedMemory(name=name+'LatestIndex', create=False)
            self.firstIndexMem = shared_memory.SharedMemory(name=name+'FirstIndex', create=False)
            self.readyWriteIndexMem = shared_memory.SharedMemory(name=name+'ReadyWriteIndex', create=False)
            self.isNewMem = shared_memory.SharedMemory(name=name+'IsNew', create=False)
        self.lock = lock
        self.size = size
        self.readTime = time.time_ns()
        self.Sync()

    def Sync(self) -> None:
        '''
        同步到最新的数据
        '''
        self.nextReadIndex = self._GetLatestIndex()
        self.isReadToLatest = False
    
    def WriteNext(self, time_stamp_ns:int, data:'bytes') -> None:
        '''
        写下一帧数据
        :param time_stamp:int 下一帧的时间戳
        :param data:bytes 下一帧的数据 不能超过 1024 个 bytes
        '''
        self.lock.acquire(True)
        try:
            ready_write_index_ = self._GetReadyWriteIndex()
            # first_index_ = self._GetFirstIndex()
            latest_index_ = self._GetLatestIndex()

            index_node_ = IndexNode(ready_write_index_, ready_write_index_, ready_write_index_, time_stamp_ns, 1)
            self.WriteFrame(ready_write_index_, data)
            self.WriteIndex(index_node_)
            if (latest_index_ == SharedMemZoneSender.INVAILD_INDEX):
                # 如果最新的索引是无效的，代表是新的内存块
                # 则写入第 0 个 index
                self._SetLatsetIndex(1)
            else:
                # 如果不是新内存块，就
                self._SetLatsetIndex(ready_write_index_ + 1)

            ready_write_index_ += 1
            if (ready_write_index_ >= self.size):
                self._SetReadyWriteIndex(0)
            else:
                self._SetReadyWriteIndex(ready_write_index_)
        except Exception as e_:
            self._logger.error('WriteNext Exception {0} {1}'.format(type(e_), e_))
        finally:
            self.lock.release()

    def ReadNext(self) -> typing.Tuple[int, bytes]:
        '''
        读下一帧数据
        :return:tuple 返回的数据
            - [0]:int 下一帧的时间戳
            - [1]:bytes 下一帧的数据
        '''
        # time_now_ns_ = time.time_ns()
        index_node_ = self.GetIndexNode(self.nextReadIndex)
        
        if (index_node_.valid != 1):
            return (0, bytes())

        # if ((index_node_.time_stamp_ns + DELAY_TIME_VISABLE) > time_now_ns_):    # 2022年9月8日注释，尝试解决 ShareMem 读取慢的问题
        # if ((index_node_.time_stamp_ns) > time_now_ns_):
            # print('========')
            # return (0, bytes())

        if (index_node_.current == index_node_.next):
            # 如果本次要读的数据是最新的数据
            if (self.isReadToLatest):
                # 如果已经读到最新了
                return (0, bytes())
            else:
                self.isReadToLatest = True
                return (index_node_.time_stamp_ns, self.ReadFrame(index_node_.current))
        else:
            # 如果本次要读的数据不是最新的数据
            self.isReadToLatest = False
            self.nextReadIndex = index_node_.next
            return (index_node_.time_stamp_ns, self.ReadFrame(index_node_.current))

    def ReadToLatest(self) -> typing.List[typing.Tuple[int, bytes]]:
        '''
        读到最新时刻
        :return:List[bytes] 到最新时刻的数据
        '''
        l_ = []
        while (True):
            time_, data_ = self.ReadNext()
            if (len(data_) > 0):
                l_.append((time_, data_))
            else:
                break
        return l_

    def ReadToLatestIndex(self) -> typing.Tuple[bool, int, int]:
        '''
        读取当前 Index 到最新 Index 的索引, 并设置当前读到的索引为最新
        :return:
            - [0]:bool: 是否有有效的数据
            - [1]:int: strat_index
            - [2]:int: end_index
        '''
        latest_index_ = self._GetLatestIndex()
        next_read_index_ = self.nextReadIndex
        if (latest_index_ == SharedMemZoneSender.INVAILD_INDEX):
            # 如果是无效的最新索引
            return (False, 0, 0)
        else:
            if (next_read_index_ == SharedMemZoneSender.INVAILD_INDEX):
                next_read_index_ = 0
            # print('ReadToLatestIndex : latest_index_: {0} next_read_index_ {1}'.format(latest_index_, next_read_index_))
            # 如果是有效的最新索引
            if (next_read_index_ < latest_index_):
                self.nextReadIndex = latest_index_
                return (True, next_read_index_, latest_index_)
            elif (next_read_index_ > latest_index_):
                # 下一轮
                self.nextReadIndex = 0
                return (True, next_read_index_, self.size)
            else:
                return (False, 0, 0)

    def ReadFrame(self, index:int) -> 'bytes':
        '''
        读指定位置的数据
        :param index:int 指定的位置索引
        :return:bytes 指定位置的数据
        '''
        length_ = int.from_bytes(self.sharedDataListMem[index][0:8], byteorder='big', signed=False)
        # node_ = self.GetIndexNode(index)
        data_ = self.sharedDataListMem[index][8:8+length_]
        act_len_ = len(data_)
        if ((act_len_ == 0) and (length_ != 0)):
            # 如果实际数据是空，但是长度不为空，就返回指定长度的 0 bytes
            a_= bytes([0]*length_)
            # print(a_)
            return a_
        if (act_len_ != length_):
            # 如果得到的 bytes 数据长度和期望长度不同，就在尾部补充 /x00
            l_ = list(data_)
            l_.extend([0]*(length_ - act_len_))
            data_ = bytes(l_)
        return data_

    def WriteFrame(self, index:int, data:'bytes') -> None:
        '''
        写指定位置的数据
        :param index:int 要写入的位置
        :param data:bytes 要写入的数据
        '''
        self.sharedDataListMem[index] = len(data).to_bytes(8, byteorder='big', signed=False) + data

    def _SetLatsetIndex(self, index:int) -> None:
        '''
        设置最新位置的索引
        :param index:int 要设置的最新位置的索引
        '''
        self.latestIndexMem.buf[0:8] = index.to_bytes(length=8, byteorder='big', signed=False)
    
    def _GetLatestIndex(self) -> int:
        '''
        获取最新位置的索引
        :return:int 最新位置的索引
        '''
        return int.from_bytes(self.latestIndexMem.buf[0:8], byteorder='big', signed=False)

    def _SetFirstIndex(self, index:int) -> None:
        '''
        设置第一个位置的索引
        :param index:int 要设置的第一个位置的索引
        '''
        self.firstIndexMem.buf[0:8] = index.to_bytes(length=8, byteorder='big', signed=False)
    
    def _GetFirstIndex(self) -> int:
        '''
        获取第一个位置的索引
        :return:int 第一个位置的索引
        '''
        return int.from_bytes(self.firstIndexMem.buf[0:8], byteorder='big', signed=False)

    def _SetReadyWriteIndex(self, index:int) -> None:
        '''
        设置最新位置的索引
        :param index:int 要设置的最新位置的索引
        '''
        self.readyWriteIndexMem.buf[0:8] = index.to_bytes(length=8, byteorder='big', signed=False)
    
    def _GetReadyWriteIndex(self) -> int: 
        '''
        设置最新位置的索引
        :param index:int 要设置的最新位置的索引
        '''
        return int.from_bytes(self.readyWriteIndexMem.buf[0:8], byteorder='big', signed=False)

    def _SetIsNew(self, index:int) -> None:
        '''
        设置最新位置的索引
        :param index:int 要设置的最新位置的索引
        '''
        self.isNewMem.buf[0:1] = index.to_bytes(length=1, byteorder='big', signed=False)
    
    def _GetIsNew(self) -> int:
        '''
        获取是否最新内存
        :return: int
            - 0:不是新内存
            - 1:是新内存
        '''
        return int.from_bytes(self.isNewMem.buf[0:1], byteorder='big', signed=False)

    def WriteIndex(self, index_node: IndexNode) -> None:
        '''
        设置最新位置的索引
        :param index:int 要设置的最新位置的索引
        '''
        self.sharedIndexListMem[index_node.current] = index_node.ToBytes()

    def GetIndexNode(self, index:int) -> IndexNode:
        '''
        设置最新位置的索引
        :param index:int 要设置的最新位置的索引
        '''
        if (index > self.size):
            print('GetIndexNode(self, index:int) {0}'.format(index))
        try:
            data_ = self.sharedIndexListMem[index]
        except:
            return IndexNode(0, 0, 0, 0, 0)
        len_ = len(data_)
        if (len_ != 33):
            # 如果读到全 0
            l_ = list(data_)
            l_.extend([0]*(33 - len_))
            return self._NodeFromBytes(bytes(l_))
        return self._NodeFromBytes(data_)
    
    def _NodeFromBytes(self, data:bytes) -> IndexNode:
        '''
        设置最新位置的索引
        :param index:int 要设置的最新位置的索引
        '''
        return IndexNode(
            prev=int.from_bytes(data[0:8], byteorder='big', signed=False),
            next=int.from_bytes(data[8:16], byteorder='big', signed=False),
            current=int.from_bytes(data[16:24], byteorder='big', signed=False),
            time_stamp_ns=int.from_bytes(data[24:32], byteorder='big', signed=False),
            valid=int.from_bytes(data[32:33], byteorder='big', signed=False))
