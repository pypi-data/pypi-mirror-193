from obsw.modes.device_modes import BasicDeviceMode, BasicModeTypes


class ErrorMode(BasicDeviceMode):
    def __init__(self):
        super().__init__(BasicModeTypes.ERROR.value)

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
