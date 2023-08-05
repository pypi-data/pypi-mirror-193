from obsw.telecommand.telecommand_loader import TelecommandLoader
from obsw.telecommand.telecommand_factory import TelecommandFactory
from obsw.telecommand.pus_telecommand import PUSTelecommand
from obsw.definitions.constants import *
from obsw.base.root import RootObject
from obsw.events import EventType


class PUSTelecommandLoader(TelecommandLoader):
    def __init__(self):
        super().__init__()

        # initialize the TC buffer (where raw TC data is stored) to None
        self.__tc_buffer = None

        # initialize max length of TC packet data field, this excludes header
        self.__max_tc_data_pkt_length = 0

        # initialize max number of TCs that can be held to zero
        self.__max_number_of_tc = 0

    def load(self):
        """Loads TCs into TCManager by creating factory managed
        TCs from raw data stored in its buffer.

        This method is usually triggered externally periodically or
        using interrupts.
        """
        assert self.__tc_buffer is not None, "TC Buffer area is not set."
        assert self.__max_tc_data_pkt_length > 0, "Max TC Packet Data length not set."
        assert self.__max_number_of_tc > 0, "Max number of TCs not set."

        # get singleton factory
        tc_factory = TelecommandFactory.get_instance()
        print(f'tc factory : {tc_factory.is_object_configured()}')
        n_tc = self.__tc_buffer[0]  # first byte represents number of TCs
        if n_tc > self.__max_number_of_tc:
            RootObject.get_event_repository().create(
                self, EventType.EVT_TOO_MANY_TC_PKT.value)
            return

        idx_packet_start = 1  # keeps track of where the packet ends
        for idx in range(n_tc):
            ## NOTE: indexing a bytearray in python creates a shallow copy

            # -----------------------PACKET ID------------------------------------------------
            # obtain packet id (CCSDS Packet ID and Packet Version), 2 Bytes
            tc_pkt_id_arr = self.__tc_buffer[idx_packet_start:idx_packet_start +
                                         CCSDS_PKT_ID_NBYTES]
            tc_pkt_id = tc_pkt_id_arr[0]<<8
            tc_pkt_id += tc_pkt_id_arr[1]
            print(f'Packet ID: {tc_pkt_id}')
            

            #---------------------- PACKET SQ CTRL--------------------------------------------

            # packet sequence control, 2 Bytes
            tc_pkt_seq_ctrl_arr = self.__tc_buffer[
                idx_packet_start + CCSDS_PKT_ID_NBYTES:idx_packet_start +
                CCSDS_PKT_ID_NBYTES + CCSDS_PKT_SQ_CTRL_NBYTES]
            tc_pkt_seq_ctrl = tc_pkt_seq_ctrl_arr[0]<<8
            tc_pkt_seq_ctrl += tc_pkt_seq_ctrl_arr[1]
            print(f'SQ Ctrl: {tc_pkt_seq_ctrl}')

            # -------------------- PACKET DATA LENGTH (secondary hdr + user data)-------------

            # packet data length, 2 Bytes
            tc_data_pkt_length_arr = self.__tc_buffer[
                idx_packet_start + CCSDS_PKT_ID_NBYTES +
                CCSDS_PKT_SQ_CTRL_NBYTES:idx_packet_start +
                CCSDS_PKT_ID_NBYTES + CCSDS_PKT_SQ_CTRL_NBYTES +
                CCSDS_PKT_DATA_LENGTH_DEFINE_NBYTES]
            tc_data_pkt_length = tc_data_pkt_length_arr[0]<<8
            tc_data_pkt_length += tc_data_pkt_length_arr[1]
            print(f"data packet length : {tc_data_pkt_length}")

            # --------------------PACKET SECONDARY HEADER (PUS)-------------------------------

            ## packet secondary header (PUS packet header) starts at 7th Byte from left

            # TC Acknowledgement Flag, 7th Byte of TC from left (includes PUS version)
            tc_ack = self.__tc_buffer[idx_packet_start +
                                      CCSDS_PKT_PRM_HDR_NBYTES]

            # TC Type, 1 Byte, starts at 8th Byte of TC from left
            tc_type = self.__tc_buffer[idx_packet_start +
                                       CCSDS_PKT_PRM_HDR_NBYTES +
                                       PUS_HEADER_TC_ACK_NBYTES]
            print(f"type : {tc_type}")

            # TC Subtype, 1 Byte, 9th Byte of TC from left
            tc_subtype = self.__tc_buffer[idx_packet_start +
                                          CCSDS_PKT_PRM_HDR_NBYTES +
                                          PUS_HEADER_TC_ACK_NBYTES +
                                          PUS_HEADER_TC_SERVICE_NBYTES]
            print(f"subtype : {tc_subtype}")

            # TC Source, 2 Bytes, 10th and 11th Byte of TC
            tc_source_arr = self.__tc_buffer[
                idx_packet_start + CCSDS_PKT_PRM_HDR_NBYTES +
                PUS_HEADER_TC_ACK_NBYTES + PUS_HEADER_TC_SERVICE_NBYTES +
                PUS_HEADER_TC_SUBSERVICE_NBYTES:idx_packet_start +
                CCSDS_PKT_PRM_HDR_NBYTES + PUS_HEADER_TC_ACK_NBYTES +
                PUS_HEADER_TC_SERVICE_NBYTES +
                PUS_HEADER_TC_SUBSERVICE_NBYTES + PUS_HEADER_TC_SRC_ID_NBYTES]
            tc_source = tc_source_arr[0]<<8
            tc_source += tc_source_arr[1]
            print(f"source : {tc_source}")

            # TC Spare, last byte of PUS TC HEADER, 12th Byte of TC
            tc_spare = self.__tc_buffer[idx_packet_start +
                                        CCSDS_PKT_PRM_HDR_NBYTES +
                                        PUS_HEADER_TC_NBYTES - 1]
            print(f"tc spare: {tc_spare}")

            # ----------------------USER DATA FIELD-------------------------------------------
            # starts at 13th Byte of TC and of length equal to USER DATA LENGTH
            tc_usr_data_length = tc_data_pkt_length - PUS_HEADER_TC_NBYTES
            tc_usr_data = self.__tc_buffer[
                idx_packet_start + CCSDS_PKT_PRM_HDR_NBYTES +
                PUS_HEADER_TC_NBYTES:idx_packet_start +
                CCSDS_PKT_PRM_HDR_NBYTES + PUS_HEADER_TC_NBYTES +
                tc_usr_data_length]
            print(f"user data length : {tc_usr_data_length}")
            print(f"user data: {tc_usr_data}")

            # continue parsing next packet if packet is invalid
            if tc_pkt_id != PUSTelecommand.get_packet_id():
                idx_packet_start += CCSDS_PKT_PRM_HDR_NBYTES + tc_data_pkt_length
                continue

            # create event if TC is too long
            if tc_data_pkt_length > self.__max_tc_data_pkt_length:
                RootObject.get_event_repository().create(
                    self, EventType.EVT_TC_TOO_LONG.value)
                return

            tc_object = None
            fast_data_load = True
            if tc_type == PUS_TYPE_MOD_CTRL and tc_subtype == PUS_SUBTYPE_MOD_CTRL_SM:
                print('allocating PUS Mode Control CMD...')
                tc_object = tc_factory.allocate_mode_change_telecommand()
                print(f'allocated PUS Mode Control CMD...{tc_object}')
            elif tc_type == PUS_TYPE_DOOF and tc_subtype == PUS_SUBTYPE_DOOF_INCREMENT:
                tc_object = tc_factory.allocate_doof_telecommand()
            else:
                RootObject.get_event_repository().create(
                    self, EventType.EVT_TC_UNKNOWN_TYPE.value)
                idx_packet_start += CCSDS_PKT_PRM_HDR_NBYTES + tc_data_pkt_length
                continue

            if tc_object is None:
                RootObject.get_event_repository().create(
                    self, EventType.EVT_TC_NOT_AVAIL.value)
                idx_packet_start += CCSDS_PKT_PRM_HDR_NBYTES + tc_data_pkt_length
                continue

            tc_object.set_telecommand_id(tc_pkt_seq_ctrl)
            tc_object.set_type(tc_type)
            tc_object.set_subtype(tc_subtype)
            tc_object.set_source(tc_source)
            tc_object.set_ack_level(tc_ack)
            tc_object.set_time_tag(1)

            if fast_data_load:
                tc_object.set_raw_data_fast(tc_usr_data)
            else:
                for idx_byte in range(len(tc_usr_data)):
                    tc_object.set_raw_data_safe(idx_byte,
                                                tc_usr_data[idx_byte])
            self.get_tc_manager().load(tc_object)
            idx_packet_start += CCSDS_PKT_PRM_HDR_NBYTES + tc_data_pkt_length

    def release(self, tc):
        """Releases a TC by setting it as not in use.
        """
        assert self.__tc_buffer is not None, "TC Buffer should not be None. Configure object."
        assert self.__max_number_of_tc > 0, "Max number of TC are zero."
        assert self.__max_tc_data_pkt_length > 0, "Packet data field size is zero."
        assert tc is not None, "Cannot release None TC. Provide valid TC Object."
        tc.set_in_use(False)

    def set_tc_buffer(self, buffer):
        assert buffer is not None, "Buffer cannot be None."
        self.__tc_buffer = buffer

    def set_max_tc_pkt_length(self, max_length):
        """set max size of TC Packet including header
        """
        assert max_length > PUS_HEADER_TC_NBYTES, "Length should be greater than PUS_HEADER"
        self.__max_tc_data_pkt_length = max_length - PUS_HEADER_TC_NBYTES

    def get_max_tc_pkt_length(self):
        return self.__max_tc_data_pkt_length + PUS_HEADER_TC_NBYTES

    def set_max_number_of_tc(self, number):
        assert number > 0, "Number of TCs should be greater than 0."
        self.__max_number_of_tc = number

    def get_max_number_of_tc(self):
        return self.__max_number_of_tc

    def is_object_configured(self):
        return super().is_object_configured() \
            and self.__tc_buffer is not None\
                and self.__max_number_of_tc!=0\
                    and self.__max_tc_data_pkt_length!=0
