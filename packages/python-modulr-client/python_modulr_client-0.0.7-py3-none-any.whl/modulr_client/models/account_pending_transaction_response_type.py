from enum import Enum


class AccountPendingTransactionResponseType(str, Enum):
    PI_BACS = "PI_BACS"
    PI_BACS_CONTRA = "PI_BACS_CONTRA"
    PI_FAST = "PI_FAST"
    PI_CHAPS = "PI_CHAPS"
    PI_DD = "PI_DD"
    PI_SECT = "PI_SECT"
    PI_SEPA_INST = "PI_SEPA_INST"
    PI_REV = "PI_REV"
    PI_FAST_REV = "PI_FAST_REV"
    PO_FAST = "PO_FAST"
    PO_CHAPS = "PO_CHAPS"
    PO_DD = "PO_DD"
    PO_SECT = "PO_SECT"
    PO_SEPA_INST = "PO_SEPA_INST"
    PO_REV = "PO_REV"
    INT_INTERC = "INT_INTERC"
    INT_INTRAC = "INT_INTRAC"
    ADHOC = "ADHOC"
    FE_TXN = "FE_TXN"
    FE_ACMNT = "FE_ACMNT"
    FE_ACOPN = "FE_ACOPN"
    FE_REV = "FE_REV"
    PO_MASTER = "PO_MASTER"
    PI_MASTER = "PI_MASTER"
    PO_REV_MASTER = "PO_REV_MASTER"
    PO_VISA = "PO_VISA"
    PI_VISA = "PI_VISA"
    PI_SWIFT = "PI_SWIFT"
    PO_SWIFT = "PO_SWIFT"

    def __str__(self) -> str:
        return str(self.value)
