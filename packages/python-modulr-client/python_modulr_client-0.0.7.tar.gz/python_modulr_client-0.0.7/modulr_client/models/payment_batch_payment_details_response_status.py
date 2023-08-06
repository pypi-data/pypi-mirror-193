from enum import Enum


class PaymentBatchPaymentDetailsResponseStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    REJECTED = "REJECTED"
    SUBMITTED = "SUBMITTED"
    CANCELLED = "CANCELLED"

    def __str__(self) -> str:
        return str(self.value)
