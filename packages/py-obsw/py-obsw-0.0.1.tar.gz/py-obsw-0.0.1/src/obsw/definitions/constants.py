# PUS Service Type for TC Verification Report
# -------------------------------------------

PUS_TYPE_TC_VER = 1
# PUS Service 1, Subtype for TC Acceptance Report Success
PUS_SUBTYPE_TC_VER_ACC_SC = 1
# PUS Service 1, Subtype for TC Acceptance Report Failure
PUS_SUBTYPE_TC_VER_ACC_FL = 2
# PUS Service 1, Subtype for TC Execution Start Report Success
PUS_SUBTYPE_TC_VER_EXE_STR_SC = 3
# PUS Service 1, Subtype for TC Execution Start Report Failure
PUS_SUBTYPE_TC_VER_EXE_STR_FL = 4
# PUS Service 1, Subtype for TC Execution Progress Report Success
PUS_SUBTYPE_TC_VER_EXE_PRO_SC = 5
# PUS Service 1, Subtype for TC Execution Progress Report Failure
PUS_SUBTYPE_TC_VER_EXE_PRO_FL = 6
# PUS Service 1, Subtype for TC Execution End Report Success
PUS_SUBTYPE_TC_VER_EXE_END_SC = 7
# PUS Service 1, Subtype for TC Execution End Report Failure
PUS_SUBTYPE_TC_VER_EXE_END_FL = 8


# PUS Service Type for Dummy Service
# ----------------------------------

PUS_TYPE_DOOF = 200
# PUS TC Subservice to send zero as payload
PUS_SUBTYPE_DOOF_SEND_ZERO = 1
# PUS TC Subservice to incremenet a counter
PUS_SUBTYPE_DOOF_INCREMENT = 2



# PUS Service Type for Mode Control
# ---------------------------------

PUS_TYPE_MOD_CTRL = 201
# PUS Service 201, Subservice 1, TC service to set mode
PUS_SUBTYPE_MOD_CTRL_SM = 1
# PUS Service 201, Subservice 2, TC service to get mode
PUS_SUBTYPE_MOD_CTRL_GM = 2


# PUS HEADER SIZE CONSTANTS
# -------------------------

# PUS TC HEADER SIZE IN BYTES
PUS_HEADER_TC_NBYTES = 6
# PUS TC ACK SIZE IN BYTES 
PUS_HEADER_TC_ACK_NBYTES = 1
# PUS HEADER TC SERVICE TYPE SIZE IN BYTES
PUS_HEADER_TC_SERVICE_NBYTES = 1
# PUS HEADER TC SUBSERVICE TYPE SIZE IN BYTES
PUS_HEADER_TC_SUBSERVICE_NBYTES = 1
# PUS HEADER TC SOURCE ID SIZE IN BYTES
PUS_HEADER_TC_SRC_ID_NBYTES = 2
# PUS HEADER TC SPARE BYTE (To make integral number of words: 1 word = 2Bytes)
PUS_HEADER_TC_SPARE_NBYTES = 1


# CCSDS PRIMARY HEADER SIZE CONSTANTS
# -----------------------------------
# CCSDS PKT PRIMARY HEADER BYTES
CCSDS_PKT_PRM_HDR_NBYTES = 6
# CCSDS PKT ID (PKT VERSION NO. + PACKET ID) SIZE
CCSDS_PKT_ID_NBYTES = 2
# CCSDS PKT SEQUENCE CTRL NUMBER OF BYTES
CCSDS_PKT_SQ_CTRL_NBYTES = 2
# CCSDS PKT DATA LENGTH DECLARATION NUMBER OF BYTES
CCSDS_PKT_DATA_LENGTH_DEFINE_NBYTES = 2


# TC EXECUTION
# ------------
TC_CAN_EXECUTE = True
TC_CANNOT_EXECUTE = False