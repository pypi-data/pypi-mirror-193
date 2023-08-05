import abc
import enum
from obsw.base.root import RootObject
from obsw.events import EventType


class ActionOutcome(enum.Enum):
    ACTION_DISABLED = 1
    ACTION_SUCCESS = 2
    ACTION_FAILURE = 3
    ACTION_CANNOT_EXECUTE = 4
    ACTION_RESET = 5
    MEM_LOAD_PRE_CHECKSUM_FAILED = 6
    MEM_LOAD_POST_CHECKSUM_FAILED = 7
    PACKET_NOT_FOUND = 8
    PUS_MODE_MAN_FULL = 9
    APP_DATA_INCONSISTENT = 10
    TM_MAN_QUEUE_FULL = 11
    LAST_ACTION_OUTCOME = 12


class IPunctualAction(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def _do_action(self):
        pass


class PunctualAction(IPunctualAction, RootObject):
    def __init__(self):
        super().__init__()
        self.enabled_status = True
        self.last_outcome = ActionOutcome.ACTION_RESET.value

    def is_enabled(self):
        return self.enabled_status

    def set_enabled(self, enabled_status):
        self.enabled_status = enabled_status

    def get_last_outcome(self):
        return self.last_outcome

    def reset_last_outcome(self):
        self.last_outcome = ActionOutcome.ACTION_RESET.value

    def execute(self):
        outcome = ActionOutcome.ACTION_DISABLED.value
        if self.enabled_status:
            outcome = self._do_action()
            RootObject.get_event_repository().create(
                self, EventType.PUNCTUAL_ACTION_EXEC.value)
        else:
            RootObject.get_event_repository().create(
                self, EventType.PUNCTUAL_ACTION_DIS.value)
        self.last_outcome = outcome
        return outcome

    def _do_action(self):
        pass