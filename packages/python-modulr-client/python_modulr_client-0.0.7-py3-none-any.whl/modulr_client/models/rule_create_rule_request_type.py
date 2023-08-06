from enum import Enum


class RuleCreateRuleRequestType(str, Enum):
    SPLIT = "SPLIT"
    SWEEP = "SWEEP"
    FUNDING = "FUNDING"

    def __str__(self) -> str:
        return str(self.value)
