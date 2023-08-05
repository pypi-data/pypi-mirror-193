from obsw.events.event_repository import EventRepository


class PUSEventRepository(EventRepository):
    def __init__(self):
        super().__init__()
        self.__telemetry_manager = None

    def get_telemetry_manager(self):
        return self.__telemetry_manager

    def set_telemetry_manager(self, tm_manager):
        self.__telemetry_manager = tm_manager

    def create(self, event_originator, event_type):
        assert self.is_object_configured() and event_originator is not None
        if not self.is_global_enabled():
            return
        # this is a dummy implementation
        # TODO: Implement PUS TC Verification Service.
        print(f'created event of type {event_type}')
        
    def is_object_configured(self):
        return super().is_object_configured() and self.__telemetry_manager is not None

    
