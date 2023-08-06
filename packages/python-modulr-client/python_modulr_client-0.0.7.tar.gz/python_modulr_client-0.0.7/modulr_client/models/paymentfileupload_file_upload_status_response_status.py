from enum import Enum


class PaymentfileuploadFileUploadStatusResponseStatus(str, Enum):
    SUBMITTED = "SUBMITTED"
    INVALID = "INVALID"
    VALID = "VALID"
    DUPLICATE = "DUPLICATE"
    REJECTED = "REJECTED"
    ACCEPTED = "ACCEPTED"
    PROCESSED = "PROCESSED"

    def __str__(self) -> str:
        return str(self.value)
