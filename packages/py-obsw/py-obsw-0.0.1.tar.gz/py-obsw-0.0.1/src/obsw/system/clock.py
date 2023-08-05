from obsw.base.root import RootObject
import abc

class IObsClock(RootObject, metaclass=abc.ABCMeta):
    def __init__(self):
        super().__init__()

    @abc.abstractmethod
    def get_time(self):
        pass

    @abc.abstractmethod
    def sync_with_system_time(self):
        pass
