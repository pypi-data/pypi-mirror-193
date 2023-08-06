from .ZoneSenderObject import ZoneSenderObject


class DoIPDiagMessage(ZoneSenderObject):
    def __init__(self, target_address: int, header_type:int, cmd: list):
        super().__init__()
        self.target_address = target_address
        self.type = header_type
        self.cmd = cmd
