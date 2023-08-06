"""
A grocery store.

https://schema.org/GroceryStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GroceryStoreInheritedProperties(TypedDict):
    """A grocery store.

    References:
        https://schema.org/GroceryStore
    Note:
        Model Depth 5
    Attributes:
    """


class GroceryStoreProperties(TypedDict):
    """A grocery store.

    References:
        https://schema.org/GroceryStore
    Note:
        Model Depth 5
    Attributes:
    """


class GroceryStoreAllProperties(
    GroceryStoreInheritedProperties, GroceryStoreProperties, TypedDict
):
    pass


class GroceryStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GroceryStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GroceryStoreProperties,
        GroceryStoreInheritedProperties,
        GroceryStoreAllProperties,
    ] = GroceryStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GroceryStore"
    return model


GroceryStore = create_schema_org_model()


def create_grocerystore_model(
    model: Union[
        GroceryStoreProperties,
        GroceryStoreInheritedProperties,
        GroceryStoreAllProperties,
    ]
):
    _type = deepcopy(GroceryStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GroceryStoreAllProperties):
    pydantic_type = create_grocerystore_model(model=model)
    return pydantic_type(model).schema_json()
