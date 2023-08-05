from enum import Enum


class DirectdebitCollectionStatus(str, Enum):
    SUCCESS = "SUCCESS"
    PROCESSING = "PROCESSING"
    REPRESENTABLE = "REPRESENTABLE"
    CANCELLED = "CANCELLED"
    FAILED = "FAILED"
    SCHEDULED = "SCHEDULED"
    REPRESENTED = "REPRESENTED"

    def __str__(self) -> str:
        return str(self.value)
