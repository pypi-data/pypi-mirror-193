from enum import Enum


class PaymentPaymentResponseApprovalStatus(str, Enum):
    NOTNEEDED = "NOTNEEDED"
    PENDING = "PENDING"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
