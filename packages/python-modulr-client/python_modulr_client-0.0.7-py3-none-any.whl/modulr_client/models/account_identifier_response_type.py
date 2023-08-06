from enum import Enum


class AccountIdentifierResponseType(str, Enum):
    SCAN = "SCAN"
    IBAN = "IBAN"
    DD = "DD"
    INTL = "INTL"

    def __str__(self) -> str:
        return str(self.value)
