from obsw.telemetry.telemetry_packet import TelemetryPacket


class PUSTelemetryPacket(TelemetryPacket):
    __pus_version = 0b0010
    __packet_id = 0

    def __init__(self):
        super().__init__()
        PUSTelemetryPacket.__packet_id = None
        self.__packet_sq_flags = 0b11 << 14
        self.__packet_sq_count = 0
        self.__packet_sq_ctrl = self.__packet_sq_flags + self.__packet_sq_count
        self.__apid = None
        self.__msg_type_counter = 0
        self.__user_data = None
        self.__src_data = None
        self.__packet_err_ctrl = None

    @staticmethod
    def get_pus_version():
        return PUSTelemetryPacket.__pus_version

    @staticmethod
    def get_packet_id():
        assert self.__apid is not None
        return PUSTelemetryPacket.__packet_id

    def get_packet_sq_ctrl(self):
        return self.__packet_sq_ctrl

    def set_packet_sq_count(self, count):
        assert count < 2**14-1
        self.__packet_sq_count = count
        self.__packet_sq_ctrl = self.__packet_sq_flags + self.__packet_sq_count

    def get_apid(self):
        return self.__apid

    def set_apid(self, apid):
        # packet id for ccsds TM packet is 2 bytes long.
        # Bit sequence left to right (MSB to LSB) is as below
        # --------------------------------------------------------|
        # packet version |             packet id                  |
        #                |----------------------------------------|
        #                |packet type| secondary hdr flag| apid   |
        # --------------------------------------------------------|
        # 3 bits         |1 bit      | 1 bit             | 11 bits|
        # --------------------------------------------------------|
        #     000        |0 (TM)     | 1 (PUS hdr)       | apid   |
        # --------------------------------------------------------|
        assert apid < 2**11
        self.__apid = apid
        PUSTelemetryPacket.__packet_id = 0b0001 << 11
        PUSTelemetryPacket.__packet_id += apid

    def get_msg_type_counter(self):
        return self.__msg_type_counter

    def set_msg_type_counter(self, msg_type_ounter):
        assert msg_counter >= 0
        self.__msg_type_counter = msg_type_ounter

    def get_user_data(self):
        return self.__user_data

    def get_src_data(self):
        return self.__src_data

    def get_packet_err_ctrl(self):
        return self.__packet_err_ctrl

    def is_object_configured(self):
        return super().is_object_configured()\
             and self.__type > 0\
                 and self.__subtype > 0\
                     and self.__destination > 0\
                         and PUSTelemetryPacket.__packet_id > 0\
                             and PUSTelemetryPacket.__obs_clock is not None\
                                 and self.__time_tag > 0
