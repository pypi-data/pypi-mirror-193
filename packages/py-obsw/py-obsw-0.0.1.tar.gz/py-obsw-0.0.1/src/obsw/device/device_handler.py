from obsw.base.root import RootObject

class DeviceHandler(RootObject):
    def __init__(self):
        super().__init__()

    def switch_on(self, mode_based_component):
        pass

    def switch_off(self, mode_based_component):
        pass

    def switch_normal(self, mode_based_component):
        pass

    def switch_raw(self, mode_based_component):
        pass

    def switch_error(self, mode_based_component):
        pass