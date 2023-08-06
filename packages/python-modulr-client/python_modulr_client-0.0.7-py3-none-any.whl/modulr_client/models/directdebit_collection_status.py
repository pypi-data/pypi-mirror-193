from enum import Enum


class DirectdebitCollectionStatus(str, Enum):
    SUCCESS = "SUCCESS"
    FAILED = "FAILED"
    PROCESSING = "PROCESSING"
    SCHEDULED = "SCHEDULED"
    REPRESENTABLE = "REPRESENTABLE"
    REPRESENTED = "REPRESENTED"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
