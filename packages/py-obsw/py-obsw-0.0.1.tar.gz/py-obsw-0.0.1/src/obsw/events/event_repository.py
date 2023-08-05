from obsw.base.root import RootObject
from obsw.events import Event
from collections import deque


class EventRepository(RootObject):
    def __init__(self):
        self.__global_enabled = False
        self._event_list = None
        self.__list_size = 0
        self.__clock = None

    def is_global_enabled(self):
        return self.__global_enabled

    def set_global_enable(self, status):
        self.__global_enabled = status

    def get_repository_size(self):
        return self.__list_size

    def set_repository_size(self, size):
        assert size > 0 and self.__list_size == 0
        self.__list_size = size
        self._create_repo_data_structure()

    def get_clock(self):
        return self.__clock

    def set_clock(self, clock):
        self.__clock = clock

    def _create_repo_data_structure(self):
        self._event_list = deque(maxlen=self.__list_size)

    def create(self, event_originator, event_type):
        assert self.is_object_configured() and event_originator is not None
        if not self.is_global_enabled():
            return
        event = Event()
        event.set_event_type(event_type)
        event.set_timestamp(self.__clock.get_time())
        self._event_list.append(event)

    def is_object_configured(self):
        return super().is_object_configured() and self.__clock is not None and self._event_list is not None
