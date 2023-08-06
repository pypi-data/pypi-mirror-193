"""
A tire shop.

https://schema.org/TireShop
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TireShopInheritedProperties(TypedDict):
    """A tire shop.

    References:
        https://schema.org/TireShop
    Note:
        Model Depth 5
    Attributes:
    """


class TireShopProperties(TypedDict):
    """A tire shop.

    References:
        https://schema.org/TireShop
    Note:
        Model Depth 5
    Attributes:
    """


class TireShopAllProperties(TireShopInheritedProperties, TireShopProperties, TypedDict):
    pass


class TireShopBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TireShop", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TireShopProperties, TireShopInheritedProperties, TireShopAllProperties
    ] = TireShopAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TireShop"
    return model


TireShop = create_schema_org_model()


def create_tireshop_model(
    model: Union[TireShopProperties, TireShopInheritedProperties, TireShopAllProperties]
):
    _type = deepcopy(TireShopAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of TireShopAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TireShopAllProperties):
    pydantic_type = create_tireshop_model(model=model)
    return pydantic_type(model).schema_json()
