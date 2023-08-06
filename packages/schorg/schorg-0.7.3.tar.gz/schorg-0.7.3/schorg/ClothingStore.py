"""
A clothing store.

https://schema.org/ClothingStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ClothingStoreInheritedProperties(TypedDict):
    """A clothing store.

    References:
        https://schema.org/ClothingStore
    Note:
        Model Depth 5
    Attributes:
    """


class ClothingStoreProperties(TypedDict):
    """A clothing store.

    References:
        https://schema.org/ClothingStore
    Note:
        Model Depth 5
    Attributes:
    """


class ClothingStoreAllProperties(
    ClothingStoreInheritedProperties, ClothingStoreProperties, TypedDict
):
    pass


class ClothingStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ClothingStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ClothingStoreProperties,
        ClothingStoreInheritedProperties,
        ClothingStoreAllProperties,
    ] = ClothingStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ClothingStore"
    return model


ClothingStore = create_schema_org_model()


def create_clothingstore_model(
    model: Union[
        ClothingStoreProperties,
        ClothingStoreInheritedProperties,
        ClothingStoreAllProperties,
    ]
):
    _type = deepcopy(ClothingStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ClothingStoreAllProperties):
    pydantic_type = create_clothingstore_model(model=model)
    return pydantic_type(model).schema_json()
