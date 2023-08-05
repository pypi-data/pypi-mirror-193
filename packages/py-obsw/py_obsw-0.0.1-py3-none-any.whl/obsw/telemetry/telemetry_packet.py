from obsw.base.root import RootObject
import abc


class ITelemetryPacket(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def update(self):
        pass

    @abc.abstractmethod
    def get_bytes(self):
        pass

    @abc.abstractmethod
    def get_byte(self, n):
        pass

    @abc.abstractmethod
    def serialize(self):
        pass

    @abc.abstractmethod
    def is_valid(self):
        pass


class TelemetryPacket(RootObject, ITelemetryPacket):
    __obs_clock = None

    def __init__(self):
        super().__init__()
        self.__in_use = False
        self.__type = 0
        self.__subtype = 0
        self.__destination = 0
        self.__time_tag = -1

    @staticmethod
    def get_obs_clock():
        assert TelemetryPacket.__obs_clock is not None
        return TelemetryPacket.__obs_clock

    @staticmethod
    def set_obs_clock(obs_clock):
        assert obs_clock is not None
        TelemetryPacket.__obs_clock = obs_clock

    def get_in_use(self):
        return self.__in_use

    def set_in_use(self, in_use):
        self.__in_use = in_use

    def get_type(self):
        return self.__type

    def set_type(self, tm_type):
        assert tm_type > 0
        self.__type = tm_type

    def get_subtype(self):
        return self.__subtype

    def set_subtype(self, tm_subtype):
        assert tm_subtype > 0
        self.__subtype = tm_subtype

    def get_destination(self):
        return self.__destination

    def set_destination(self, destination):
        assert destination > 0
        self.__destination = destination

    def get_time_tag(self):
        return self.__time_tag

    def set_time_tag(self, time_tag):
        assert time_tag > 0
        self.__time_tag = time_tag

    def get_number_of_bytes(self):
        pass

    def update(self):
        pass

    def get_bytes(self):
        pass

    def get_byte(self, n):
        pass

    def serialize(self):
        pass

    def is_valid(self):
        pass        
