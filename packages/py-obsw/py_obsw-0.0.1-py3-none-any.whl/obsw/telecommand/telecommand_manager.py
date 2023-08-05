"""This module implements a TelecommandManager following the Manager Pattern.

A Telecommand Manager manages the lifetime of a command after it is loaded
by a TelecommandLoader.
"""
from obsw.base.root import RootObject
from obsw.definitions import ClassID
from obsw.events import EventType
from obsw.base.punctual_action import ActionOutcome


class TelecommandManager(RootObject):
    def __init__(self):
        super().__init__()
        self.__tc_list = []  # list of TCs (has None or NULL PTR of max size)
        self.__pending_tc_counter = 0  # number of pending TCs
        self.__pending_tc_max_size = 0  # max size of pending TCs
        self.__tc_loader = None
        self.__clock = None
        self.set_class_id(ClassID.ID_TELECOMMANDMANAGER.value)

    def reset(self):
        """Abort all pending TCs, and brings the TCManager to 
        initial state.
        """
        assert self.__tc_list, "TC list not initialized"
        for i in range(len(self.__tc_list)):
            if self.__tc_list[i]:
                RootObject.get_event_repository().create(
                    self.__tc_list[i], EventType.EVT_TC_ABORTED.value)
                self.__tc_loader.release(self.__tc_list[i])
                self.__tc_list[i] = None
        self.__pending_tc_counter = 0

    def get_max_pending_command_size(self):
        assert self.__pending_tc_max_size
        return self.__pending_tc_max_size

    def set_max_pending_command_size(self, max_size):
        """Set the size of maximum number of pending TCs.
        To be called only once after instantiation.
        """
        assert self.__pending_tc_max_size == 0, "This method should be called only once."
        assert max_size > 0, "Max size cannot be zero or negative."
        self.__pending_tc_max_size = max_size
        self.__tc_list = [None] * max_size

    def load(self, tc):
        assert self.is_object_configured(), "Configure object first."
        assert tc is not None, "Cannot load None."
        # if TC is invalid, reject TC and create event for invalid TC
        if not tc.is_valid():
            RootObject.get_event_repository().create(
                tc, EventType.EVT_TC_NOT_VALID.value)
            self.__tc_loader.release(tc)
            return

        # Check whether max no. of TCs have been loaded.
        # Reject if full and create event
        if self.__pending_tc_counter == self.__pending_tc_max_size:
            RootObject.get_event_repository().create(
                tc, EventType.EVT_TC_LIST_FULL.value)
            self.__tc_loader.release(tc)
            return
        
        # Insert TC into first empty slot
        for i in range(self.__pending_tc_max_size):
            if self.__tc_list[i] is None:
                self.__tc_list[i] = tc
                self.__pending_tc_counter += 1
                return
        
        assert False, "Check code implementation."

    def get_pending_telecommands_counter(self):
        assert self.is_object_configured(), "Object is not configured."
        return self.__pending_tc_counter

    def get_pending_telecommand(self, index):
        assert self.is_object_configured(), "Object is not configured."
        assert i < self.__pending_tc_max_size, "Index out of range. Max TC list size exceeded."
        return self.__tc_list[index]

    def abort(self, tc):
        """Abort a TC object.
        Check if TC in pending list. 
        If yes, release its resources and remove it from list
        """
        assert self.is_object_configured(), "Object is not configured."
        assert tc is not None, "TC cannot be None."
        if tc in self.__tc_list:
            # create an envent for TC Abort
            RootObject.get_event_repository().create(tc, EventType.EVT_TC_ABORTED.value)

            # release resources taken up by TC
            self.__tc_loader.release(tc)

            # replace the TC by NULL Pointer
            self.__tc_list[self.__tc_list.index(tc)] = None
            self.__pending_tc_counter -= 1
            return
        return
    
    def abort_by_id(self, tc_id):
        """Abort a TC by its id.
        """
        assert self.is_object_configured(), "Object is not configured."
        assert tc_id > 0, "TC ID is invalid, cannot <=0."
        for idx in range(len(self.__tc_list)):
            if self.__tc_list[idx].get_telecommand_id() == tc_id:
                # create an envent for TC Abort
                RootObject.get_event_repository().create(self.__tc_list[idx], EventType.EVT_TC_ABORTED.value)

                # release resources taken up by TC
                self.__tc_loader.release(self.__tc_list[idx])

                # replace the TC by NULL Pointer
                self.__tc_list[idx] = None
                self.__pending_tc_counter -= 1
                return
        return

    def get_tc_loader(self):
        assert self.__tc_loader is not None, "TC Loader has not been set yet."
        return self.__tc_loader

    def set_tc_loader(self, tc_loader):
        assert tc_loader is not None, "TC Loader cannot be None"
        self.__tc_loader = tc_loader

    def get_clock(self):
        assert self.__clock is not None, "Clock not set yet."
        return self.__clock

    def set_clock(self, clock):
        assert clock is not None, "Clock cannot be None."
        self.__clock = clock

    def execute(self):
        """Execute TCs that are due execution and can be executed.
        """
        assert self.is_object_configured(), "TC Manager is not configured."
        outcome = None
        for tc in self.__tc_list:
            if tc is not None and tc.get_time_tag() <= self.__clock.get_time():
                if tc.can_execute():
                    outcome = tc.execute()
                    if outcome != ActionOutcome.ACTION_SUCCESS.value:
                        RootObject.get_event_repository().create(tc, EventType.EVT_TC_EXEC_FAIL.value)
                    else:
                        RootObject.get_event_repository().create(tc, EventType.EVT_TC_EXEC_SUCC.value)
                else:
                    RootObject.get_event_repository().create(tc, EventType.EVT_TC_EXEC_CHECK_FAIL.value)
                self.__tc_loader.release(tc)
                self.__tc_list[self.__tc_list.index(tc)] = None
                self.__pending_tc_counter -= 1
        return

    def is_object_configured(self):
        return super().is_object_configured() \
            and self.__tc_loader is not None\
                 and self.__clock is not None\
                      and self.__pending_tc_max_size!=0







    

    

