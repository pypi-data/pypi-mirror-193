from enum import Enum


class GetCustomersNameType(str, Enum):
    WORD_MATCH = "WORD_MATCH"
    WORD_MATCH_ALPHANUMERIC = "WORD_MATCH_ALPHANUMERIC"
    PREFIX = "PREFIX"
    SUFFIX = "SUFFIX"
    CONTAINS = "CONTAINS"
    EXACT = "EXACT"

    def __str__(self) -> str:
        return str(self.value)
