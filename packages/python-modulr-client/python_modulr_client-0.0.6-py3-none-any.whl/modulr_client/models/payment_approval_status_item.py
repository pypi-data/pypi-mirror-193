from enum import Enum


class PaymentApprovalStatusItem(str, Enum):
    NOTNEEDED = "NOTNEEDED"
    APPROVED = "APPROVED"
    REJECTED = "REJECTED"
    PENDING = "PENDING"
    DELETED = "DELETED"

    def __str__(self) -> str:
        return str(self.value)
