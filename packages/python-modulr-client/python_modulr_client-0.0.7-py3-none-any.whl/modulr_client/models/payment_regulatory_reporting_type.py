from enum import Enum


class PaymentRegulatoryReportingType(str, Enum):
    CRED = "CRED"
    DEBT = "DEBT"
    BOTH = "BOTH"

    def __str__(self) -> str:
        return str(self.value)
