"""
A payment method using a credit, debit, store or other card to associate the payment with an account.

https://schema.org/PaymentCard
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentCardInheritedProperties(TypedDict):
    """A payment method using a credit, debit, store or other card to associate the payment with an account.

    References:
        https://schema.org/PaymentCard
    Note:
        Model Depth 5
    Attributes:
        annualPercentageRate: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.
        interestRate: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.
        feesAndCommissionsSpecification: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.
    """

    annualPercentageRate: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    interestRate: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    feesAndCommissionsSpecification: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class PaymentCardProperties(TypedDict):
    """A payment method using a credit, debit, store or other card to associate the payment with an account.

    References:
        https://schema.org/PaymentCard
    Note:
        Model Depth 5
    Attributes:
        floorLimit: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A floor limit is the amount of money above which credit card transactions must be authorized.
        cashBack: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str, StrictBool]], StrictInt, StrictFloat, SchemaOrgObj, str, StrictBool]]): A cardholder benefit that pays the cardholder a small percentage of their net expenditures.
        contactlessPayment: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): A secure method for consumers to purchase products or services via debit, credit or smartcards by using RFID or NFC technology.
        monthlyMinimumRepaymentAmount: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The minimum payment is the lowest amount of money that one is required to pay on a credit card statement each month.
    """

    floorLimit: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cashBack: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str, StrictBool]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
            StrictBool,
        ]
    ]
    contactlessPayment: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    monthlyMinimumRepaymentAmount: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class PaymentCardAllProperties(
    PaymentCardInheritedProperties, PaymentCardProperties, TypedDict
):
    pass


class PaymentCardBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentCard", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"annualPercentageRate": {"exclude": True}}
        fields = {"interestRate": {"exclude": True}}
        fields = {"feesAndCommissionsSpecification": {"exclude": True}}
        fields = {"floorLimit": {"exclude": True}}
        fields = {"cashBack": {"exclude": True}}
        fields = {"contactlessPayment": {"exclude": True}}
        fields = {"monthlyMinimumRepaymentAmount": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PaymentCardProperties, PaymentCardInheritedProperties, PaymentCardAllProperties
    ] = PaymentCardAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentCard"
    return model


PaymentCard = create_schema_org_model()


def create_paymentcard_model(
    model: Union[
        PaymentCardProperties, PaymentCardInheritedProperties, PaymentCardAllProperties
    ]
):
    _type = deepcopy(PaymentCardAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PaymentCardAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PaymentCardAllProperties):
    pydantic_type = create_paymentcard_model(model=model)
    return pydantic_type(model).schema_json()
