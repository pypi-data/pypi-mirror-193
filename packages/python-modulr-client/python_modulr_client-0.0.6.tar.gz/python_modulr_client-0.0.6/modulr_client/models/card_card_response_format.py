from enum import Enum


class CardCardResponseFormat(str, Enum):
    VIRTUAL = "VIRTUAL"
    PHYSICAL = "PHYSICAL"

    def __str__(self) -> str:
        return str(self.value)
