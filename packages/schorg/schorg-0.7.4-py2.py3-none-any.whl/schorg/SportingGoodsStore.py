"""
A sporting goods store.

https://schema.org/SportingGoodsStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SportingGoodsStoreInheritedProperties(TypedDict):
    """A sporting goods store.

    References:
        https://schema.org/SportingGoodsStore
    Note:
        Model Depth 5
    Attributes:
    """


class SportingGoodsStoreProperties(TypedDict):
    """A sporting goods store.

    References:
        https://schema.org/SportingGoodsStore
    Note:
        Model Depth 5
    Attributes:
    """


class SportingGoodsStoreAllProperties(
    SportingGoodsStoreInheritedProperties, SportingGoodsStoreProperties, TypedDict
):
    pass


class SportingGoodsStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SportingGoodsStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SportingGoodsStoreProperties,
        SportingGoodsStoreInheritedProperties,
        SportingGoodsStoreAllProperties,
    ] = SportingGoodsStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SportingGoodsStore"
    return model


SportingGoodsStore = create_schema_org_model()


def create_sportinggoodsstore_model(
    model: Union[
        SportingGoodsStoreProperties,
        SportingGoodsStoreInheritedProperties,
        SportingGoodsStoreAllProperties,
    ]
):
    _type = deepcopy(SportingGoodsStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SportingGoodsStoreAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SportingGoodsStoreAllProperties):
    pydantic_type = create_sportinggoodsstore_model(model=model)
    return pydantic_type(model).schema_json()
