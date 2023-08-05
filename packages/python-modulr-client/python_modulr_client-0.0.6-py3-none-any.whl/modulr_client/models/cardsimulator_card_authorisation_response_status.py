from enum import Enum


class CardsimulatorCardAuthorisationResponseStatus(str, Enum):
    REVERSED = "REVERSED"
    APPROVED = "APPROVED"
    SETTLED = "SETTLED"

    def __str__(self) -> str:
        return str(self.value)
