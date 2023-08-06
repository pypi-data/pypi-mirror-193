"""
A home goods store.

https://schema.org/HomeGoodsStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HomeGoodsStoreInheritedProperties(TypedDict):
    """A home goods store.

    References:
        https://schema.org/HomeGoodsStore
    Note:
        Model Depth 5
    Attributes:
    """


class HomeGoodsStoreProperties(TypedDict):
    """A home goods store.

    References:
        https://schema.org/HomeGoodsStore
    Note:
        Model Depth 5
    Attributes:
    """


class HomeGoodsStoreAllProperties(
    HomeGoodsStoreInheritedProperties, HomeGoodsStoreProperties, TypedDict
):
    pass


class HomeGoodsStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HomeGoodsStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HomeGoodsStoreProperties,
        HomeGoodsStoreInheritedProperties,
        HomeGoodsStoreAllProperties,
    ] = HomeGoodsStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HomeGoodsStore"
    return model


HomeGoodsStore = create_schema_org_model()


def create_homegoodsstore_model(
    model: Union[
        HomeGoodsStoreProperties,
        HomeGoodsStoreInheritedProperties,
        HomeGoodsStoreAllProperties,
    ]
):
    _type = deepcopy(HomeGoodsStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HomeGoodsStoreAllProperties):
    pydantic_type = create_homegoodsstore_model(model=model)
    return pydantic_type(model).schema_json()
