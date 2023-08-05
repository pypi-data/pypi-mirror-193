from enum import Enum


class AccountAccessGroupWithDetailsResponseType(str, Enum):
    USER_DEFINED = "USER_DEFINED"
    DELEGATE = "DELEGATE"
    SERVICE_CUSTOMER = "SERVICE_CUSTOMER"
    SERVICE_PARTNER = "SERVICE_PARTNER"

    def __str__(self) -> str:
        return str(self.value)
