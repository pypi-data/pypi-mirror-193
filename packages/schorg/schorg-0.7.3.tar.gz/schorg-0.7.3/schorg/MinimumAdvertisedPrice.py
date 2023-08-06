"""
Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product.

https://schema.org/MinimumAdvertisedPrice
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MinimumAdvertisedPriceInheritedProperties(TypedDict):
    """Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product.

    References:
        https://schema.org/MinimumAdvertisedPrice
    Note:
        Model Depth 5
    Attributes:
    """


class MinimumAdvertisedPriceProperties(TypedDict):
    """Represents the minimum advertised price ("MAP") (as dictated by the manufacturer) of an offered product.

    References:
        https://schema.org/MinimumAdvertisedPrice
    Note:
        Model Depth 5
    Attributes:
    """


class MinimumAdvertisedPriceAllProperties(
    MinimumAdvertisedPriceInheritedProperties,
    MinimumAdvertisedPriceProperties,
    TypedDict,
):
    pass


class MinimumAdvertisedPriceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MinimumAdvertisedPrice", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MinimumAdvertisedPriceProperties,
        MinimumAdvertisedPriceInheritedProperties,
        MinimumAdvertisedPriceAllProperties,
    ] = MinimumAdvertisedPriceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MinimumAdvertisedPrice"
    return model


MinimumAdvertisedPrice = create_schema_org_model()


def create_minimumadvertisedprice_model(
    model: Union[
        MinimumAdvertisedPriceProperties,
        MinimumAdvertisedPriceInheritedProperties,
        MinimumAdvertisedPriceAllProperties,
    ]
):
    _type = deepcopy(MinimumAdvertisedPriceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MinimumAdvertisedPriceAllProperties):
    pydantic_type = create_minimumadvertisedprice_model(model=model)
    return pydantic_type(model).schema_json()
