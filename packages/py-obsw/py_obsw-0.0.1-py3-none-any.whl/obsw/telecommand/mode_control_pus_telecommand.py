from turtle import mode
from obsw.telecommand.pus_telecommand import PUSTelecommand
from obsw.definitions import ClassID
from obsw.definitions.constants import *


class ModeControlPUSTelecommand(PUSTelecommand):
    """PUS TC for changing mode
    """

    def __init__(self):
        super().__init__()
        self.set_ack_level(0b00100001)  # ack level byte contains pus version
        self.set_telecommand_id(ClassID.ID_MOD_CTRL_PUS_COMMAND.value)
        self.set_type(PUS_TYPE_MOD_CTRL)
        self.set_subtype(PUS_SUBTYPE_MOD_CTRL_SM)
        self.modal_component = None
        self.user_data = None

    def set_modal_component(self, modal_component):
        self.modal_component = modal_component

    def _do_action(self):
        """Action to be performed by the command.
        This telecommand changes the mode of its plugin component.
        """
        raise NotImplementedError

    def get_user_data(self):
        """Get the user data field of the user data
        """
        assert (
            self.is_object_configured()
        ), "User data is not available. Call set raw data first."
        return self.user_data
    
    def get_number_of_bytes(self):
        return 2

    def set_raw_data_fast(self, byte_array):
        """Set user data.
        """
        assert len(byte_array) == 2, "Exactly 2 bytes of user data are allowed."
        self.user_data = byte_array

    def is_object_configured(self):
        return (
            super().is_object_configured()
            and self.modal_component is not None
            and self.user_data is not None
        )

