from enum import Enum


class AccountCreateCustomerRequestLegalEntity(str, Enum):
    GB = "GB"
    NL = "NL"
    IE = "IE"

    def __str__(self) -> str:
        return str(self.value)
