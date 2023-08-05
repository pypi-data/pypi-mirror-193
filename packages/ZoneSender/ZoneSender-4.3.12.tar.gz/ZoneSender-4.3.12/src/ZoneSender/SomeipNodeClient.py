from typing import Union
import json
import typing
import os

import grpc

from . import ZoneSenderData
from .ObjIo import *

from .Protos import SomeIpNode_pb2, SomeIpNode_pb2_grpc


class SomeipNodeClient(object):
    def __init__(self) -> None:
        """ SomeipNode 的客户端
        """
        self._someipNodeStub = SomeIpNode_pb2_grpc.SomeIpNodeStub(
            channel=grpc.insecure_channel(
                target='{0}:{1}'
                    .format(
                        ZoneSenderData.SOMEIP_STACK_NODE_IP, 
                        ZoneSenderData.SOMEIP_STACK_NODE_PORT),
                options = ZoneSenderData.GRPC_OPTIONS
            )
        )

    def StartLogging(self,folder_path:str,file_name:str) -> 'int':
        ''' 启动 记录以太网数据
        :param folder_path: str 文件夹
        :param file_name: str 文件名字
        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._someipNodeStub.StartLog(
                SomeIpNode_pb2.Common__pb2.folder_file_path(
                    folder = folder_path,
                    file = file_name,
                )
            )
            if res_.result == 0 :
                return 0
            else :
                raise Exception(res_.reason)
        except Exception as e_ :
            print(e_)
            return 1000
    
    def StopLogging(self,folder_path:str,file_name:str) -> 'int':
        ''' 停止 记录以太网数据
        :param folder_path: str 文件夹
        :param file_name: str 文件名字
        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._someipNodeStub.StopLog(
                SomeIpNode_pb2.Common__pb2.folder_file_path(
                    folder = folder_path,
                    file = file_name,
                )
            )
            if res_.result == 0 :
                return 0
            else :
                raise Exception(res_.reason)
        except Exception as e_ :
            print(e_)
            return 1000
    
    def GetLoggingStatus(self, info: dict) -> 'int':
        ''' 获取记录数据状态
        :return: tuple\n
            - tuple: 成功 tuple[0] 1为有任务，0是没有任务；tuple[1] 为当前记录文件名\n
            - 1000: error\n
        '''
        try:
            res_ = self._someipNodeStub.GetLogStatus(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            # return (res_.result,res_.reason)
            info.update({
                'file_path': res_.reason
            })
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000

    def StartSomeIpStack(self, ip_addr: 'str', iface: 'str') -> 'int':
        ''' 启动 SomeIp 协议栈
        :param ip_addr: str 本机IP地址
        :param file_name: str 本机网卡名字

        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._someipNodeStub.StartSomeIpStack(
                SomeIpNode_pb2.Common__pb2.net_info(
                    ip_addr = ip_addr,
                    iface = iface
                )
            )
            print('启动Someip协议栈, result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_:
            print(e_)
            return 1000
    
    def StartSomeIpBypass(self) :
        try:
            ''' 启动 SomeIpBypass 协议栈

            :return: int\n
                - 0: 成功\n
                - 1000: error\n
            '''
            res_ = self._someipNodeStub.StartSomeIpStackBypass(SomeIpNode_pb2.Common__pb2.empty())
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000
    
    def StopSomeIpByPass(self) :
        try:
            '''关闭 SomeIpBypass 协议栈

            :return: int\n
                - 0: 成功\n
                - 1000: error\n
            '''
            res_ = self._someipNodeStub.StopSomeIpStackBypass(SomeIpNode_pb2.Common__pb2.empty())
            return res_.result
        except Exception as e_ :
            print(e_)
            return 1000

    def StopSomeIpStack(self) -> 'int':
        '''关闭 SomeIp 协议栈

        :return: int

            - 0: 成功

            - 1000: error
        '''
        try:
            res_ = self._someipNodeStub.StopSomeIpStack(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            print('关闭SomeIp协议栈, result: {0}, reason:{1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_:
            print(e_)
            return 1000

    def AddSomeIpArxml(self, arxml_path: 'str') -> 'int':
        ''' 添加一个 SomeIp Arxml 文件, 可以重复调用添加多个

        :return: int

            - 0: 成功

            - 1000: error
        '''
        try:
            res_ = self._someipNodeStub.AddSomeIpArxml(
                SomeIpNode_pb2.Common__pb2.file_path(
                    path = arxml_path
                )
            )
            print('加载 SomeIp Arxml 文件 result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_:
            print(e_)
            return 1000
    
    def AddIfaceInfo(self,ip:str,ifacename:str) -> 'int':
        ''' 添加一个网卡信息, 可以重复添加，但是只会记录最后一个，当前只支持单网卡模式
        :param ip: str 网卡的IPv4地址
        :param ip: str 网卡的名字
        :return: int

            - 0: 成功

            - 1000: error
        '''
        try:
            res_ = self._someipNodeStub.AddIfaceInfo(
                SomeIpNode_pb2.Common__pb2.net_info(
                    ip_addr = ip,
                    iface = ifacename
                )
            )
            if res_.result == 0 :
                return 0
            else :
                raise Exception(res_.reason)
        except Exception as e_ :
            print(e_)
            return 1000
    
    def GetIfaceInfo(self) -> Union['tuple','int'] :
        ''' 获取网卡的信息

        :return: int | tuple

            - tuple: 成功,元组为（ip,name）

            - 1000: error
        '''
        try:
            res_ = self._someipNodeStub.GetIfaceInfo(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            if res_.ip_addr and res_.iface :
                return (res_.ip_addr,res_.iface)
            else :
                raise Exception('获取网卡信息失败')
        except Exception as e_ :
            print(e_)
            return 1000
 
    def GetArxmlJsonData(self) -> Union[dict,int] :
        ''' 获取所有 SomeIp Arxml 文件中的信息

        :return: int | dict

            - dict: 成功,字典里为arxml信息

            - 1000: error
        '''
        try:
            res_ = self._someipNodeStub.GetArxmlToJson(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            if res_.result == 0 :
                return json.loads(res_.json_data)
            else :
                raise Exception(f'{res_.reason}')
        except Exception as e_ :
            print(e_)
            return 1000

    def GetSomeIpServiceInfos(self, return_d: 'dict') -> 'int':
        ''' 获取当前已经加载的 SomeIp Arxml Info

        :param return_d: 如果获取成功，将会把获取的信息填充到该字典中
        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._someipNodeStub.GetSomeIpServiceInfos(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            if (not res_.result.result == 0):
                return res_.result.result
            return_d.clear()
            return_d.update(json.loads(res_.json_str_info))
            return res_.result.result
        except Exception as e_:
            print(e_)
            return 1000

    def UpdateSomeIpServiceConfig(
        self, 
        service_name: 'str', 
        instance_id: 'int', 
        service_type: 'str',
        service_state : 'bool' = True) -> 'int':
        ''' 更新SomeIp中服务的信息

        :param service_id: str SomeIp Service ID
        :param instance_id: int SomeIp Service Instance ID
        :param service_type: str 可以是 'consumer'|'provider' 表示该服务设置为什么类型
        :param state : int 默认值是True，用户可以不用填，如果需要停止服务，该参数赋值False

        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._someipNodeStub.UpdateSomeipServiceConfig(
                SomeIpNode_pb2.service_tag(
                    service_name = service_name,
                    instance_id = instance_id,
                    service_type = service_type,
                    service_state = service_state,
                )
            )
            print('更新 SomeIp 服务设定 result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_:
            print(e_)
            return 1000

    def Reset(self) -> 'int':
        ''' 复位 SomeIp 协议栈，并清空 SomeIp 服务配置

        :return: int\n
            - 0: 成功\n
            - 1000: error\n
        '''
        try:
            res_ = self._someipNodeStub.Reset(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            print('复位 SomeIp 协议栈 result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_:
            print(e_)
            return 1000

    def GetSomeIpStackStatus(self) -> 'int':
        '''获取当前 Someip Stack 的状态

        :return: int\n
            - 0 正在运行\n
            - 1 协议栈未启动\n
            - 2 协议栈未初始化\n
            - 1000 error
        '''
        try:
            res_ = self._someipNodeStub.GetSomeipStackStatus(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            print('SomeipStack 的状态为 {0}'.format(res_.result))
            return res_.result
        except Exception as e_:
            print(e_)
            return 1000

    def SomeipCallSync(
        self, 
        someip_package_in: 'SomeipPackage', 
        someip_package_out: 'SomeipPackage', 
        timeout: 'int' = 1000,
        *args, **kwargs) -> 'int':
        ''' 同步调用 SomeipCall
        :param someip_package_in: 要调用的 SomeipPackage
        :param someip_package_out: 如果成功调用，则将返回的 SomeipPackage 填充到该对象中
        :param timeout: 超时参数，单位 ms
        :param by: str 设置使用什么来发送 Someip 'context'|'payload'
        :return: int\n
            - 0 正在运行\n
            - 1 超时\n
            - 1000 error
        '''
        try:
            d_ = someip_package_in.ToDict()
            d_.update({'by': kwargs.get('by', 'context')})
            d_.update({'payload': d_['payload'].hex()})
            res_ = self._someipNodeStub.SomeipCallSync(
                SomeIpNode_pb2.someip_call_context(
                    timeout = timeout,
                    str_context = json.dumps(d_)
                )
            )
            result_ = res_.result.result
            if (result_ == 0):
                # 成功回复
                recv_d_ = json.loads(res_.str_context)
                recv_d_.update({'payload': bytes.fromhex(recv_d_['payload'])})
                # print(recv_d_)
                # someip_package_out = SomeipPackage.From(recv_d_)
                SomeipPackage.CopyData(SomeipPackage.From(recv_d_), someip_package_out)
                return 0
            else:
                print(res_.result.reason)
                return result_
        except Exception as e_:
            print(e_)
            return 1000

    def GetAllOfferService(self, offer_services_out:list) -> int:
        '''
        获取当前 SomeipStack 所有的 Offer 的服务\n
        注意, 如果获取成功, offer_service 会清空\n
        :param offer_service:list 获取到的服务信息将传到该 list 中\n
        :return:int
            - 0:获取成功
            - 1:协议栈未启动
            - 1000:error
        '''
        try:
            res_ = self._someipNodeStub.GetAllOfferService(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            if (res_.result.result != 0):
                print(res_.result.reason)
                return res_.result.result
            offer_services_out.clear()
            for info_ in res_.infos:
                offer_services_out.append(SomeipPackage(
                    service_name=info_.service_name,
                    instance_id=info_.instance_id,
                    service_id=info_.service_id,
                    src_ip=info_.src_ip,
                ))
            print('GetAllOfferService result {0}'.format(res_.result.result))
            return res_.result.result
        except Exception as e_:
            print('GetAllOfferService Except {0}'.format(e_))
            return 1000

    def ConvertSomeipDbToPy(self, src_file:str, dst_file:str) -> int:
        '''
        将指定的 SomeipDB 文件转换成 .py 的代码提示辅助文件
        :param src_file:str 输入的文件, 支持两种类型: CANxxx.arxml 和 CANxxx.json, 支持输入相对路径和绝对路径
        :param dst_file:str 输出的文件, 将转换的文件写到哪里。注意 python 的 import 不支持 . 和 -
        :return:int 返回结果 0 成功 其他失败
        '''
        try:
            if (not os.path.isabs(src_file)):
                src_file = os.path.abspath(src_file)
            if (not os.path.isabs(dst_file)):
                dst_file = os.path.abspath(dst_file)
            res_ = self._someipNodeStub.ConvertSomeipDbToPy(
                SomeIpNode_pb2.convert_input(
                    src_file = src_file,
                    dst_file = dst_file,
                )
            )
            print('ConvertSomeipDbToPy result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_:
            print('ConvertSomeipDbToPy Exception: ', e_)
            return 1000

    def ConvertSomeipDbToJson(self, src_file:str, dst_file:str) -> int:
        '''
        将指定的 SomeipDB 文件转换成 .json 的方便看里面内容的文件
        :param src_file:str 输入的文件, 支持类型: CANxxx.arxml
        :param dst_file:str 输出的文件, 将转换的文件写到哪里, 建议使用 .json 后缀
        :return:int 返回结果 0 成功 其他失败
        '''
        try:
            if (not os.path.isabs(src_file)):
                src_file = os.path.abspath(src_file)
            if (not os.path.isabs(dst_file)):
                dst_file = os.path.abspath(dst_file)
            res_ = self._someipNodeStub.ConvertSomeipDbToJson(
                SomeIpNode_pb2.convert_input(
                    src_file = src_file,
                    dst_file = dst_file,
                )
            )
            print('ConvertSomeipDbToJson result: {0}, reason: {1}'.format(res_.result, res_.reason))
            return res_.result
        except Exception as e_:
            print('ConvertSomeipDbToJsonClient Exception: ', e_)
            return 1000
    
    def GetServiceStates(self, service_states: typing.List[SomeipServiceState]) -> int:
        '''
        获取当前正在运行的 SomeipService 状态
        :param service_states:list[SomeipServiceState] 空 list, 如果本函数调用成功，就会填充这个 list
        :return:int 调用结果
        
        详细的 SomeipServiceState 请看该数据结构的源码注释
        关于服务状态的判定逻辑：
            - 如果该服务作为 Providr, 一般服务启动后，只要网络没有问题，都是 True
            - 如果该服务作为 Consumer, 判定逻辑如下
                - 如果该服务有 EventGroupID，那么收到 Provider 的 SubscriberACK 的时候，
                就判定为 True, 否则为 False
                - 如果该服务没有 EventGroupID，如果发现了该服务的 Offer 且 TCP 建连成功就
                判定为 True ，否则为 False，如果该服务是 UDP，那么只需要判定该有没有该服务的
                Offer, 如果有 Offer，就判定成功。
        '''
        try:
            res_ = self._someipNodeStub.GetServiceStates(
                SomeIpNode_pb2.Common__pb2.empty()
            )
            if (not res_.result.result == 0):
                # 如果返回结果失败
                return res_.result.result
            for service_state_ in res_.service_states:
                service_states.append(SomeipServiceState(
                    service_name=service_state_.service_name,
                    service_id=service_state_.service_id,
                    instance_id=service_state_.instance_id,
                    service_state=service_state_.service_state,
                    service_side=service_state_.service_side,
                ))
            print('[SomeipNodeClient.GetServiceStates] 成功，result: {0}, reason: {1}'.format(res_.result.result, res_.result.reason))
            return res_.result.result
        except Exception as e_:
            print('[SomeipNodeClient.GetServiceStates] 失败，reason: {0}'.format(e_))
            return 1000