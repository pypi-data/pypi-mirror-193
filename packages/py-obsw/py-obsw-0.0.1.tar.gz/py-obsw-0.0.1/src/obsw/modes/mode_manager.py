from obsw.base.root import RootObject


class ModeManager(RootObject):
    def __init__(self):
        super().__init__()
        self.enabled_status = []
        