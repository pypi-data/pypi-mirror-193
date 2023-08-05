from obsw.telemetry.telemetry_packet import PUSTelemetryPacket
from obsw.definitions import ClassID
from obsw.definitions.constants import *

class PUSTcVerificationPacket(PUSTelemetryPacket):
    def __init__(self):
        super().__init__()
        self.set_class_id(ClassID.ID_PUS_TC_VERIFICATION_PACKET.value)
        self.set_type(PUS_TYPE_TC_VER)
        self.__src_data_size = 0
        self.__request_id = None
        self.__tc_pid = None
        self.__tc_packet_sq_ctrl = None
        self.__telecommand_id = 0
        self.__failure_notice = None
        self.__error_code = 0
        self.__failure_data = None

    def set_subtype(self, tm_subtype):
        super().set_subtype()
        if self.get_subtype() in [PUS_SUBTYPE_TC_VER_ACC_SC, PUS_SUBTYPE_TC_VER_EXE_STR_SC, PUS_SUBTYPE_TC_VER_EXE_PRO_SC, PUS_SUBTYPE_TC_VER_EXE_END_SC]:
            self.__src_data_size = 32
        else:
            self.__src_data_size = 48 # assuming err code of 16 bits

    def get_number_of_bytes(self):
        pass

    def get_request_id(self):
        assert self.__request_id is not None and self.__tc_pid is not None and self.__tc_packet_sq_ctrl is not None
        return self.__request_id

    def get_tc_pid(self):
        assert self.__tc_pid is not None
        return self.__tc_pid

    def set_tc_pid(self, pid):
        assert pid < 2**16
        self.__tc_pid = pid
        self.__request_id = self.__tc_pid << 16

    def get_tc_packet_sq_ctrl(self):
        assert self.__tc_packet_sq_ctrl is not None, "Set sequence ctrl first."
        return self.__tc_packet_sq_ctrl

    def set_tc_packet_sq_ctrl(self, packet_sq_ctrl):
        assert self.__tc_pid is not None, "Set TC PID first."
        assert packet_sq_ctrl < 2**16 - 1
        self.__tc_packet_sq_ctrl = packet_sq_ctrl
        self.__request_id += self.__tc_packet_sq_ctrl

    def get_telecommand_id(self):
        return self.__telecommand_id

    def set_telecommand_id(self, tc_id):
        assert tc_id > 0
        self.__telecommand_id = tc_id

    def get_failure_notice(self):
        assert self.__error_code!=0
        return self.__failure_notice

    def get_error_code(self):
        assert self.__error_code != 0
        return self.__error_code

    def set_error_code(self, error_code):
        assert error_code > 0
        assert self.__request_id is not None, "Set Request ID data first."
        self.__error_code = error_code
        self.__failure_notice = self.__error_code

    def get_bytes(self):
        pass

    def update(self):
        pass
