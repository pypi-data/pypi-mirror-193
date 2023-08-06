from enum import Enum


class DirectdebitMandateStatus(str, Enum):
    PENDING = "PENDING"
    SUBMITTED = "SUBMITTED"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
