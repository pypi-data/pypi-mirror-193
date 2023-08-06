"""
A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.

https://schema.org/LoanOrCredit
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LoanOrCreditInheritedProperties(TypedDict):
    """A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.

    References:
        https://schema.org/LoanOrCredit
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


class LoanOrCreditProperties(TypedDict):
    """A financial product for the loaning of an amount of money, or line of credit, under agreed terms and charges.

    References:
        https://schema.org/LoanOrCredit
    Note:
        Model Depth 5
    Attributes:
        requiredCollateral: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)
        loanType: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The type of a loan or credit.
        currency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        renegotiableLoan: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether the terms for payment of interest can be renegotiated during the life of the loan.
        gracePeriod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The period of time after any due date that the borrower has to fulfil its obligations before a default (failure to pay) is deemed to have occurred.
        loanTerm: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of the loan or credit agreement.
        amount: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The amount of money.
        loanRepaymentForm: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A form of paying back money previously borrowed from a lender. Repayment usually takes the form of periodic payments that normally include part principal plus interest in each payment.
        recourseLoan: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): The only way you get the money back in the event of default is the security. Recourse is where you still have the opportunity to go back to the borrower for the rest of the money.
    """

    requiredCollateral: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    loanType: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    currency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    renegotiableLoan: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    gracePeriod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    loanTerm: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    amount: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    loanRepaymentForm: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    recourseLoan: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]


class LoanOrCreditAllProperties(
    LoanOrCreditInheritedProperties, LoanOrCreditProperties, TypedDict
):
    pass


class LoanOrCreditBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LoanOrCredit", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"annualPercentageRate": {"exclude": True}}
        fields = {"interestRate": {"exclude": True}}
        fields = {"feesAndCommissionsSpecification": {"exclude": True}}
        fields = {"requiredCollateral": {"exclude": True}}
        fields = {"loanType": {"exclude": True}}
        fields = {"currency": {"exclude": True}}
        fields = {"renegotiableLoan": {"exclude": True}}
        fields = {"gracePeriod": {"exclude": True}}
        fields = {"loanTerm": {"exclude": True}}
        fields = {"amount": {"exclude": True}}
        fields = {"loanRepaymentForm": {"exclude": True}}
        fields = {"recourseLoan": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        LoanOrCreditProperties,
        LoanOrCreditInheritedProperties,
        LoanOrCreditAllProperties,
    ] = LoanOrCreditAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LoanOrCredit"
    return model


LoanOrCredit = create_schema_org_model()


def create_loanorcredit_model(
    model: Union[
        LoanOrCreditProperties,
        LoanOrCreditInheritedProperties,
        LoanOrCreditAllProperties,
    ]
):
    _type = deepcopy(LoanOrCreditAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of LoanOrCreditAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LoanOrCreditAllProperties):
    pydantic_type = create_loanorcredit_model(model=model)
    return pydantic_type(model).schema_json()
