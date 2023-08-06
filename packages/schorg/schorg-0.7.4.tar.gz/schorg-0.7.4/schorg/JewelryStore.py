"""
A jewelry store.

https://schema.org/JewelryStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class JewelryStoreInheritedProperties(TypedDict):
    """A jewelry store.

    References:
        https://schema.org/JewelryStore
    Note:
        Model Depth 5
    Attributes:
    """


class JewelryStoreProperties(TypedDict):
    """A jewelry store.

    References:
        https://schema.org/JewelryStore
    Note:
        Model Depth 5
    Attributes:
    """


class JewelryStoreAllProperties(
    JewelryStoreInheritedProperties, JewelryStoreProperties, TypedDict
):
    pass


class JewelryStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="JewelryStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        JewelryStoreProperties,
        JewelryStoreInheritedProperties,
        JewelryStoreAllProperties,
    ] = JewelryStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "JewelryStore"
    return model


JewelryStore = create_schema_org_model()


def create_jewelrystore_model(
    model: Union[
        JewelryStoreProperties,
        JewelryStoreInheritedProperties,
        JewelryStoreAllProperties,
    ]
):
    _type = deepcopy(JewelryStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of JewelryStoreAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: JewelryStoreAllProperties):
    pydantic_type = create_jewelrystore_model(model=model)
    return pydantic_type(model).schema_json()
