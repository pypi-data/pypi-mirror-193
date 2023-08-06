"""
A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)

https://schema.org/MortgageLoan
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MortgageLoanInheritedProperties(TypedDict):
    """A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)

    References:
        https://schema.org/MortgageLoan
    Note:
        Model Depth 6
    Attributes:
        requiredCollateral: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)
        loanType: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The type of a loan or credit.
        currency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        renegotiableLoan: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether the terms for payment of interest can be renegotiated during the life of the loan.
        gracePeriod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The period of time after any due date that the borrower has to fulfil its obligations before a default (failure to pay) is deemed to have occurred.
        loanTerm: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of the loan or credit agreement.
        amount: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The amount of money.
        loanRepaymentForm: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A form of paying back money previously borrowed from a lender. Repayment usually takes the form of periodic payments that normally include part principal plus interest in each payment.
        recourseLoan: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): The only way you get the money back in the event of default is the security. Recourse is where you still have the opportunity to go back to the borrower for the rest of the money.
    """

    requiredCollateral: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    loanType: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    currency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    renegotiableLoan: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    gracePeriod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    loanTerm: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    amount: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    loanRepaymentForm: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    recourseLoan: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    


class MortgageLoanProperties(TypedDict):
    """A loan in which property or real estate is used as collateral. (A loan securitized against some real estate.)

    References:
        https://schema.org/MortgageLoan
    Note:
        Model Depth 6
    Attributes:
        loanMortgageMandateAmount: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Amount of mortgage mandate that can be converted into a proper mortgage at a later stage.
        domiciledMortgage: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Whether borrower is a resident of the jurisdiction where the property is located.
    """

    loanMortgageMandateAmount: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    domiciledMortgage: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    


class AllProperties(MortgageLoanInheritedProperties , MortgageLoanProperties, TypedDict):
    pass


class MortgageLoanBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MortgageLoan",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'requiredCollateral': {'exclude': True}}
        fields = {'loanType': {'exclude': True}}
        fields = {'currency': {'exclude': True}}
        fields = {'renegotiableLoan': {'exclude': True}}
        fields = {'gracePeriod': {'exclude': True}}
        fields = {'loanTerm': {'exclude': True}}
        fields = {'amount': {'exclude': True}}
        fields = {'loanRepaymentForm': {'exclude': True}}
        fields = {'recourseLoan': {'exclude': True}}
        fields = {'loanMortgageMandateAmount': {'exclude': True}}
        fields = {'domiciledMortgage': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MortgageLoanProperties, MortgageLoanInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MortgageLoan"
    return model
    

MortgageLoan = create_schema_org_model()


def create_mortgageloan_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mortgageloan_model(model=model)
    return pydantic_type(model).schema_json()


