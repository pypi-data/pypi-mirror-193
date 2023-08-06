from enum import Enum


class AccountAccessGroupWithDetailsResponseType(str, Enum):
    SERVICE_PARTNER = "SERVICE_PARTNER"
    SERVICE_CUSTOMER = "SERVICE_CUSTOMER"
    DELEGATE = "DELEGATE"
    USER_DEFINED = "USER_DEFINED"

    def __str__(self) -> str:
        return str(self.value)
