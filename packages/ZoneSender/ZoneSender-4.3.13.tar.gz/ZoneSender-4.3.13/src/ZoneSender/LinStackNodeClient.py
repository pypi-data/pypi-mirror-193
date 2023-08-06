from typing import Union
from typing import List
import grpc
from . import ZoneSenderData
from .ObjIo import *

from .Protos import LinStackNode_pb2,LinStackNode_pb2_grpc


class LinStackNodeClient(object) :
    """
    LinStackNode 的客户端
    """
    def __init__(self) -> None:
        self._linStackStub = LinStackNode_pb2_grpc.LinStackNodeStub(
            channel=grpc.insecure_channel(
                target='{0}:{1}'
                    .format(
                        ZoneSenderData.LIN_STACK_NODE_IP, 
                        ZoneSenderData.LIN_STACK_NODE_PORT),
                options = ZoneSenderData.GRPC_OPTIONS
            )
        )

    def setConfig(self,configs:List[dict]) -> int:

        ''' LIN Stack设置硬件类型,目前只支持vector
        
        :param configs: List[dict] 
            configs example:\n
            [{'hardwareType':'vector','appName':'zoneSender'},{'hardwareType':'pcan','appName':'zoneSender'}]\n

        :return: int\n
            - 0: 成功\n
            - 1: 配置失败\n
            - 1000: error\n
        '''

        try:
            configs_ = list()
            for config_ in configs :
                configs_.append(
                    LinStackNode_pb2.lin_stack_config(
                        hardwareType = config_['hardwareType'],
                        appName = config_['appName'],
                    )
                )
            res_ = self._linStackStub.SetConfig(
                LinStackNode_pb2.lin_stack_configs(
                    config = configs_,
                )
            )
            print('setConfig result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000
    
    def startLinStack(self) -> int:
        ''' 启动LIN Stack
        :return: int\n
            - 0: 成功\n
            - 1: 未设置LIN Stack,需要先setConfig\n
            - 2: LIN Stack已经在运行\n
            - 3: LIN Stack启动失败
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.StartLinStack(
                LinStackNode_pb2.Common__pb2.empty()
            )
            print('StartLinStack result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000
    
    def stopLinStack(self) -> int:
        '''停止LIN Stack
        :return: int\n
            - 0: 成功\n
            - 1: 未设置LIN Stack,需要先setConfig\n
            - 2: LIN Stack不在运行\n
            - 3: LIN Stack停止失败
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.StopLinStack(
                LinStackNode_pb2.Common__pb2.empty()
            )
            print('StopLinStack result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000

    def reset(self) -> int:
        '''重置LIN Stack，会清除LIN Stack所有信息，需要重新设置然后启动才能正常使用
        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.Reset(
                LinStackNode_pb2.Common__pb2.empty()
            )
            print('ResetLinStack result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000

    def setMessageSimulation(self,channel:int,id:int,simu:bool) -> int:
        '''设置LIN报文响应仿真
        :param channel: int 设置的LIN通道
        :param id: int 指定报文的ID
        :param simu: bool True为使能仿真，False为关闭仿真
        :return: int\n
            - 0: 成功\n
            - 1: 未设置LIN Stack,需要先setConfig\n
            - 2: LIN Stack未运行\n
            - 3: LIN 驱动层错误
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.SetMessageSimulation(
                LinStackNode_pb2.lin_message_config(
                    id = id,
                    simu = simu,
                    channel = channel,
                )
            )
            print('setMessageSimulation result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000
    
    def setHeaderSimulation(self,channel:int,simu:bool) -> int:
        '''设置主节点报文头仿真
        :param channel: int 设置的LIN通道
        :param simu: bool True为使能仿真，False为关闭仿真
        :return: int\n
            - 0: 成功\n
            - 1: 未设置LIN Stack,需要先setConfig\n
            - 2: LIN Stack未运行\n
            - 3: 当前通道不是主节点模式，不支持主节点报文头仿真
            - 4: LIN 驱动层错误
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.SetHeaderSimulation(
                LinStackNode_pb2.lin_header_config(
                    simu = simu,
                    channel = channel,
                )
            )
            print('setHeaderSimulation result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000

    def clearSend(self,channel:int = -1) ->int :
        '''清除LIN Stack中所有仿真
        :param channel: int 设置LIN通道，-1是全部通道，非-1就是特定通道
        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.ClearSend(
                LinStackNode_pb2.Common__pb2.generic_int(
                    index = channel
                )
            )
            print('ClearSend result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000
    
    def clearCrcConfig(self,channel:int = -1,id:int = 0) ->int :
        '''清除所有CRC配置
        :param channel: -1是全部通道所有crc清除，非-1就是特定通道
        :param id: int LIN报文的ID
        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.ClearLinCrcConfig(
                LinStackNode_pb2.lin_crc_config(
                    channel = channel,
                    id = id,
                )
            )
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000

    def setCrcConfig(self,channel:int,id:int,
                    crc_bit_start:int,crc_bit_len:int,
                    rc_bit_start:int,rc_bit_len:int,rc_min_value:int,rc_max_value:int,
                    crc_table:list) -> int :
        '''设置对应的报文CRC配置
        :param channel: int 设置LIN通道
        :param id: int LIN报文的ID
        :param crc_bit_start: int CRC所在bit的起始位
        :param crc_bit_len: int CRC所占的bit长度
        :param rc_bit_start: int RC所在bit起始位
        :param rc_bit_len: int RC所占的bit长度
        :param rc_min_value: int RC最小值
        :param rc_max_value: int RC最大值
        :param crc_table: int CRC算法使用的CRC表
        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.SetLinCrcConfig(
                LinStackNode_pb2.lin_crc_config(
                    channel = channel,
                    id = id,
                    crc_bit_start = crc_bit_start,
                    rc_bit_start = rc_bit_start,
                    crc_bit_len = crc_bit_len,
                    rc_bit_len = rc_bit_len,
                    rc_min_value = rc_min_value,
                    rc_max_value = rc_max_value,
                    crc_table = crc_table
                )
            )
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000


    def clearSubscribe(self) -> int:
        '''清除LIN Stack中所有的订阅
        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._linStackStub.ClearSubscribe(
                LinStackNode_pb2.Common__pb2.empty()
            )
            print('clearSubscribe result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000
    
    def isRunning(self) -> Union[int,bool]:
        '''获取LIN Stack当前的运行状态
        :return: int or bool\n
            - True: 运行\n
            - False: 不在运行\n
            - 1000 : error
        '''
        try:
            res_ = self._linStackStub.GetStatus(
                LinStackNode_pb2.Common__pb2.empty()
            )
            if res_.status == 0:
                return True
            else:
                return False
        except Exception as e_ :
            print(e_)
            return 1000