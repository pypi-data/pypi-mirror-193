from enum import Enum


class InboundpaymentInboundPaymentRequestType(str, Enum):
    PI_BACS = "PI_BACS"
    PI_FP = "PI_FP"
    PI_DD = "PI_DD"
    PO_REV = "PO_REV"
    PI_FAST = "PI_FAST"
    INT_INTERC = "INT_INTERC"
    PI_CHAPS = "PI_CHAPS"
    PI_SECT = "PI_SECT"
    PI_SEPA_INST = "PI_SEPA_INST"

    def __str__(self) -> str:
        return str(self.value)
