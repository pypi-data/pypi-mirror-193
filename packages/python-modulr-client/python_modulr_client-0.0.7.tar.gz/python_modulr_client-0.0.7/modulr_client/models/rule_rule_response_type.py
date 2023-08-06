from enum import Enum


class RuleRuleResponseType(str, Enum):
    SPLIT = "SPLIT"
    SWEEP = "SWEEP"
    FUNDING = "FUNDING"

    def __str__(self) -> str:
        return str(self.value)
