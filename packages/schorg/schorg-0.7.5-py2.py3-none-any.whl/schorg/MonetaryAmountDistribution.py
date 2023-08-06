"""
A statistical distribution of monetary amounts.

https://schema.org/MonetaryAmountDistribution
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MonetaryAmountDistributionInheritedProperties(TypedDict):
    """A statistical distribution of monetary amounts.

    References:
        https://schema.org/MonetaryAmountDistribution
    Note:
        Model Depth 5
    Attributes:
        percentile75: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The 75th percentile value.
        percentile25: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The 25th percentile value.
        duration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        median: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The median value.
        percentile90: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The 90th percentile value.
        percentile10: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The 10th percentile value.
    """

    percentile75: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    percentile25: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    duration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    median: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    percentile90: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    percentile10: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class MonetaryAmountDistributionProperties(TypedDict):
    """A statistical distribution of monetary amounts.

    References:
        https://schema.org/MonetaryAmountDistribution
    Note:
        Model Depth 5
    Attributes:
        currency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency in which the monetary amount is expressed.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    """

    currency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MonetaryAmountDistributionAllProperties(
    MonetaryAmountDistributionInheritedProperties,
    MonetaryAmountDistributionProperties,
    TypedDict,
):
    pass


class MonetaryAmountDistributionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MonetaryAmountDistribution", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"percentile75": {"exclude": True}}
        fields = {"percentile25": {"exclude": True}}
        fields = {"duration": {"exclude": True}}
        fields = {"median": {"exclude": True}}
        fields = {"percentile90": {"exclude": True}}
        fields = {"percentile10": {"exclude": True}}
        fields = {"currency": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MonetaryAmountDistributionProperties,
        MonetaryAmountDistributionInheritedProperties,
        MonetaryAmountDistributionAllProperties,
    ] = MonetaryAmountDistributionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MonetaryAmountDistribution"
    return model


MonetaryAmountDistribution = create_schema_org_model()


def create_monetaryamountdistribution_model(
    model: Union[
        MonetaryAmountDistributionProperties,
        MonetaryAmountDistributionInheritedProperties,
        MonetaryAmountDistributionAllProperties,
    ]
):
    _type = deepcopy(MonetaryAmountDistributionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MonetaryAmountDistribution. Please see: https://schema.org/MonetaryAmountDistribution"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MonetaryAmountDistributionAllProperties):
    pydantic_type = create_monetaryamountdistribution_model(model=model)
    return pydantic_type(model).schema_json()
