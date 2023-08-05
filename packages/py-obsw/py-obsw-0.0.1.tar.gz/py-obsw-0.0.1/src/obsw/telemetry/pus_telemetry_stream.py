from obsw.telemetry.telemetry_stream import TelemetryStream
from obsw.definitions import ClassID
from obsw.base.root import RootObject
from obsw.events import EventType
from obsw.telemetry.pus_telemetry_packet import PUSTelemetryPacket


class PUSTelemetryStream(TelemetryStream):
    def __init__(self):
        super().__init__()
        self.__tmdata = None
        self.__size = 0
        # write counter is the index where the next byte is to be written
        # the first byte contains the number of tm packets written to tm stream
        # since last reset
        self.__write_counter = 0
        self.__pkt_seq_ctrl = 0
        self.__n_additional_bytes = 11 + 4  # size of Timestamp. why 11?
        self.set_class_id(ClassID.ID_PUS_TELEMETRY_STREAM.value)

    def set_capacity(self, n):
        self.__size = n
        self.__tmdata = bytearray(n)

    def get_start_address(self):
        assert self.__tmdata is not None
        return self.__tmdata

    def get_pkt_counter(self):
        assert self.__tmdata is not None
        return self.__tmdata[0]

    def get_write_counter(self):
        return self.__write_counter

    def get_seq_ctrl(self):
        return self.__pkt_seq_ctrl % 0x40

    def reset(self):
        assert self.__size > 0 and self.__tmdata is not None
        self.__write_counter = 1
        self.__tmdata[0] = 0

    def flush(self):
        self.reset()

    def get_capacity(self):
        assert self.__size > 0
        return self.__size

    def does_packet_fit(self, tm_packet):
        assert self.is_object_configured()
        return (tm_packet.get_number_of_bytes() + self.__n_additional_bytes) <= (
            self.__size - self.__write_counter
        )

    def write(self, tm_packet):
        assert self.is_object_configured()
        EIGHT_BITS = 0b11111111
        n_tm_data = tm_packet.get_number_of_bytes()
        if self.__pkt_seq_ctrl == 0xFF:
            self.__pkt_seq_ctrl = 0xC0
        else:
            self.__pkt_seq_ctrl += 1
        if (
            self.__write_counter + n_tm_data + self.__n_additional_bytes
            > self.get_capacity()
        ):
            RootObject.get_event_repository().create(self, EventType.EVT_TM_STREAM_END)
            return
        pkt_id = PUSTelemetryPacket.get_packet_id()

        # write packet ID: 2 bytes
        self.__tmdata[self.__write_counter] = pkt_id >> 8
        self.__tmdata[self.__write_counter + 1] = pkt_id & EIGHT_BITS

        # write sequence control: 2 bytes
        self.__tmdata[self.__write_counter + 2] = self.__pkt_seq_ctrl >> 8
        self.__tmdata[self.__write_counter + 3] = self.__pkt_seq_ctrl & EIGHT_BITS

        # write number of additional bytes
        t3 = self.__n_additional_bytes - 6 + n_tm_data
        self.__tmdata[self.__write_counter + 4] = t3 >> 8
        self.__tmdata[self.__write_counter + 5] = t3 & EIGHT_BITS

        # update write counter: 6 new bytes are added
        self.__write_counter += 6

        # write packet data field
        self.__tmdata[self.__write_counter] = PUSTelemetryPacket.get_pus_version() << 4
        self.__tmdata[self.__write_counter + 1] = tm_packet.get_type()
        self.__tmdata[self.__write_counter + 2] = tm_packet.get_subtype()

        # add time tag: 4 bytes for unix clock time tag (int(time.time()))
        self.__tmdata[self.__write_counter + 3] = tm_packet.get_time_tag() >> 24
        self.__tmdata[self.__write_counter + 4] = (
            tm_packet.get_time_tag() >> 16
        ) & EIGHT_BITS
        self.__tmdata[self.__write_counter + 5] = (
            tm_packet.get_time_tag() >> 8
        ) & EIGHT_BITS
        self.__tmdata[self.__write_counter + 6] = tm_packet.get_time_tag() & EIGHT_BITS

        # update write counter
        self.__write_counter += 7

        # add user data
        user_data = tm_packet.get_user_data()
        for b in user_data:
            self.__tmdata.append(b)
            self.__write_counter += 1

        # packet error control
        self.__tmdata[self.__write_counter] = 0
        self.__tmdata[self.__write_counter + 1] = 0

        # update the number of TMs written
        self.__tmdata[0] += 1

    def is_object_configured(self):
        return super().is_object_configured() and self.__size > 0 and self.__tmdata is not None
