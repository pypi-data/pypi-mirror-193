from enum import Enum


class DirectdebitCollectionScheduleResponseStatus(str, Enum):
    ACTIVE = "ACTIVE"
    PENDING = "PENDING"
    SUBMITTED = "SUBMITTED"
    REJECTED = "REJECTED"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
