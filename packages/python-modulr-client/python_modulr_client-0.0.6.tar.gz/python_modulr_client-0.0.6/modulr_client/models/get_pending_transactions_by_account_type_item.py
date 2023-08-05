from enum import Enum


class GetPendingTransactionsByAccountTypeItem(str, Enum):
    ADHOC = "ADHOC"
    FE_ACMNT = "FE_ACMNT"
    PI_BACS_CONTRA = "PI_BACS_CONTRA"
    PO_CHAPS = "PO_CHAPS"
    PO_MASTER = "PO_MASTER"
    PO_DD = "PO_DD"
    PI_SECT = "PI_SECT"
    PO_VISA = "PO_VISA"
    PI_VISA = "PI_VISA"
    PI_MASTER = "PI_MASTER"
    PO_REV = "PO_REV"
    PI_SWIFT = "PI_SWIFT"
    FE_REV = "FE_REV"
    PI_FAST_REV = "PI_FAST_REV"
    PO_SWIFT = "PO_SWIFT"
    PI_SEPA_INST = "PI_SEPA_INST"
    INT_INTRAC = "INT_INTRAC"
    FE_TXN = "FE_TXN"
    PO_REV_MASTER = "PO_REV_MASTER"
    PI_REV = "PI_REV"
    PO_FAST = "PO_FAST"
    FE_ACOPN = "FE_ACOPN"
    PI_FAST = "PI_FAST"
    PI_DD = "PI_DD"
    PO_SEPA_INST = "PO_SEPA_INST"
    INT_INTERC = "INT_INTERC"
    PI_BACS = "PI_BACS"
    PI_CHAPS = "PI_CHAPS"
    PO_SECT = "PO_SECT"

    def __str__(self) -> str:
        return str(self.value)
