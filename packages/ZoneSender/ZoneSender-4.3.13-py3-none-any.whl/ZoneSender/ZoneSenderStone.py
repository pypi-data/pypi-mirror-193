import json
import os
import platform
import time
import typing
import uuid
from concurrent.futures import ThreadPoolExecutor

import grpc
import paho.mqtt.client as mqtt

from . import ZoneSenderData
from .ObjIo import *
from .SharedMemory import SharedMemZoneSender
# from .ObjIo import 
from .ZoneSenderFramework import ZoneSenderFramework


class ZoneSenderStone(ZoneSenderFramework):
    def __init__(self) -> None:
        super().__init__()
        ########################################
        self._threadPool = ThreadPoolExecutor(2)
        self._mqttClient = mqtt.Client(
            client_id=uuid.uuid4().hex,
            transport='websockets')
        self._mqttClient.on_connect = self._OnMqttConnect
        self._mqttClient.on_message = self._OnMqttMessage
        self._mqttClient.on_disconnect = self._OnMqttDisconnect
        self._mqttClient.connect(ZoneSenderData.MQTT_BROKER_IP, ZoneSenderData.MQTT_BROKER_PORT)
        if platform.system() == 'Windows' :
            self.shareMem = SharedMemZoneSender()
        self._mqttClient.loop_start()
        
    def Subscribe(self, obj) -> None:
        ''' 订阅对象事件，只有订阅了相关对象，才能在后续的 OnXXX 回调函数中收到对应的对象接收事件

        :param obj: 需要订阅的对象，可以是如下类型\n
            - ZoneSender.ObjIo.CanMessage\n
            - ZoneSender.ObjIo.CanFrame\n
            - ZoneSender.ObjIo.CanSignal\n
            - ZoneSender.ObjIo.CanISignalIPdu\n
            - ZoneSender.ObjIo.SomeipPackage\n
            - ZoneSender.ObjIo.LinMessage\n
            - ZoneSender.ObjIo.LinFrame\n
            - ZoneSender.ObjIo.LinSignal\n
        '''
        obj_ = obj
        if (isinstance(obj_, CanMessage)):
            self._mqttClient.subscribe('zonesender/canstacknode/message/{0}/{1}'.format(obj_.channel, hex(obj_.arbitration_id).lower()))
            self._mqttClient.publish(
                topic='zonesender/canstacknode/subscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'arbitration_id': obj_.arbitration_id,
                }).encode('utf-8')
            )
        elif (isinstance(obj_, CanFrame)):
            self._mqttClient.subscribe('zonesender/canparsernode/frame/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/canparsernode/subscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'frame',
                }).encode('utf-8')
            )
        elif (isinstance(obj_, CanSignal)):
            self._mqttClient.subscribe('zonesender/canparsernode/signal/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/canparsernode/subscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'signal',
                }).encode('utf-8')
            )
        elif (isinstance(obj_, CanISignalIPdu)):
            self._mqttClient.subscribe('zonesender/canparsernode/pdu/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/canparsernode/subscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'pdu',
                }).encode('utf-8')
            )
        elif (isinstance(obj_, SomeipPackage)):
            if (obj_.serviceName == ''):
                print('不能订阅空的 someip service')
                return
            self._mqttClient.subscribe('zonesender/someipnode/someippackage/{0}'.format(obj_.serviceName))
            self._mqttClient.subscribe('zonesender/someipnode/someipcalling/{0}'.format(obj_.serviceName))
            self._mqttClient.subscribe('zonesender/someipnode/someipbypass/{0}'.format(obj_.serviceName))
            payload_ = json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'service_name': obj_.serviceName,
                    'channel': obj_.channel,
                }).encode('utf-8')
            self._mqttClient.publish(
                topic='zonesender/someipnode/subscribe',
                payload=payload_
            )
        elif isinstance(obj_,LinFrame):
            self._mqttClient.subscribe('zonesender/linparsernode/frame/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/linparsernode/subscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'frame',
                }).encode('utf-8')
            )
        elif isinstance(obj_,LinMessage):
            self._mqttClient.subscribe('zonesender/linparsernode/message/{0}/{1}'.format(obj_.frame_channel, obj_.frame_id))
            self._mqttClient.publish(
                topic='zonesender/linparsernode/subscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.frame_channel,
                    'name': obj_.frame_id,
                    'type': 'message',
                }).encode('utf-8')
            )
        elif isinstance(obj_,LinSignal) :
            self._mqttClient.subscribe('zonesender/linparsernode/signal/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/linparsernode/subscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'signal',
                }).encode('utf-8')
            )
        elif isinstance(obj_, DiagnosticEcuInfo):
            self._mqttClient.subscribe('zonesender/canudsnode/Rx/diagnostic_request')
            self._mqttClient.subscribe('zonesender/canudsnode/Rx/diagnostic_response')
            self._mqttClient.publish(
                topic='zonesender/canudsnode/subscribe',
                payload=json.dumps(
                    {
                        'client_id': self._mqttClient._client_id.decode('utf-8'),
                        'channel': obj_.channel,
                        'name': obj_.name,
                        'request_id_phys': obj_.request_id,
                        'response_id': obj_.response_id,
                        'function_id': obj_.function_id
                    }
                )
            )
        elif isinstance(obj_, DiagnosticEcuInfo_DoIP):
            self._mqttClient.subscribe('zonesender/doipudsnode/Rx/diagnostic_request')
            self._mqttClient.subscribe('zonesender/doipudsnode/Rx/diagnostic_response')
            self._mqttClient.publish(
                topic='zonesender/doipudsnode/subscribe',
                payload=json.dumps(
                    {
                        'client_id': self._mqttClient._client_id.decode('utf-8'),
                        'name': obj_.name,
                        'source_address': obj_.source_address,
                        'target_address': obj_.target_address
                    }
                )
            )

    def UnSubscribe(self, obj) -> None:
        ''' 取消订阅事件，调用该函数后，将不会再 OnXXX 的回调函数中收到相关消息

        :param obj: 需要取消订阅的对象，可以为如下类型\n
            - ZoneSender.ObjIo.CanMessage\n
            - ZoneSender.ObjIo.CanFrame\n
            - ZoneSender.ObjIo.CanSignal\n
            - ZoneSender.ObjIo.CanISignalIPdu\n
            - ZoneSender.ObjIo.SomeipPackage\n
        '''
        obj_ = obj
        if (isinstance(obj_, CanMessage)):
            self._mqttClient.unsubscribe('zonesender/canstacknode/message/{0}/{1}'.format(obj_.channel, hex(obj_.arbitration_id).lower()))
            self._mqttClient.publish(
                topic='zonesender/canstacknode/unsubscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'arbitration_id': obj_.arbitration_id,
                }).encode('utf-8')
            )
        elif (isinstance(obj_, CanFrame)):
            self._mqttClient.unsubscribe('zonesender/canparsernode/frame/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/canparsernode/unsubscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'frame',
                }).encode('utf-8')
            )
        elif (isinstance(obj_, CanISignalIPdu)):
            self._mqttClient.unsubscribe('zonesender/canparsernode/pdu/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/canparsernode/unsubscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'pdu',
                }).encode('utf-8')
            )
        elif (isinstance(obj_, CanSignal)):
            self._mqttClient.unsubscribe('zonesender/canparsernode/signal/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/canparsernode/unsubscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'signal',
                }).encode('utf-8')
            )
        elif (isinstance(obj_, SomeipPackage)):
            self._mqttClient.unsubscribe('zonesender/someipnode/someippackage/{0}'.format(obj_.serviceName))
            self._mqttClient.unsubscribe('zonesender/someipnode/someipcalling/{0}'.format(obj_.serviceName))
            self._mqttClient.publish(
                topic='zonesender/someipnode/unsubscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'service_name':obj_.serviceName,
                    'channel': obj_.channel,
                }).encode('utf-8')
            )
        elif (isinstance(obj_, LinFrame)):
            self._mqttClient.unsubscribe('zonesender/linparsernode/frame/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/linparsernode/unsubscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'frame',
                }).encode('utf-8')
            )
        elif (isinstance(obj_, LinMessage)):
            self._mqttClient.unsubscribe('zonesender/linparsernode/signal/{0}/{1}'.format(obj_.frame_channel, obj_.frame_id))
            self._mqttClient.publish(
                topic='zonesender/linparsernode/unsubscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.frame_channel,
                    'name': obj_.frame_id,
                    'type': 'message',
                }).encode('utf-8')
            )
        elif (isinstance(obj_, LinSignal)):
            self._mqttClient.unsubscribe('zonesender/linparsernode/signal/{0}/{1}'.format(obj_.channel, obj_.name))
            self._mqttClient.publish(
                topic='zonesender/linparsernode/unsubscribe',
                payload=json.dumps({
                    'client_id': self._mqttClient._client_id.decode('utf-8'),
                    'channel': obj_.channel,
                    'name': obj_.name,
                    'type': 'signal',
                }).encode('utf-8')
            )
        elif isinstance(obj_, DiagnosticEcuInfo):
            self._mqttClient.unsubscribe('zonesender/canudsnode/Rx/diagnostic_request')
            self._mqttClient.unsubscribe('zonesender/canudsnode/Rx/diagnostic_response')
            self._mqttClient.publish(
                topic='zonesender/canudsnode/unsubscribe',
                payload=json.dumps(
                    {
                        'client_id': self._mqttClient._client_id.decode('utf-8'),
                        'channel': obj_.channel,
                        'name': obj_.name,
                        'request_id_phys': obj_.request_id,
                        'response_id': obj_.response_id,
                        'function_id': obj_.function_id
                    }
                )
            )
        elif isinstance(obj_, DiagnosticEcuInfo_DoIP):
            self._mqttClient.unsubscribe('zonesender/doipudsnode/Rx/diagnostic_request')
            self._mqttClient.unsubscribe('zonesender/doipudsnode/Rx/diagnostic_response')
            self._mqttClient.publish(
                topic='zonesender/doipudsnode/unsubscribe',
                payload=json.dumps(
                    {
                        'client_id': self._mqttClient._client_id.decode('utf-8'),
                        'name': obj_.name,
                        'source_address': obj_.source_address,
                        'target_address': obj_.target_address
                    }
                )
            )

    def OnCanFrame(self, timestamp , can_frame: 'CanFrame') -> None:
        ''' [需要用户重写实现定制功能]\n
        当收到一个 CAN 报文应该做什么，此函数在收到任何订阅过的 CAN 报文的时候触发

        :param timestamp: 收到该数据的时间戳,ns
        :param can_frame: ZoneSender.ObjIo.CanFrame 收到的 CANFrame 对象
        '''
        pass

    def OnCanPdu(self, timestamp, can_pdu: 'CanISignalIPdu') -> None:
        ''' [需要用户重写实现定制功能]\n
        当收到一个 CAN PDU 应该做什么，此函数在收到任何订阅过的 CAN PDU 的时候触发

        :param timestamp: 收到该数据的时间戳,ns
        :param can_pdu: ZoneSender.ObjIo.CanISignalIPdu 收到的 CanISignalIPdu 对象
        '''
        pass

    def OnCanSignal(self, timestamp, can_signal: 'CanSignal') -> None:
        ''' [需要用户重写实现定制功能]\n
        当收到一个 CAN Signal 应该做什么，此函数在收到任何订阅过的 CAN Signal 的时候触发

        :param timestamp: 收到该数据的时间戳
        :param can_signal: ZoneSender.ObjIo.CanSignal 收到的 CanSignal 对象
        '''
        pass

    def OnDiagRequest_DoIP(self, diagnostic_request: DoIPDiagMessage):
        '''[需要用户重写实现定制功能]
        当收到一个DoIP诊断请求命令 应该做什么，此函数在收到任何订阅过的DoIP诊断请求的时候触发
        ：param diagnostic_request: 收到诊断请求的报文，包括target_address和诊断TP数据
        例如target_address：0x1000 cmd:[0x10, 0x01]
        '''
        pass

    def OnDiagResponse_DoIP(self, diagnostic_response: DoIPDiagMessage):
        '''[需要用户重写实现定制功能]
        当收到一个DoIP诊断请求命令 应该做什么，此函数在收到任何订阅过的DoIP诊断请求的时候触发
        ：param diagnostic_request: 收到诊断请求的报文，包括target_address和诊断TP数据
        例如target_address：0x0e80 cmd:[0x50, 0x01]
        '''
        pass

    def OnDiagRequest(self, diagnostic_request: CanDiagMessage):
        ''' [需要用户重写实现定制功能]
        当收到一个 CAN 诊断请求命令 应该做什么，此函数在收到任何订阅过的CAN 诊断请求的时候触发
        ：param diagnostic_request: 收到的诊断请求的报文，包括id和诊断TP数据
        例如 id：0x710 cmd: [0x10, 0x01]
        '''
        pass

    def OnDiagResponse(self, diagnostic_response: CanDiagMessage):
        '''[需要用户重写实现定制功能]
        当收到一个 CAN 诊断请求命令 应该做什么，此函数在收到任何订阅过的CAN 诊断请求的时候触发
        ：param diagnostic_request: 收到的诊断请求的报文，包括id和诊断TP数据
        例如 id：0x718 cmd: [0x50, 0x01]
        '''
        pass

    def OnCanMessage(self, timestamp, can_message: 'CanMessage') -> None:
        ''' [需要用户重写实现定制功能]\n
        当收到一个 CAN Message 应该做什么，此函数在收到任何订阅过的 CAN Message 的时候触发

        :param timestamp: 收到该数据的时间戳,ns
        :param can_message: ZoneSender.ObjIo.CanMessage 收到的 CanMessage 对象
        '''
        pass

    def OnSomeipPackage(self, timestamp, someip_package: 'SomeipPackage') -> None:
        ''' [需要用户重写实现定制功能]\n
        当收到一个 SomeipPackage 应该做什么，此函数在收到任何订阅过的 SomeipPackage 的时候触发

        :param timestamp: 收到该数据的时间戳,ns
        :param someip_package: ZoneSender.ObjIo.SomeipPackage 收到的 SomeipPackage 对象
        '''
        pass

    def OnSomeipCalling(self, timestamp, someip_in: SomeipPackage, someip_out: SomeipPackage) -> None:
        ''' [需要用户重写实现定制功能]\n
        作为 Provider 端调用，当收到 Someip Consumer 的请求做什么\n
        根据 someip_in 的数据做逻辑判断，给 someip_out.context 赋值实现自定义返回数据\n

        :param timestamp: flaot 收到该数据的时间戳,ns
        :param someip_in: ZoneSender.ObjIo.SomeipPackage Someip Consumer 端请求的数据
        :param someip_out: ZoneSender.ObjIp.SomeipPackage 需要填充的数据
        :param is_response:bool 是否恢复本次 request
        '''
        pass
    
    def OnSomeipBypass(self,timestamp,someip_package :'SomeipPackage') -> None :
        ''' [需要用户重写实现定制功能]\n
        当收到一个 SomeipPackage 应该做什么，此函数在收到任何订阅过的 SomeipPackage 的时候触发

        :param timestamp: 收到该数据的时间戳,ns
        :param someip_package: ZoneSender.ObjIo.SomeipPackage 收到的 SomeipPackage 对象
        '''
        pass

    def OnSomeipStateChange(self,timestamp,service : 'tuple',state : 'bool') -> None :
        ''' [需要用户重写实现定制功能]\n
        订阅的服务状态回调
        :param timestamp: flaot 收到该数据的时间戳,ns
        :param service: 服务的具体信息，为一个元组，（service_id,instance_id）
        :param state: 表明当前服务是否可用的状态
        '''
        pass

    def OnLinMessage(self,timestamp, lin_message: 'LinMessage') ->None :
        ''' [需要用户重写实现定制功能]\n
        当收到一个 LIN 报文应该做什么，此函数在收到任何订阅过的 LIN 报文的时候触发

        :param timestamp: 收到该数据的时间戳,ns
        :param lin_message: ZoneSender.ObjIo.LinMessage 收到的 LIN Message 对象
        '''
        pass
    
    def OnLinFrame(self,timestamp, lin_frame: 'LinFrame') ->None :
        ''' [需要用户重写实现定制功能]\n
        当收到一个 LIN 报文应该做什么，此函数在收到任何订阅过的 LIN 报文的时候触发

        :param timestamp: 收到该数据的时间戳,ns
        :param lin_frame: ZoneSender.ObjIo.LinFrame 收到的 LIN Frame 对象
        '''
        pass

    def OnLinSignal(self,timestamp, lin_signal: 'LinSignal') ->None :
        ''' [需要用户重写实现定制功能]\n
        当收到一个 LIN 信号应该做什么，此函数在收到任何订阅过的 LIN 信号的时候触发

        :param timestamp: 收到该数据的时间戳,ns
        :param lin_signal: ZoneSender.ObjIo.LinSignal 收到的 LIN Signal 对象
        '''
        pass
    
    def SendCan(self, obj, **kwargs) -> None:
        '''发送一条CAN报文, 数据将立刻发送

        :param obj: 要发送的 CAN 对象，可以是如下类型\n
            - ZoneSender.ObjIo.CanMessage\n
            - ZoneSender.ObjIo.CanISignalIPdu\n
        :param kwargs: 附加 key:value 型参数，有如下可能:\n
            - by: str 通过什么参数来发送，有如下可能:\n
                - 'data': 通过 obj.data 的数据来发送\n
                - 'context': 通过 obj.context 的数据来发送\n
        '''
        obj_ = obj
        try:
            if (isinstance(obj_, CanMessage)):
                d_ = {
                    'id': obj_.arbitration_id,
                    'ext': obj_.is_extended_id,
                    'rem': obj_.is_remote_frame,
                    'chl': obj_.channel,
                    'dlc': obj_.dlc,
                    'd': obj_.data,
                    'fd': obj_.is_fd,
                }
                self._mqttClient.publish(
                    topic='zonesender/canstacknode/requests/send_can_message',
                    payload=json.dumps(d_).encode('utf-8')
                )
            elif (isinstance(obj_, CanISignalIPdu)):
                d_ = {
                    'name': obj_.name,
                    'chl': obj_.channel,
                    'context': obj_.context,
                    'd': obj_.data,
                }
                d_['kwargs'] = kwargs
                self._mqttClient.publish(
                    topic='zonesender/canparsernode/requests/send_can_pdu',
                    payload=json.dumps(d_).encode('utf-8')
                )
        except Exception as e_:
            print(e_)

    def SetCycleSendTask(self, period_ms: 'int', obj, times: 'int' = -1) -> None:
        ''' 设置定时发送任务，定时把 obj 发送出去

        :param period_ms: 发送周期
        :param obj: 要发送的对象，支持以下类型\n
            - ZoneSender.ObjIo.CanMessage\n
            - ZoneSender.ObjIo.CanISignalIPdu\n
            - ZoneSender.ObjIo.CanFrame\n
        :param times: 发送的次数，规则如下\n
            - \-1(默认) 一直发送\n
            - 0 停止发送，可以对已经发送的对象设置0来停止发送\n
            - 任意正整数 N，连续发送 N 次\n
        :return: None
        '''
        period_ms_ = period_ms
        obj_ = obj
        times_ = times
        try:
            if (isinstance(obj_, CanMessage)):
                # 设置循环发送 CanMessage
                d_ = {
                    'name': obj_.name,
                    'id': obj_.arbitration_id,
                    'ext': obj_.is_extended_id,
                    'rem': obj_.is_remote_frame,
                    'chl': obj_.channel,
                    'dlc': obj_.dlc,
                    'd': obj_.data,
                    'fd': obj_.is_fd,
                    'times': times_,
                    'period': period_ms_,
                }
                self._mqttClient.publish(
                    topic='zonesender/canstacknode/requests/send_can_message_cyc',
                    payload=json.dumps(d_).encode('utf-8')
                )
            elif (isinstance(obj_, CanFrame)):
                # 设置循环发送 CanFrame
                d_ = {
                    'name': obj_.name,
                    'chl': obj_.channel,
                    'times': times_,
                    'period': period_ms_,
                    'd': [],    # TODO 暂时保留 d 来发送空数据，保持接口一致
                    'context': obj_.context,
                }
                self._mqttClient.publish(
                    topic='zonesender/canparsernode/requests/send_can_frame_cyc',
                    payload=json.dumps(d_).encode('utf-8')
                )
            elif (isinstance(obj_, CanISignalIPdu)):
                # 设置循环发送 CAN PDU
                d_ = {
                    'name': obj_.name,
                    'chl': obj_.channel,
                    'context': obj_.context,
                    'times': times_,
                    'period': period_ms_,
                }
                self._mqttClient.publish(
                    topic='zonesender/canparsernode/requests/send_can_pdu_cyc',
                    payload=json.dumps(d_).encode('utf-8')
                )
        except Exception as e_:
            print(e_)

    def SomeipCallAsync(self, someip_package: 'SomeipPackage', *args, **kwargs) -> None:
        ''' 作为 Client调用，请求一个 someip method | get | set

        :param someip_package: 要发送的 SomeipPackage
        :param by: str 设置使用什么参数发送 'context'|'payload'
        :return: None
        '''
        try:
            d_ = someip_package.ToDict()
            d_.update({'by': kwargs.get('by', 'context')})
            d_.update({'payload': d_['payload'].hex()})
            self._mqttClient.publish(
                topic='zonesender/someipnode/request/call',
                payload=json.dumps(d_).encode('utf-8')
            )
        except Exception as e_:
            print('ZoneSenderStone.SomeipCallAsync Exception {0}'.format(e_))

    def SomeipSetDefaultAnswer(self, someip_package: 'SomeipPackage') -> None:
        ''' 作为 Server 调用，设置后台 SomeIpServer 的数据

        :param someip_package: 要设置的 SomeipPackage
        :return: None
        '''
        try:
            d_ = {
                'sv_name': someip_package.serviceName,
                'ince_id': someip_package.instanceId,
                'if_name': someip_package.interfaceName,
                'if_type': someip_package.interfaceType,
                'context': someip_package.context,
                'channel': someip_package.channel,
            }
            self._mqttClient.publish(
                topic='zonesender/someipnode/request/setvalue',
                payload=json.dumps(d_).encode('utf-8'),
            )
        except Exception as e_:
            print('ZoneSenderStone.SomeipSetDefaultAnswer Exception {0}'.format(e_))

    def SomeipPublish(self, someip_package: 'SomeipPackage', *args, **kwargs) -> None:
        ''' 作为 Server 调用，发送一次 Notification 或者 Event

        :param someip_package: 要发布的 SomeipPackage
        :param by: str 设置使用什么参数发送 'context'|'payload'
        :return: None
        '''
        try:
            d_ = someip_package.ToDict()
            d_.update({'by': kwargs.get('by', 'context')})
            d_.update({'payload': d_['payload'].hex()})
            self._mqttClient.publish(
                topic='zonesender/someipnode/request/publish',
                payload=json.dumps(d_).encode('utf-8')
            )
        except Exception as e_:
            print('ZoneSenderStone.SomeipPublish Exception {0}'.format(e_))
    
    def SetLinData(self,obj) :
        '''设置LIN报文, 数据将立刻发送
        :param obj: 要发送的 LIN 对象，可以是如下类型\n
            - ZoneSender.ObjIo.LinFrame\n
            - ZoneSender.ObjIo.LinMessage\n
            - ZoneSender.ObjIo.LinSignal\n
        '''
        if isinstance(obj,LinMessage) :
            d_ = {
                'channel':obj.frame_channel,
                'id':obj.frame_id,
                'name' :obj.name,
                'data' :obj.frame_data
            }
            self._mqttClient.publish(
                    topic='zonesender/linparsernode/requests/set_frame_data',
                    payload=json.dumps(d_).encode('utf-8')
                )
        elif isinstance(obj,LinFrame) :
            d_ = {
                'channel':obj.channel,
                'id':obj.id,
                'name' :obj.name,
                }
            if obj.context:
                d_['data'] = obj.context
                d_['encode_type'] = 'unraw'
            elif obj.context_raw:
                d_['data'] = obj.context_raw
                d_['encode_type'] = 'raw'
            elif obj.data:
                d_['data'] = obj.data
            self._mqttClient.publish(
                    topic='zonesender/linparsernode/requests/set_frame_data',
                    payload=json.dumps(d_).encode('utf-8')
                )
        elif isinstance(obj,LinSignal) :
            d_ = {
                'channel':obj.channel,
                'name':obj.name
            }
            if obj.data_raw != None:
                d_['data'] = obj.data_raw
                d_['encode_type'] = 'raw' 
            elif obj.data != None:
                d_['data'] = obj.data
                d_['encode_type'] = 'unraw' 
            else:
                print('cant get valid signal value')
                return
            self._mqttClient.publish(
                    topic='zonesender/linparsernode/requests/set_signal_data',
                    payload=json.dumps(d_).encode('utf-8')
                )

    def diag_request_doip(self, obj):
        if isinstance(obj, DoIPDiagMessage):
            d_ = {
                'target_address': obj.target_address,
                'header_type': obj.type,
                'd': obj.cmd,
            }
            self._mqttClient.publish(
                topic='zonesender/doipudsnode/Tx/diagnostic_request',
                payload=json.dumps(d_).encode('utf-8')
            )

    def diag_response_doip(self, obj):
        if isinstance(obj, DoIPDiagMessage):
            d_ = {
                'target_address': obj.target_address,
                'header_type': obj.type,
                'd': obj.cmd,
            }
            self._mqttClient.publish(
                topic='zonesender/doipudsnode/Tx/diagnostic_response',
                payload=json.dumps(d_).encode('utf-8')
            )

    def diag_request(self, obj):
        if isinstance(obj, CanDiagMessage):
            d_ = {
                'id': obj.id,
                'd': obj.cmd,
                'dlc': obj.dlc,
                'fd': obj.is_fd,
            }
            self._mqttClient.publish(
                topic='zonesender/canudsnode/Tx/diagnostic_request',
                payload=json.dumps(d_).encode('utf-8')
            )

    def diag_response(self, obj):
        if isinstance(obj, CanDiagMessage):
            d_ = {
                'id': obj.id,
                'd': obj.cmd,
                'dlc': obj.dlc,
                'fd': obj.is_fd
            }
            self._mqttClient.publish(
                topic='zonesender/canudsnode/Tx/diagnostic_response',
                payload=json.dumps(d_).encode('utf-8')
            )

    def OnRecvLogMessage(self, log_msg: str) -> None:
        '''
        当收到后端的一些 log 信息做什么
        默认是打印
        用户可以通过重写该该函数实现定制功能,如：
        - 屏蔽 log
        - 写 log 到文件
        '''
        print(log_msg)

    def _OnMqttMessage(self, client: mqtt.Client, userdata, msg: mqtt.MQTTMessage) -> None:
        '''当收到MQTTMwssage的时候做什么

        :param client: mqtt client
        :param userdata: None
        :param msg: mqtt.MQTTMessage
        '''
        topic_split_ = msg.topic.split('/')
        # 消息分发
        if (topic_split_[1] == 'canstacknode'):
            recv_d_ = json.loads(msg.payload.decode('utf-8'))
            # 收到 CAN 数据
            if (topic_split_[2] == 'message'):
                # 收到 CANMessage
                self._DealWithCanMessage(recv_d_)
        elif (topic_split_[1] == 'canparsernode'):
            recv_d_ = json.loads(msg.payload.decode('utf-8'))
            # print(recv_d_)
            if (topic_split_[2] == 'frame'):
                # 收到 CanFrame
                self._DealWithCanFrame(recv_d_)
            elif (topic_split_[2] == 'signal'):
                # 收到CANSIgnal
                self._DealWithCanSignal(recv_d_)
            elif (topic_split_[2] == 'pdu'):
                # 收到CANPdu
                self._DealWithCanISignalIPdu(recv_d_)
        elif (topic_split_[1] == 'out'):
            self.OnRecvLogMessage(msg.payload.decode('utf-8'))
        elif (topic_split_[1] == 'someipnode'):
            recv_d_ = json.loads(msg.payload.decode('utf-8'))
            if (topic_split_[2] == 'someippackage'):
                # 收到 SomeipPackage
                # print(recv_d_)
                self._DealWithSomeipPackage(recv_d_)
            elif (topic_split_[2] == 'someipcalling'):
                # 作为 Provider 端收到 Someip Request 后做什么
                self._DealWithSomeipCalling(recv_d_)
            elif (topic_split_[2] == 'someipbypass') :
                self._DealWithSomeipBypass(recv_d_)
            elif (topic_split_[2] == 'statechange') :
                self.OnSomeipStateChange(recv_d_['t'],(recv_d_['srv_id'],recv_d_['inst_id']),recv_d_['state'])   
        elif topic_split_[1] == 'linstacknode' :
            pass
        elif topic_split_[1] == 'linparsernode':
            recv_d_ = json.loads(msg.payload.decode('utf-8'))
            if (topic_split_[2] == 'message'):
                # 收到 CanFrame
                self._DealWithLinMessage(recv_d_)
            elif (topic_split_[2] == 'signal'):
                # 收到CANSIgnal
                self._DealWithLinSignal(recv_d_)
            elif (topic_split_[2] == 'frame'):
                # 收到CANPdu
                self._DealWithLinFrame(recv_d_)

        elif topic_split_[1] == 'canudsnode' and topic_split_[2] == 'Rx':
            recv_d_ = json.loads(msg.payload.decode('utf-8'))
            if topic_split_[3] == 'diagnostic_request':
                self._DealWithCanUdsMessageRequest(recv_d_)
            elif topic_split_[3] == 'diagnostic_response':
                self._DealWithCanUdsMessageResponse(recv_d_)

        elif topic_split_[1] == 'doipudsnode' and topic_split_[2] == 'Rx':
            recv_d_ = json.loads(msg.payload.decode('utf-8'))
            if topic_split_[3] == 'diagnostic_request':
                self._DealWithDoIPUdsMessageRequest(recv_d_)
            elif topic_split_[3] == 'diagnostic_response':
                self._DealWithDoIPUdsMessageResponse(recv_d_)

    def _OnMqttConnect(self, client: mqtt.Client, userdata, flags, rc) -> None:
        '''
        连接到 MQTT Broker 的时候做什么
        '''
        self._mqttClient.subscribe('zonesender/out/info')
        self._mqttClient.subscribe('zonesender/out/warn')
        self._mqttClient.subscribe('zonesender/out/error')
        self._mqttClient.subscribe('zonesender/out/debug')
        self._mqttClient.subscribe('zonesender/someipnode/statechange')

    def _OnMqttDisconnect(self, client: mqtt.Client, userdata, rc) -> None:
        '''
        当断开与MQTT Broker 连接的时候做什么
        '''
        while (True):
            try:
                client.reconnect()
                break
            except Exception as e_:
                print(e_)
            time.sleep(2)

    def _DealWithDoIPUdsMessageRequest(self, recv_d: dict):
        diag_msg_ = DoIPDiagMessage(target_address=recv_d['target_address'], header_type=recv_d['header_type'], cmd=recv_d['d'])
        self._threadPool.submit(self.OnDiagRequest_DoIP, diag_msg_)

    def _DealWithDoIPUdsMessageResponse(self, recv_d: dict):
        # print("_DealWithDoIPUdsMessageResponse", recv_d)
        diag_msg_ = DoIPDiagMessage(target_address=recv_d['target_address'], header_type=recv_d['header_type'], cmd=recv_d['d'])
        self._threadPool.submit(self.OnDiagResponse_DoIP, diag_msg_)

    def _DealWithCanUdsMessageRequest(self, recv_d: dict):
        '''处理接收到的诊断请求消息'''
        diag_msg_ = CanDiagMessage(id=recv_d['id'], cmd=recv_d['d'])
        self._threadPool.submit(self.OnDiagRequest, diag_msg_)

    def _DealWithCanUdsMessageResponse(self, recv_d: dict):
        '''处理接收到的诊断响应消息'''
        diag_msg_ = CanDiagMessage(id=recv_d['id'], cmd=recv_d['d'])
        self._threadPool.submit(self.OnDiagResponse, diag_msg_)

    def _DealWithCanMessage(self, recv_d: 'dict') -> None:
        '''
        处理接收到的 CaneMessage 消息
        '''
        can_msg_ = CanMessage(
            arbitration_id=recv_d['id'], 
            channel=recv_d['chl'], 
            dlc=recv_d['dlc'], 
            data=recv_d['d'],
            is_fd=recv_d['fd'],
            is_extended_id=recv_d['ext'],
            is_remote_frame=recv_d['rem'])
        self._threadPool.submit(
            self.OnCanMessage,
            recv_d['t'], can_msg_
        )

    def _DealWithCanFrame(self, recv_d: 'dict') -> None:
        '''
        处理收到的 CanFrame 消息
        '''
        can_frame_ = CanFrame(
            name=recv_d['name'],
            channel=recv_d['chl']
        )
        can_frame_.data = recv_d['d']
        can_frame_.dlc = recv_d['dlc']
        can_frame_.id = recv_d['id']
        self._threadPool.submit(
            self.OnCanFrame,
            recv_d['t'], can_frame_
        )

    def _DealWithCanISignalIPdu(self, recv_d: 'dict') -> None:
        '''
        处理收到的 CanISignalIPdu 消息
        '''
        can_pdu_ = CanISignalIPdu(
            name=recv_d['name'],
            channel=recv_d['chl'],
            context=recv_d['cnt'],
        )
        can_pdu_.data = recv_d['d']
        self._threadPool.submit(
            self.OnCanPdu,
            recv_d['t'], can_pdu_
        )

    def _DealWithCanSignal(self, recv_d: 'dict') -> None:
        '''
        处理收到的 CanSignal 消息
        '''
        can_signal_ = CanSignal(
            name=recv_d['name'],
            channel=recv_d['chl'],
            data=recv_d['d'],
            unit=recv_d['u'],
            mean=recv_d['m'],
        )
        self._threadPool.submit(
            self.OnCanSignal,
            recv_d['t'], can_signal_
        )

    def _DealWithSomeipPackage(self, recv_d: 'dict') -> None:
        '''
        处理接收到的 SomeipPackage
        '''
        recv_d['payload'] = bytes.fromhex(recv_d['payload'])
        self._threadPool.submit(
            self.OnSomeipPackage,
            recv_d['t'], SomeipPackage.From(recv_d)
        )

    def _DealWithSomeipCalling(self, recv_d: 'dict') -> None:
        '''
        作为 Provider 端调用，处理 Someip Request
        '''
        recv_d['payload'] = bytes.fromhex(recv_d['payload'])
        self._threadPool.submit(
            self._DealWithSomeipCalling_,
            recv_d,
        )

    def _DealWithSomeipCalling_(self, recv_d: 'dict') -> None:
        '''
        self._DealWithSomeipCalling 的线程函数
        '''
        someip_in_ = SomeipPackage.From(recv_d)
        someip_out_ = SomeipPackage.From(recv_d)
        someip_out_.context = {}
        self.OnSomeipCalling(recv_d['t'], someip_in_, someip_out_)
        
        self.SomeipSetDefaultAnswer(someip_out_)

    def _DealWithLinMessage(self,recv_d:dict) ->None :
        lin_message_ = LinMessage(
            channel= recv_d['chl'],
            frameId= recv_d['id'],
            data = recv_d['d_real'],
            dlc= recv_d['dlc'],
            context= recv_d['d_'],
            context_raw= recv_d['d_raw']
        )
        lin_message_.name = recv_d['name']
        self._threadPool.submit(
            self.OnLinMessage,
            recv_d['t'], lin_message_
        )
    
    def _DealWithLinFrame(self,recv_d:dict) ->None :
        lin_frame_ = LinFrame(
            name= recv_d['name'],
            channel= recv_d['chl'],
            context= recv_d['d_'],
            context_raw= recv_d['d_raw']
        )
        lin_frame_.id = recv_d['id']
        lin_frame_.dlc = recv_d['dlc']
        lin_frame_.data = recv_d['d_real']
        self._threadPool.submit(
            self.OnLinFrame,
            recv_d['t'], lin_frame_
        )
    
    def _DealWithLinSignal(self,recv_d:dict) ->None :
        lin_signal_ = LinSignal(
            name= recv_d['name'],
            channel= recv_d['chl'],
            data_raw= recv_d['d_raw'],
            data= recv_d['d_']
        )
        lin_signal_.id = recv_d['id']
        self._threadPool.submit(
            self.OnLinSignal,
            recv_d['t'], lin_signal_
        )

    def _DealWithSomeipBypass(self, recv_d: 'dict') -> None:
        '''
        处理接收到的 SomeipBypass
        '''
        recv_d['payload'] = bytes.fromhex(recv_d['payload'])
        self._threadPool.submit(
            self.OnSomeipBypass,
            recv_d['t'], SomeipPackage.From(recv_d)
        )
