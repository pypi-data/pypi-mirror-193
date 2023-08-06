from enum import Enum


class InboundpaymentMessageResponseCode(str, Enum):
    GENERAL = "GENERAL"
    BUSINESSRULE = "BUSINESSRULE"
    MFASTATUS = "MFASTATUS"
    MFAERROR = "MFAERROR"
    MFATIMEOUT = "MFATIMEOUT"
    MFADEVICEMM = "MFADEVICEMM"
    MFAMESSAGEINVALID = "MFAMESSAGEINVALID"
    NOTFOUND = "NOTFOUND"
    DUPLICATE = "DUPLICATE"
    INVALID = "INVALID"
    CONNECTION = "CONNECTION"
    RETRY = "RETRY"
    RATELIMIT = "RATELIMIT"
    PERMISSION = "PERMISSION"

    def __str__(self) -> str:
        return str(self.value)
