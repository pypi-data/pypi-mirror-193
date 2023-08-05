from enum import Enum


class PispgatewayLegacyPaymentContextPaymentContextCode(str, Enum):
    Bill_Payment = "BillPayment"
    ECOMMERCEGOODS = "ECOMMERCEGOODS"
    BILLPAYMENT = "BILLPAYMENT"
    Other = "Other"
    PARTYTOPARTY = "PARTYTOPARTY"
    OTHER = "OTHER"
    Ecommerce_Services = "EcommerceServices"
    Party_To_Party = "PartyToParty"
    ECOMMERCESERVICES = "ECOMMERCESERVICES"
    Ecommerce_Goods = "EcommerceGoods"

    def __str__(self) -> str:
        return str(self.value)
