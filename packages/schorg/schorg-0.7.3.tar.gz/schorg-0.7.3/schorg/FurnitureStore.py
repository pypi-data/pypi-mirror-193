"""
A furniture store.

https://schema.org/FurnitureStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FurnitureStoreInheritedProperties(TypedDict):
    """A furniture store.

    References:
        https://schema.org/FurnitureStore
    Note:
        Model Depth 5
    Attributes:
    """


class FurnitureStoreProperties(TypedDict):
    """A furniture store.

    References:
        https://schema.org/FurnitureStore
    Note:
        Model Depth 5
    Attributes:
    """


class FurnitureStoreAllProperties(
    FurnitureStoreInheritedProperties, FurnitureStoreProperties, TypedDict
):
    pass


class FurnitureStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FurnitureStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FurnitureStoreProperties,
        FurnitureStoreInheritedProperties,
        FurnitureStoreAllProperties,
    ] = FurnitureStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FurnitureStore"
    return model


FurnitureStore = create_schema_org_model()


def create_furniturestore_model(
    model: Union[
        FurnitureStoreProperties,
        FurnitureStoreInheritedProperties,
        FurnitureStoreAllProperties,
    ]
):
    _type = deepcopy(FurnitureStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FurnitureStoreAllProperties):
    pydantic_type = create_furniturestore_model(model=model)
    return pydantic_type(model).schema_json()
