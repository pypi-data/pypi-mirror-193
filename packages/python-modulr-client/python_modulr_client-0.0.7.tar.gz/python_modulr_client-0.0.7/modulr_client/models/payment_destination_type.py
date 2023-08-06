from enum import Enum


class PaymentDestinationType(str, Enum):
    BENEFICIARY = "BENEFICIARY"
    ACCOUNT = "ACCOUNT"
    SCAN = "SCAN"
    IBAN = "IBAN"

    def __str__(self) -> str:
        return str(self.value)
