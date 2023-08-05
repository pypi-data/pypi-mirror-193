import json
import os
import typing

from .CanParserNodeClient import CanParserNodeClient
from .CanStackNodeClient import CanStackNodeClient
from .SomeipNodeClient import SomeipNodeClient
from .LinParseNodeClient import LinParseNodeClient
from .LinStackNodeClient import LinStackNodeClient
from .LogReplayNodeClient import LogReplayNodeClient
from .CanUdsNodeClient import CanUdsNodeClient
from .TcpIpNodeClient import TcpIpNodeClient
from .ConfigNodeClient import ConfigNodeClient
from .DoIPUdsNodeClient import DoIPUdsNodeClient


class ZoneSenderFramework(object):
    '''
    ZoneSender 的基础类，可以用来实现对硬件的简单控制\n
    该对象有几个成员变量，可以查看相应的对象介绍页面来了解函数列表:\n
        - CanStack: ZoneSender.CanStackNodeClient\n
        - CanParser: ZoneSender.CanParserNodeClient\n
        - SomeipStack: ZoneSender.SomeipNodeClient\n
    通过调用几个成员变量的函数实现各种控制功能\n
    '''
    def __init__(self) -> None:
        super().__init__()
        self.CanStack = CanStackNodeClient()
        self.CanParser = CanParserNodeClient()
        self.SomeipStack = SomeipNodeClient()
        self.LinStack = LinStackNodeClient()
        self.LinParser = LinParseNodeClient()
        self.LogReplay = LogReplayNodeClient()
        self.CanUds = CanUdsNodeClient()
        self.TcpIpStack = TcpIpNodeClient()
        self.Config = ConfigNodeClient()
        self.DoIPUds = DoIPUdsNodeClient()


    def Reset(self) -> None:
        ''' 复位所有功能，包括:\n
            - 复位 CAN 协议栈\n
            - 清空 CAN DB 文件\n
            - 清除所有数据记录任务\n
            - 清空 SomeipStack \n
            - 清空 SomeipStack Arxml 文件\n
            - 复位 LIN 协议栈\n
            - 清空 LIN ldf文件\n

        '''
        self.CanStack.StopCanStack()
        self.CanStack.ClearSubscribe()
        self.CanStack.ClearSend()
        self.CanStack.ClearLogger()
        self.CanParser.ClearSubscribe()
        self.CanParser.ClearCanDb()
        self.SomeipStack.Reset()
        self.LinStack.reset()
        self.LinParser.clearChannelConfig()
        self.LinParser.clearSubscribe()
        self.DoIPUds.reset()

    def Reset_LIN(self) ->None :
        ''' 复位所有功能，包括:\n
            - 复位 LIN 协议栈\n
            - 清空 LIN ldf文件\n
        '''
        self.LinStack.reset()
        self.LinParser.clearChannelConfig()
        self.LinParser.clearSubscribe()

    def Reset_CAN(self) ->None :
        ''' 复位所有功能，包括:\n
            - 复位 CAN 协议栈\n
            - 清空 CAN DB 文件\n
            - 清除所有数据记录任务\n
        '''
        self.CanStack.StopCanStack()
        self.CanStack.ClearSubscribe()
        self.CanStack.ClearSend()
        self.CanStack.ClearLogger()
        self.CanParser.ClearSubscribe()
        self.CanParser.ClearCanDb()
    
    def Reset_SomeIp(self) -> None :
        ''' 复位所有功能，包括:\n
            - 清空 SomeipStack \n
            - 清空 SomeipStack Arxml 文件\n
        '''
        self.SomeipStack.Reset()
        


