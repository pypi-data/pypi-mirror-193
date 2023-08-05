from obsw.telecommand.pus_telecommand import PUSTelecommand
from obsw.base.punctual_action import ActionOutcome
from obsw.definitions import ClassID
from obsw.definitions.constants import *

class DoofPUSTelecommand(PUSTelecommand):
    def __init__(self):
        super().__init__()
        self.__execution_counter = 0
        self.set_ack_level(0b00100001) # ack level byte contains pus version
        self.set_telecommand_id(ClassID.ID_DOOF_PUS_COMMAND.value)
        self.set_type(PUS_TYPE_DOOF)
        self.set_subtype(PUS_SUBTYPE_DOOF_INCREMENT)

    def get_execution_counter(self):
        return self.__execution_counter

    def get_number_of_bytes(self):
        return 1

    def get_user_data(self):
        return bytearray([self.__execution_counter])

    def set_raw_data_fast(self, byte_array):
        pass

    def _do_action(self):
        self.__execution_counter += 1
        print(f'execution counter is {self.__execution_counter}')
        return ActionOutcome.ACTION_SUCCESS.value

    def is_object_configured(self):
        return super().is_object_configured()
        
        

    
