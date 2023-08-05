import enum

class EventType(enum.Enum):
    NULL = 0
    PUNCTUAL_ACTION_EXEC = 1
    PUNCTUAL_ACTION_DIS = 2

    # TC Events
    EVT_TC_NOT_VALID = 8
    EVT_TC_LOADED = 9
    EVT_TC_EXEC_SUCC = 10
    EVT_TC_ABORTED = 11
    EVT_TC_LIST_FULL = 12
    EVT_TC_EXEC_CHECK_FAIL = 13
    EVT_TC_EXEC_FAIL = 14
    EVT_TC_NOT_AVAIL = 56
    EVT_TC_UNKNOWN_TYPE = 57
    EVT_TC_TOO_LONG =  58
    EVT_TOO_MANY_TC_PKT = 59
    EVT_TM_STREAM_END = 60

    # Mode Transition Events
    MODE_TRANS_INHIBITED = 16
    MODE_TRANS_PERFORMED = 17



class Event:
    def __init__(self):
        self.__timestamp = None
        self.__event_type = None

    def get_timestamp(self):
        return self.__timestamp

    def set_timestamp(self, timestamp):
        assert isinstance(timestamp, int)

    def get_event_type(self):
        return self.__event_type

    def set_event_type(self, event_type):
        self.__event_type = event_type
