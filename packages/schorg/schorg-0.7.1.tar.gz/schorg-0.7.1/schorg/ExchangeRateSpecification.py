"""
A structured value representing exchange rate.

https://schema.org/ExchangeRateSpecification
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ExchangeRateSpecificationInheritedProperties(TypedDict):
    """A structured value representing exchange rate.

    References:
        https://schema.org/ExchangeRateSpecification
    Note:
        Model Depth 4
    Attributes:
    """

    


class ExchangeRateSpecificationProperties(TypedDict):
    """A structured value representing exchange rate.

    References:
        https://schema.org/ExchangeRateSpecification
    Note:
        Model Depth 4
    Attributes:
        currency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        currentExchangeRate: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The current price of a currency.
        exchangeRateSpread: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The difference between the price at which a broker or other intermediary buys and sells foreign currency.
    """

    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    currentExchangeRate: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    exchangeRateSpread: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    


class AllProperties(ExchangeRateSpecificationInheritedProperties , ExchangeRateSpecificationProperties, TypedDict):
    pass


class ExchangeRateSpecificationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ExchangeRateSpecification",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'currency': {'exclude': True}}
        fields = {'currentExchangeRate': {'exclude': True}}
        fields = {'exchangeRateSpread': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ExchangeRateSpecificationProperties, ExchangeRateSpecificationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ExchangeRateSpecification"
    return model
    

ExchangeRateSpecification = create_schema_org_model()


def create_exchangeratespecification_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_exchangeratespecification_model(model=model)
    return pydantic_type(model).schema_json()


