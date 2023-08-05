from obsw.telecommand import Telecommand
from obsw.definitions.constants import *

class PUSTelecommand(Telecommand):
    __pus_version = 0b0010
    # packet ID as defined in CCSDS. Packet ID is unique for an application.
    # Packet ID containts APID, which is the destination of the TC.
    # Source ID on the other hand, is the ID of the issuer (source) of the TC.
    # Therefore, when a TC is being loaded to application, the APID in the TC should match
    # the APID of the application.
    # When a TC is being created by this application, set the Source ID in the TC to the 
    # APID of the application.
    __packet_id = 0
    apid = 0

    #-----------------------------------------------------------------------
    # acceptance ack flag tells the destination app to provide ack services
    # In PUS, Bit 0 is the MSB
    # for requesting successful acceptance: Bit 3 is set to 1 -> 0001
    # for requesting start execution ack: Bit 2 is set to 1 -> 0010
    # for requesting successful progress ack: Bit 1 is set to 1 -> 0100
    # for requesting successful completion ack: Bit 0 is set to 1 -> 1000
    # ----------------------------------------------------------------------
    acceptance_ack = 1
    start_ack = 2
    progress_ack = 4
    completion_ack = 8

    def __init__(self):
        super().__init__()
        self.__tc_id = 0
        self.__tc_type = 0
        self.__tc_subtype = 0
        self.__tc_source = 0
        self.__ack_level = 0

        # validity code is zero if data is valid, and non-zero if invalid
        # value of code defines the type of error in data
        self.__validity_check_code = 0

    def is_valid(self):
        return self.__validity_check_code == 0

    def get_validity_check_code(self):
        return self.__validity_check_code

    def set_validity_check_code(self, code):
        self.__validity_check_code = code

    @staticmethod
    def get_packet_id():
        return PUSTelecommand.__packet_id

    @staticmethod
    def set_apid(apid):
        # packet id for ccsds TC packet is 2 bytes long.
        # Bit sequence left to right (MSB to LSB) is as below
        # --------------------------------------------------------|
        # packet version |             packet id                  |
        #                |----------------------------------------|
        #                |packet type| secondary hdr flag| apid   |
        # --------------------------------------------------------|
        # 3 bits         |1 bit      | 1 bit             | 11 bits|
        # --------------------------------------------------------|
        #     000        |1 (TC)     | 1 (PUS hdr)       | apid   |
        # --------------------------------------------------------|
        assert apid > 2**11
        # first 3 bits (from left) are zero for space packets
        # move 1 to 13th place from right
        PUSTelecommand.__packet_id == 0b0001 << 12
        PUSTelecommand.__packet_id += apid
        PUSTelecommand.apid = apid

    def get_telecommand_id(self):
        return self.__tc_id

    def set_telecommand_id(self, tc_id):
        """Set TC ID. CCSDS Packet Sequence Control is set as TCID for PUS Telecommands.
        """
        assert tc_id > 0, "Telecommand ID should be greater than zero!"
        self.__tc_id = tc_id

    def get_type(self):
        assert self.__tc_type > 0
        return self.__tc_type

    def set_type(self, type_):
        assert type_ > 0
        self.__tc_type = type_

    def get_subtype(self):
        assert self.__tc_subtype > 0
        return self.__tc_subtype

    def set_subtype(self, subtype):
        assert subtype > 0
        self.__tc_subtype = subtype

    def get_source(self):
        return self.__tc_source

    def set_source(self, source):
        assert source > 0
        self.__tc_source = source

    def get_ack_level(self):
        return self.__ack_level

    def set_ack_level(self, level):
        """Set ACK level of the command.
        """
        assert level > 0
        self.__ack_level = level

    def is_acceptance_ack_required(self):
        return (self.__ack_level & PUSTelecommand.acceptance_ack) > 0

    def is_start_ack_required(self):
        return (self.__ack_level & PUSTelecommand.start_ack) > 0

    def is_progress_ack_required(self):
        return (self.__ack_level & PUSTelecommand.progress_ack) > 0

    def is_completion_ack_required(self):
        return (self.__ack_level & PUSTelecommand.completion_ack) > 0

    def is_object_configured(self):
        return super().is_object_configured() and self.__tc_type > 0 \
            and self.__tc_subtype > 0 \
                and self.__tc_source > 0 \
                    and self.__tc_id > 0 \
                        and PUSTelecommand.__packet_id > 0

    def get_user_data(self):
        """Get the user data field of the user data
        """
        raise NotImplementedError
    
    def get_bytes(self):
        """Default implementation for PUS TCs.
        Return bytes of the full packet.
        """
        assert self.is_object_configured(), "TC not configured"
        assert PUSTelecommand.__packet_id, "Set APID first"
        EIGHT_BITS = 0b11111111
        data = bytearray()

        # # packet id
        # get the msb 8 bits
        data.append(PUSTelecommand.__packet_id>>8)
        # get the last 8 bits
        data.append(PUSTelecommand.__packet_id&EIGHT_BITS)

        # # sequence control: corresponds to TC ID, 16 bits
        # get the msb 8 bits
        data.append(self.get_telecommand_id()>>8)
        # get the last 8 bits
        data.append(self.get_telecommand_id()&EIGHT_BITS)

        # # length of data in pkt: user data length + secondary hdr
        n_usr_bytes = self.get_number_of_bytes() + PUS_HEADER_TC_NBYTES
        data.append(n_usr_bytes>>8)
        data.append(n_usr_bytes&EIGHT_BITS)

        # # ack level
        data.append(self.get_ack_level())

        # service type
        print(f'type of command : {self.get_type()}')
        data.append(self.get_type())

        # service subtype
        data.append(self.get_subtype())

        # source id
        data.append(self.get_source()>>8)
        data.append(self.get_source()&EIGHT_BITS)

        # spare byte
        data.append(0)

        # # user data
        user_data = self.get_user_data()
        # add user data byte by byte
        for b in user_data:
            data.append(b)
        
        return data




