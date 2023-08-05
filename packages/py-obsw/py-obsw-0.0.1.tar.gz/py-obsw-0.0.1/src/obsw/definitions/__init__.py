import enum


class ClassID(enum.Enum):
    ID_ROOT_OBJECT = 1
    ID_EVENT = 2

    # Telecommand Manager
    ID_TELECOMMANDMANAGER = 82

    # PUS Telemetry
    ID_PUS_TC_VERIFICATION_PACKET = 203

    # Telecommand Factory
    ID_TELECOMMANDFACTORY = 251

    # PUS Telecommands
    ID_DOOF_PUS_COMMAND = 84
    ID_MOD_CTRL_PUS_COMMAND = 85

    # PUS TM Stream
    ID_PUS_TELEMETRY_STREAM = 270
