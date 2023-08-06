"""
Represents a sale price (usually active for a limited period) of an offered product.

https://schema.org/SalePrice
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SalePriceInheritedProperties(TypedDict):
    """Represents a sale price (usually active for a limited period) of an offered product.

    References:
        https://schema.org/SalePrice
    Note:
        Model Depth 5
    Attributes:
    """


class SalePriceProperties(TypedDict):
    """Represents a sale price (usually active for a limited period) of an offered product.

    References:
        https://schema.org/SalePrice
    Note:
        Model Depth 5
    Attributes:
    """


class SalePriceAllProperties(
    SalePriceInheritedProperties, SalePriceProperties, TypedDict
):
    pass


class SalePriceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SalePrice", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SalePriceProperties, SalePriceInheritedProperties, SalePriceAllProperties
    ] = SalePriceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SalePrice"
    return model


SalePrice = create_schema_org_model()


def create_saleprice_model(
    model: Union[
        SalePriceProperties, SalePriceInheritedProperties, SalePriceAllProperties
    ]
):
    _type = deepcopy(SalePriceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SalePriceAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SalePriceAllProperties):
    pydantic_type = create_saleprice_model(model=model)
    return pydantic_type(model).schema_json()
