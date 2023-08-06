"""
A card payment method of a particular brand or name.  Used to mark up a particular payment method and/or the financial product/service that supplies the card account.Commonly used values:* http://purl.org/goodrelations/v1#AmericanExpress* http://purl.org/goodrelations/v1#DinersClub* http://purl.org/goodrelations/v1#Discover* http://purl.org/goodrelations/v1#JCB* http://purl.org/goodrelations/v1#MasterCard* http://purl.org/goodrelations/v1#VISA       

https://schema.org/CreditCard
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CreditCardInheritedProperties(TypedDict):
    """A card payment method of a particular brand or name.  Used to mark up a particular payment method and/or the financial product/service that supplies the card account.Commonly used values:* http://purl.org/goodrelations/v1#AmericanExpress* http://purl.org/goodrelations/v1#DinersClub* http://purl.org/goodrelations/v1#Discover* http://purl.org/goodrelations/v1#JCB* http://purl.org/goodrelations/v1#MasterCard* http://purl.org/goodrelations/v1#VISA       

    References:
        https://schema.org/CreditCard
    Note:
        Model Depth 6
    Attributes:
        requiredCollateral: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)
        loanType: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The type of a loan or credit.
        currency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        renegotiableLoan: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Whether the terms for payment of interest can be renegotiated during the life of the loan.
        gracePeriod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The period of time after any due date that the borrower has to fulfil its obligations before a default (failure to pay) is deemed to have occurred.
        loanTerm: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the loan or credit agreement.
        amount: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The amount of money.
        loanRepaymentForm: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A form of paying back money previously borrowed from a lender. Repayment usually takes the form of periodic payments that normally include part principal plus interest in each payment.
        recourseLoan: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): The only way you get the money back in the event of default is the security. Recourse is where you still have the opportunity to go back to the borrower for the rest of the money.
        floorLimit: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A floor limit is the amount of money above which credit card transactions must be authorized.
        cashBack: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj, StrictBool]], str, StrictInt, StrictFloat, SchemaOrgObj, StrictBool]]): A cardholder benefit that pays the cardholder a small percentage of their net expenditures.
        contactlessPayment: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): A secure method for consumers to purchase products or services via debit, credit or smartcards by using RFID or NFC technology.
        monthlyMinimumRepaymentAmount: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The minimum payment is the lowest amount of money that one is required to pay on a credit card statement each month.
    """

    requiredCollateral: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    loanType: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    renegotiableLoan: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    gracePeriod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    loanTerm: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    amount: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    loanRepaymentForm: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    recourseLoan: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    floorLimit: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cashBack: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj, StrictBool]], str, StrictInt, StrictFloat, SchemaOrgObj, StrictBool]]
    contactlessPayment: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    monthlyMinimumRepaymentAmount: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    


class CreditCardProperties(TypedDict):
    """A card payment method of a particular brand or name.  Used to mark up a particular payment method and/or the financial product/service that supplies the card account.Commonly used values:* http://purl.org/goodrelations/v1#AmericanExpress* http://purl.org/goodrelations/v1#DinersClub* http://purl.org/goodrelations/v1#Discover* http://purl.org/goodrelations/v1#JCB* http://purl.org/goodrelations/v1#MasterCard* http://purl.org/goodrelations/v1#VISA       

    References:
        https://schema.org/CreditCard
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(CreditCardInheritedProperties , CreditCardProperties, TypedDict):
    pass


class CreditCardBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CreditCard",alias='@id')
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
        fields = {'floorLimit': {'exclude': True}}
        fields = {'cashBack': {'exclude': True}}
        fields = {'contactlessPayment': {'exclude': True}}
        fields = {'monthlyMinimumRepaymentAmount': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CreditCardProperties, CreditCardInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CreditCard"
    return model
    

CreditCard = create_schema_org_model()


def create_creditcard_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_creditcard_model(model=model)
    return pydantic_type(model).schema_json()


