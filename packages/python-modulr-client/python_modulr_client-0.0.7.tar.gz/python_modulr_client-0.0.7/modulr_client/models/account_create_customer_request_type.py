from enum import Enum


class AccountCreateCustomerRequestType(str, Enum):
    LLC = "LLC"
    PLC = "PLC"
    SOLETRADER = "SOLETRADER"
    OPARTNRSHP = "OPARTNRSHP"
    LPARTNRSHP = "LPARTNRSHP"
    LLP = "LLP"
    CHARITY = "CHARITY"
    INDIVIDUAL = "INDIVIDUAL"
    PCM_INDIVIDUAL = "PCM_INDIVIDUAL"
    PCM_BUSINESS = "PCM_BUSINESS"
    TRUST = "TRUST"

    def __str__(self) -> str:
        return str(self.value)
