from obsw.base.root import RootObject
from obsw.definitions import ClassID

class TelemetryManager(RootObject):
    def __init__(self):
        super().__init__()
        self.__tm_list = []

    
