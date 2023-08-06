import grpc
from . import ZoneSenderData
from .Protos import ConfigNode_pb2, ConfigNode_pb2_grpc


class ConfigNodeClient(object):
    def __init__(self):
        self._configStub = ConfigNode_pb2_grpc.ConfigNodeStub(
            channel=grpc.insecure_channel(
                target=f'{ZoneSenderData.CONFIG_NODE_IP}:{ZoneSenderData.CONFIG_NODE_PORT}',
                options=ZoneSenderData.GRPC_OPTIONS
            )
        )

    def getHardwareInfo(self, types: list):
        res = self._configStub.getHardwareInfo(ConfigNode_pb2.hardware_type(
            type=types
        ))
        return res.hardware


