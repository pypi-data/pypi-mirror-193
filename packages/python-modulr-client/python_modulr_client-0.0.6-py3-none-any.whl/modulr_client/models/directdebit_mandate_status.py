from enum import Enum


class DirectdebitMandateStatus(str, Enum):
    SUSPENDED = "SUSPENDED"
    REJECTED = "REJECTED"
    PENDING = "PENDING"
    SUBMITTED = "SUBMITTED"
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
