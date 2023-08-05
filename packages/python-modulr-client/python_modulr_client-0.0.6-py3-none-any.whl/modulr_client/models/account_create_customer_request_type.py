from enum import Enum


class AccountCreateCustomerRequestType(str, Enum):
    LLC = "LLC"
    INDIVIDUAL = "INDIVIDUAL"
    TRUST = "TRUST"
    OPARTNRSHP = "OPARTNRSHP"
    PCM_BUSINESS = "PCM_BUSINESS"
    SOLETRADER = "SOLETRADER"
    PCM_INDIVIDUAL = "PCM_INDIVIDUAL"
    LPARTNRSHP = "LPARTNRSHP"
    CHARITY = "CHARITY"
    PLC = "PLC"
    LLP = "LLP"

    def __str__(self) -> str:
        return str(self.value)
