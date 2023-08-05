from obsw.base.root import RootObject
from obsw.definitions import ClassID
from obsw.telecommand.doof_pus_telecommand import DoofPUSTelecommand


class TelecommandFactory(RootObject):
    """Telecommand Factory is a singleton class.
    """
    __instance = None

    @classmethod
    def get_instance(cls, *args):
        print(f'isntance is {cls.__instance}')
        if cls.__instance is None:
            cls.__instance = TelecommandFactory()
        return cls.__instance

    def __init__(self):
        super().__init__()
        print(f'calling init.. tc fact')
        self.set_class_id(ClassID.ID_TELECOMMANDFACTORY.value)

        # Set DoofPUSTC size and initialize holder
        self._size_doof_pus_tc = 1
        self._pool_doof_pus_tc = [None] * self._size_doof_pus_tc

        # Set ModeChangePUSTC size and initialize holder
        self._size_mode_change_pus_tc = 1
        self._pool_mode_change_pus_tc = [None] * self._size_mode_change_pus_tc

    def set_doof_telecommand(self, idx, doof_tc):
        assert idx < self._size_doof_pus_tc, "Index out of range of max DoofTCs allowed."
        assert doof_tc is not None, "DoofTC cannot be of type None."
        self._pool_doof_pus_tc[idx] = doof_tc
        self._pool_doof_pus_tc[idx].set_in_use(False)

    def get_allocated_number_doof_telecommand(self):
        count = 0
        for tc in self._pool_doof_pus_tc:
            if tc.is_in_use():
                count += 1
        return count

    def get_max_doof_telecommand(self):
        return self._size_doof_pus_tc

    def allocate_doof_telecommand(self):
        assert self.is_object_configured(), "Object is not configured."
        for tc in self._pool_doof_pus_tc:
            if not tc.is_in_use():
                tc.set_in_use(True)
                return tc
        return None

    def is_free_doof_command(self):
        assert self.is_object_configured(), "Object is not configured."
        for tc in self._pool_doof_pus_tc:
            if not tc.is_in_use():
                return True
        return False

    def set_mode_change_telecommand(self, idx, mode_change_tc):
        assert idx < self._size_mode_change_pus_tc, "Index out of range of max ModeChangeTCs allowed."
        assert mode_change_tc is not None, "ModeChangeTC cannot be of type None."
        self._pool_mode_change_pus_tc[idx] = mode_change_tc
        self._pool_mode_change_pus_tc[idx].set_in_use(False)
        print(self._pool_mode_change_pus_tc)

    def get_allocated_number_mode_change_telecommand(self):
        count = 0
        for tc in self._pool_mode_change_pus_tc:
            if tc.is_in_use():
                count += 1
        return count

    def get_max_mode_change_telecommand(self):
        return self._size_mode_change_pus_tc

    def allocate_mode_change_telecommand(self):
        assert self.is_object_configured(), "Object is not configured."
        for tc in self._pool_mode_change_pus_tc:
            if not tc.is_in_use():
                tc.set_in_use(True)
                return tc
        return None

    def is_free_mode_change_command(self):
        assert self.is_object_configured(), "Object is not configured."
        for tc in self._pool_mode_change_pus_tc:
            if not tc.is_in_use():
                return True
        return False

    def is_object_configured(self):
        if not super().is_object_configured():
            return False

        for doof_tc in self._pool_doof_pus_tc:
            if doof_tc is None:
                return False

        for mode_change_tc in self._pool_mode_change_pus_tc:
            if mode_change_tc is None:
                return False
        
        return True
