import abc
from obsw.base.root import RootObject
from obsw.events import EventType


class IModalComponent(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def get_current_mode(self):
        pass

    @abc.abstractmethod
    def set_current_mode(self, mode_id):
        pass

    @abc.abstractmethod
    def set_default_mode(self, mode_id):
        pass


class BaseModalComponent(RootObject, IModalComponent):
    """Abstract Base class for components that have modes.
    Each component should expose functions that have associated IDs
    Each action can then be called by fetching its ID from a TC.
    """
    def __init__(self):
        # define mode data structure
        # instances of each mode is stored with its ID as key
        # the constructors of derived classes should initiate the state objects
        # and add them to this data structure
        self._modes = {}

        # actions need to be defined as key value pairs too
        # actions are references to public functions that can be
        # called by TCs
        self._actions = {}

        # current mode
        self._current_mode = None
        self._default_mode = None

    def get_current_mode(self):
        return self._current_mode

    def set_current_mode(self, mode_id):
        assert self.is_object_configured(), "Object is not configured yet."
        self._current_mode = self._modes[mode_id]

    def set_default_mode(self, mode_id):
        assert self.is_object_configured(), "Object is not configured yet."
        self._default_mode = self._modes[mode_id]

    def get_modes(self):
        assert self.is_object_configured(), "Object is not configured yet."
        return self._modes

    def get_mode(self, mode_id):
        assert self.is_object_configured(), "Object is not configured yet."
        return self._modes.get(mode_id)

    def get_action(self, action_id):
        assert self.is_object_configured(
        ), "Component is not configured. Set actions and modes."
        return self._actions[action_id]

    def is_object_configured(self):
        return super().is_object_configured() \
            and self._modes \
                    and self._actions is not None
