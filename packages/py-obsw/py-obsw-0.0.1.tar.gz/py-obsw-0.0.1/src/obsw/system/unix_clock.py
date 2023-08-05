import time
from obsw.system.clock import IObsClock

class UnixClock(IObsClock):
    def __init__(self):
        super().__init__()

    def get_time(self):
        return int(time.time())

    def sync_with_system_time(self):
        pass

    

    