"""
A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)

https://schema.org/MortgageLoan
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MortgageLoanInheritedProperties(TypedDict):
    """A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)

    References:
        https://schema.org/MortgageLoan
    Note:
        Model Depth 6
    Attributes:
        requiredCollateral: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)
        loanType: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The type of a loan or credit.
        currency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        renegotiableLoan: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): Whether the terms for payment of interest can be renegotiated during the life of the loan.
        gracePeriod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The period of time after any due date that the borrower has to fulfil its obligations before a default (failure to pay) is deemed to have occurred.
        loanTerm: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the loan or credit agreement.
        amount: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The amount of money.
        loanRepaymentForm: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A form of paying back money previously borrowed from a lender. Repayment usually takes the form of periodic payments that normally include part principal plus interest in each payment.
        recourseLoan: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): The only way you get the money back in the event of default is the security. Recourse is where you still have the opportunity to go back to the borrower for the rest of the money.
    """

    requiredCollateral: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    loanType: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    renegotiableLoan: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]
    gracePeriod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    loanTerm: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    amount: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    loanRepaymentForm: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    recourseLoan: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]


class MortgageLoanProperties(TypedDict):
    """A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)

    References:
        https://schema.org/MortgageLoan
    Note:
        Model Depth 6
    Attributes:
        loanMortgageMandateAmount: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Amount of mortgage mandate that can be converted into a proper mortgage at a later stage.
        domiciledMortgage: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): Whether borrower is a resident of the jurisdiction where the property is located.
    """

    loanMortgageMandateAmount: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    domiciledMortgage: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]


class MortgageLoanAllProperties(
    MortgageLoanInheritedProperties, MortgageLoanProperties, TypedDict
):
    pass


class MortgageLoanBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MortgageLoan", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"requiredCollateral": {"exclude": True}}
        fields = {"loanType": {"exclude": True}}
        fields = {"currency": {"exclude": True}}
        fields = {"renegotiableLoan": {"exclude": True}}
        fields = {"gracePeriod": {"exclude": True}}
        fields = {"loanTerm": {"exclude": True}}
        fields = {"amount": {"exclude": True}}
        fields = {"loanRepaymentForm": {"exclude": True}}
        fields = {"recourseLoan": {"exclude": True}}
        fields = {"loanMortgageMandateAmount": {"exclude": True}}
        fields = {"domiciledMortgage": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MortgageLoanProperties,
        MortgageLoanInheritedProperties,
        MortgageLoanAllProperties,
    ] = MortgageLoanAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MortgageLoan"
    return model


MortgageLoan = create_schema_org_model()


def create_mortgageloan_model(
    model: Union[
        MortgageLoanProperties,
        MortgageLoanInheritedProperties,
        MortgageLoanAllProperties,
    ]
):
    _type = deepcopy(MortgageLoanAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MortgageLoan. Please see: https://schema.org/MortgageLoan"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MortgageLoanAllProperties):
    pydantic_type = create_mortgageloan_model(model=model)
    return pydantic_type(model).schema_json()
