from enum import Enum


class PaymentChargeBearer(str, Enum):
    SHAR = "SHAR"
    CRED = "CRED"
    DEBT = "DEBT"

    def __str__(self) -> str:
        return str(self.value)
