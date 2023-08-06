from enum import Enum


class CardAsyncTaskResponseStatus(str, Enum):
    RECEIVED = "RECEIVED"
    RUNNING = "RUNNING"
    COMPLETE = "COMPLETE"
    ERROR = "ERROR"

    def __str__(self) -> str:
        return str(self.value)
