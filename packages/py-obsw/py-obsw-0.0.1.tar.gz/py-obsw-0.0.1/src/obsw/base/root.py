from obsw.definitions import ClassID


class RootObject:
    instance_counter = 0
    system_list = []
    system_list_size = 0
    data_pool = None
    parameter_db = None
    event_repository = None
    tracer = None

    def __init__(self):
        assert RootObject.system_list_size != 0, "System list is not initialized. Call set_system_list_size."
        assert RootObject.system_list, "System list is not initialized. Call set_system_list_size."
        assert RootObject.instance_counter < RootObject.system_list_size
        self.__instance_id = RootObject.instance_counter
        self.__class_id = None
        self.set_class_id(ClassID.ID_ROOT_OBJECT.value)
        RootObject.instance_counter += 1
        RootObject.system_list.append(self)

    @staticmethod
    def get_system_list_size():
        return RootObject.system_list_size

    @staticmethod
    def set_system_list_size(size):
        RootObject.system_list_size = size
        RootObject.system_list = [None] * size

    @staticmethod
    def get_data_pool():
        return RootObject.data_pool

    @staticmethod
    def set_data_pool(datapool):
        RootObject.data_pool = datapool

    @staticmethod
    def get_parameter_db():
        return RootObject.parameter_db

    @staticmethod
    def set_parameter_db(parameter_db):
        RootObject.parameter_db = parameter_db

    @staticmethod
    def get_event_repository():
        return RootObject.event_repository  

    @staticmethod
    def set_event_repository(evt_repo):
        RootObject.event_repository = evt_repo

    @staticmethod
    def get_tracer():
        return RootObject.tracer

    @staticmethod
    def set_tracer(tracer):
        RootObject.tracer = tracer

    @staticmethod
    def is_system_configured():
        return all([o.is_object_configured() for o in RootObject.system_list if o is not None])

    def get_class_id(self):
        return self.class_id

    def set_class_id(self, value):
        assert isinstance(value, int)
        self.__class_id = value

    def get_instance_id(self):
        return self.__instance_id

    def is_object_configured(self):
        # TODO: add: and RootObject.tracer is not None
        # tracer class not implemented yet.
        return RootObject.data_pool is not None \
             and RootObject.parameter_db is not None \
                 and RootObject.event_repository is not None