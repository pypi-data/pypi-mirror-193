from enum import Enum


class InboundpaymentAccountIdentifierDetailRequestType(str, Enum):
    IBAN = "IBAN"
    DD = "DD"
    SCAN = "SCAN"
    INTL = "INTL"

    def __str__(self) -> str:
        return str(self.value)
