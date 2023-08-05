from enum import Enum


class CardsimulatorMessageResponseCode(str, Enum):
    MFADEVICEMM = "MFADEVICEMM"
    MFAMESSAGEINVALID = "MFAMESSAGEINVALID"
    MFASTATUS = "MFASTATUS"
    CONNECTION = "CONNECTION"
    BUSINESSRULE = "BUSINESSRULE"
    MFATIMEOUT = "MFATIMEOUT"
    DUPLICATE = "DUPLICATE"
    RETRY = "RETRY"
    RATELIMIT = "RATELIMIT"
    MFAERROR = "MFAERROR"
    PERMISSION = "PERMISSION"
    GENERAL = "GENERAL"
    NOTFOUND = "NOTFOUND"
    INVALID = "INVALID"

    def __str__(self) -> str:
        return str(self.value)
