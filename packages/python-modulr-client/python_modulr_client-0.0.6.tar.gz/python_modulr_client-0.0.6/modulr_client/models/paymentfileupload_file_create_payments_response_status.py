from enum import Enum


class PaymentfileuploadFileCreatePaymentsResponseStatus(str, Enum):
    ACCEPTED = "ACCEPTED"
    DUPLICATE = "DUPLICATE"
    PROCESSED = "PROCESSED"
    REJECTED = "REJECTED"
    SUBMITTED = "SUBMITTED"
    VALID = "VALID"
    INVALID = "INVALID"

    def __str__(self) -> str:
        return str(self.value)
