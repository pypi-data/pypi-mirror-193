from enum import Enum


class GetCreatePhysicalCardAsyncTasksByAccountStatuses(str, Enum):
    RUNNING = "RUNNING"
    RECEIVED = "RECEIVED"
    ERROR = "ERROR"
    COMPLETE = "COMPLETE"

    def __str__(self) -> str:
        return str(self.value)
