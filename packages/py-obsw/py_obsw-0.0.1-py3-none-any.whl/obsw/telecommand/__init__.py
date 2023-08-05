from obsw.base.punctual_action import PunctualAction


class Telecommand(PunctualAction):
    def __init__(self):
        super().__init__()
        self.__time_tag = -1
        self.__in_use = False

    def is_valid(self):
        assert self.is_object_configured(
        ), "Telecommand Object is not configured."
        return True

    def get_validity_check_code(self):
        return 0

    def can_execute(self):
        assert self.is_object_configured(
        ), "Telecommand Object is not configured."
        return True

    def get_execution_check_code(self):
        return 0

    def get_telecommand_id(self):
        return self.get_instance_id()

    def set_telecommand_id(self, tc_id):
        return

    def get_type(self):
        return self.get_class_id()

    def set_type(self, type_):
        return

    def get_subtype(self):
        return 0

    def set_subtype(self, subtype):
        return

    def get_source(self):
        return 0

    def set_source(self, source):
        return

    def get_time_tag(self):
        return self.__time_tag

    def set_time_tag(self, time_tag):
        self.__time_tag = time_tag

    def get_number_of_bytes(self):
        """Get number of bytes in user data
        """
        return 0

    def get_bytes(self):
        """Fetch the raw bytes of the TC.
        """
        assert self.is_object_configured(), "TC is not configured."
        raise NotImplementedError

    def set_raw_data_safe(self, index, byte):
        raise NotImplementedError

    def set_raw_data_fast(self, byte_array):
        """Set user data.
        """
        raise NotImplementedError

    def is_in_use(self):
        return self.__in_use

    def set_in_use(self, in_use):
        self.__in_use = in_use

    def get_ack_level(self):
        return 0

    def set_ack_level(self, level):
        return

    def is_object_configured(self):
        return super().is_object_configured() and self.__time_tag > 0
