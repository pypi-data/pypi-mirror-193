from enum import Enum


class AccountIdentifierRequestType(str, Enum):
    IBAN = "IBAN"
    DD = "DD"
    SCAN = "SCAN"
    INTL = "INTL"

    def __str__(self) -> str:
        return str(self.value)
