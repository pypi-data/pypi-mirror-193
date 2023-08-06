"""
A payment method using a credit, debit, store or other card to associate the payment with an account.

https://schema.org/PaymentCard
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentCardInheritedProperties(TypedDict):
    """A payment method using a credit, debit, store or other card to associate the payment with an account.

    References:
        https://schema.org/PaymentCard
    Note:
        Model Depth 5
    Attributes:
        annualPercentageRate: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.
        interestRate: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.
        feesAndCommissionsSpecification: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    annualPercentageRate: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    interestRate: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    feesAndCommissionsSpecification: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    


class PaymentCardProperties(TypedDict):
    """A payment method using a credit, debit, store or other card to associate the payment with an account.

    References:
        https://schema.org/PaymentCard
    Note:
        Model Depth 5
    Attributes:
        floorLimit: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A floor limit is the amount of money above which credit card transactions must be authorized.
        cashBack: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictBool, StrictInt, StrictFloat]]): A cardholder benefit that pays the cardholder a small percentage of their net expenditures.
        contactlessPayment: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): A secure method for consumers to purchase products or services via debit, credit or smartcards by using RFID or NFC technology.
        monthlyMinimumRepaymentAmount: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The minimum payment is the lowest amount of money that one is required to pay on a credit card statement each month.
    """

    floorLimit: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cashBack: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictBool, StrictInt, StrictFloat]]
    contactlessPayment: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    monthlyMinimumRepaymentAmount: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    


class AllProperties(PaymentCardInheritedProperties , PaymentCardProperties, TypedDict):
    pass


class PaymentCardBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PaymentCard",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'annualPercentageRate': {'exclude': True}}
        fields = {'interestRate': {'exclude': True}}
        fields = {'feesAndCommissionsSpecification': {'exclude': True}}
        fields = {'floorLimit': {'exclude': True}}
        fields = {'cashBack': {'exclude': True}}
        fields = {'contactlessPayment': {'exclude': True}}
        fields = {'monthlyMinimumRepaymentAmount': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PaymentCardProperties, PaymentCardInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentCard"
    return model
    

PaymentCard = create_schema_org_model()


def create_paymentcard_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_paymentcard_model(model=model)
    return pydantic_type(model).schema_json()


