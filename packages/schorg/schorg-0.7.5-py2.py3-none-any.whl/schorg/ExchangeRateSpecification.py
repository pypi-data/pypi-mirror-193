"""
A structured value representing exchange rate.

https://schema.org/ExchangeRateSpecification
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        exchangeRateSpread: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The difference between the price at which a broker or other intermediary buys and sells foreign currency.
    """

    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    currentExchangeRate: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    exchangeRateSpread: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class ExchangeRateSpecificationAllProperties(
    ExchangeRateSpecificationInheritedProperties,
    ExchangeRateSpecificationProperties,
    TypedDict,
):
    pass


class ExchangeRateSpecificationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ExchangeRateSpecification", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"currency": {"exclude": True}}
        fields = {"currentExchangeRate": {"exclude": True}}
        fields = {"exchangeRateSpread": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ExchangeRateSpecificationProperties,
        ExchangeRateSpecificationInheritedProperties,
        ExchangeRateSpecificationAllProperties,
    ] = ExchangeRateSpecificationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ExchangeRateSpecification"
    return model


ExchangeRateSpecification = create_schema_org_model()


def create_exchangeratespecification_model(
    model: Union[
        ExchangeRateSpecificationProperties,
        ExchangeRateSpecificationInheritedProperties,
        ExchangeRateSpecificationAllProperties,
    ]
):
    _type = deepcopy(ExchangeRateSpecificationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ExchangeRateSpecification. Please see: https://schema.org/ExchangeRateSpecification"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ExchangeRateSpecificationAllProperties):
    pydantic_type = create_exchangeratespecification_model(model=model)
    return pydantic_type(model).schema_json()
