import abc
from obsw.base.root import RootObject


class ITelemetryStream(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def reset(self):
        pass

    @abc.abstractmethod
    def flush(self):
        pass

    @abc.abstractmethod
    def get_capacity(self):
        pass

    @abc.abstractmethod
    def does_packet_fit(self, tm_packet):
        pass

    @abc.abstractmethod
    def write(self, tm_packet):
        pass


class TelemetryStream(RootObject, ITelemetryStream):
    def __init__(self):
        super().__init__()

    def reset(self):
        pass

    def flush(self):
        pass

    def get_capacity(self):
        pass

    def does_packet_fit(self, tm_packet):
        pass

    def write(self, tm_packet):
        pass