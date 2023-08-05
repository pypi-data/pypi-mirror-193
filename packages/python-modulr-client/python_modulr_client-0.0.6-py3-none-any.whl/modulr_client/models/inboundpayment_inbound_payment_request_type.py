from enum import Enum


class InboundpaymentInboundPaymentRequestType(str, Enum):
    PI_DD = "PI_DD"
    PO_REV = "PO_REV"
    PI_FP = "PI_FP"
    INT_INTERC = "INT_INTERC"
    PI_SECT = "PI_SECT"
    PI_BACS = "PI_BACS"
    PI_CHAPS = "PI_CHAPS"
    PI_FAST = "PI_FAST"
    PI_SEPA_INST = "PI_SEPA_INST"

    def __str__(self) -> str:
        return str(self.value)
