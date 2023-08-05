from enum import Enum


class PaymentBatchPaymentStatusesItem(str, Enum):
    SUBMITTED = "SUBMITTED"
    REJECTED = "REJECTED"
    ACCEPTED = "ACCEPTED"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
