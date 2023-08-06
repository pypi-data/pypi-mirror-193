from enum import Enum


class InboundpaymentAccountIdentifierDetailRequestType(str, Enum):
    SCAN = "SCAN"
    IBAN = "IBAN"
    DD = "DD"
    INTL = "INTL"

    def __str__(self) -> str:
        return str(self.value)
