import abc
from obsw.base.root import RootObject

class ITelecommandLoader(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def load(self):
        pass

    @abc.abstractmethod
    def release(self):
        pass


class TelecommandLoader(RootObject, ITelecommandLoader):
    def __init__(self):
        super().__init__()
        self.__tc_manager = None

    def get_tc_manager(self):
        return self.__tc_manager

    def set_tc_manager(self, tc_manager):
        self.__tc_manager = tc_manager

    def is_object_configured(self):
        return super().is_object_configured() and self.__tc_manager is not None

    def load(self):
        raise NotImplementedError

    def release(self):
        raise NotImplementedError