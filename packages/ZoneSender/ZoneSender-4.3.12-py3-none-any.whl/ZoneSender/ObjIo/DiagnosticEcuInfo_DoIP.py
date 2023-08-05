from .ZoneSenderObject import ZoneSenderObject


class DiagnosticEcuInfo_DoIP(ZoneSenderObject):
    def __init__(self, ecu_name: str, source_address: int, target_address: int):
        super().__init__()
        self.ecu_name = ecu_name
        self.source_address = source_address
        self.target_address = target_address

    def __str__(self):
        return f'{self.ecu_name} channel: {self.source_address}, request_id: {self.target_address}'