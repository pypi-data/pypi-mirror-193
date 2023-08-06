"""
A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]] Types to describe the price of an Offer, Invoice, etc.

https://schema.org/MonetaryAmount
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MonetaryAmountInheritedProperties(TypedDict):
    """A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]] Types to describe the price of an Offer, Invoice, etc.

    References:
        https://schema.org/MonetaryAmount
    Note:
        Model Depth 4
    Attributes:
    """


class MonetaryAmountProperties(TypedDict):
    """A monetary value or range. This type can be used to describe an amount of money such as $50 USD, or a range as in describing a bank account being suitable for a balance between £1,000 and £1,000,000 GBP, or the value of a salary, etc. It is recommended to use [[PriceSpecification]] Types to describe the price of an Offer, Invoice, etc.

    References:
        https://schema.org/MonetaryAmount
    Note:
        Model Depth 4
    Attributes:
        value: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, StrictInt, StrictFloat, str]], StrictBool, SchemaOrgObj, StrictInt, StrictFloat, str]]): The value of the quantitative value or property value node.* For [[QuantitativeValue]] and [[MonetaryAmount]], the recommended type for values is 'Number'.* For [[PropertyValue]], it can be 'Text', 'Number', 'Boolean', or 'StructuredValue'.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        currency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        validThrough: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        maxValue: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The upper value of some characteristic or property.
        validFrom: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date when the item becomes valid.
        minValue: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The lower value of some characteristic or property.
    """

    value: NotRequired[
        Union[
            List[Union[StrictBool, SchemaOrgObj, StrictInt, StrictFloat, str]],
            StrictBool,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
            str,
        ]
    ]
    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    validThrough: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    maxValue: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    validFrom: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    minValue: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class MonetaryAmountAllProperties(
    MonetaryAmountInheritedProperties, MonetaryAmountProperties, TypedDict
):
    pass


class MonetaryAmountBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MonetaryAmount", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"value": {"exclude": True}}
        fields = {"currency": {"exclude": True}}
        fields = {"validThrough": {"exclude": True}}
        fields = {"maxValue": {"exclude": True}}
        fields = {"validFrom": {"exclude": True}}
        fields = {"minValue": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MonetaryAmountProperties,
        MonetaryAmountInheritedProperties,
        MonetaryAmountAllProperties,
    ] = MonetaryAmountAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MonetaryAmount"
    return model


MonetaryAmount = create_schema_org_model()


def create_monetaryamount_model(
    model: Union[
        MonetaryAmountProperties,
        MonetaryAmountInheritedProperties,
        MonetaryAmountAllProperties,
    ]
):
    _type = deepcopy(MonetaryAmountAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MonetaryAmount. Please see: https://schema.org/MonetaryAmount"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MonetaryAmountAllProperties):
    pydantic_type = create_monetaryamount_model(model=model)
    return pydantic_type(model).schema_json()
