from enum import Enum


class DirectdebitCollectionScheduleResponseStatus(str, Enum):
    REJECTED = "REJECTED"
    PENDING = "PENDING"
    SUBMITTED = "SUBMITTED"
    ACTIVE = "ACTIVE"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
