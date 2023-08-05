import abc
import enum


class BasicActions(enum.Enum):
    SWITCH_OFF = 0
    SWITCH_ON = 1
    SWITCH_NORMAL = 2
    SWITCH_RAW = 3
    SWITCH_ERROR = 4

class BasicModeTypes(enum.Enum):
    OFF = 0
    ON = 1
    NORMAL = 2
    RAW = 3
    ERROR = 4


class IBasicDeviceMode(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def switch_on(self, mode_based_component):
        pass

    @abc.abstractmethod
    def switch_off(self, mode_based_component):
        pass

    @abc.abstractmethod
    def switch_normal(self, mode_based_component):
        pass

    @abc.abstractmethod
    def switch_raw(self, mode_based_component):
        pass

    @abc.abstractmethod
    def switch_error(self, mode_based_component):
        pass


class BasicDeviceMode(IBasicDeviceMode):
    def __init__(self, type_):
        self.__type = type_
    
    def get_type(self):
        return self.__type

    def switch_on(self, mode_based_component):
        pass

    def switch_off(self, mode_based_component):
        pass

    def switch_normal(self, mode_based_component):
        pass

    def switch_raw(self, mode_based_component):
        pass

    def switch_error(self, mode_based_component):
        pass