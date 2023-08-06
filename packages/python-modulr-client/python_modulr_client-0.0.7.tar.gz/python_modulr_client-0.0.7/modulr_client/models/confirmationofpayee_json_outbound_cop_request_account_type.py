from enum import Enum


class ConfirmationofpayeeJsonOutboundCopRequestAccountType(str, Enum):
    PERSONAL = "PERSONAL"
    BUSINESS = "BUSINESS"

    def __str__(self) -> str:
        return str(self.value)
