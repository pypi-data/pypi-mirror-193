"""
A shoe store.

https://schema.org/ShoeStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ShoeStoreInheritedProperties(TypedDict):
    """A shoe store.

    References:
        https://schema.org/ShoeStore
    Note:
        Model Depth 5
    Attributes:
    """


class ShoeStoreProperties(TypedDict):
    """A shoe store.

    References:
        https://schema.org/ShoeStore
    Note:
        Model Depth 5
    Attributes:
    """


class ShoeStoreAllProperties(
    ShoeStoreInheritedProperties, ShoeStoreProperties, TypedDict
):
    pass


class ShoeStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ShoeStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ShoeStoreProperties, ShoeStoreInheritedProperties, ShoeStoreAllProperties
    ] = ShoeStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ShoeStore"
    return model


ShoeStore = create_schema_org_model()


def create_shoestore_model(
    model: Union[
        ShoeStoreProperties, ShoeStoreInheritedProperties, ShoeStoreAllProperties
    ]
):
    _type = deepcopy(ShoeStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ShoeStoreAllProperties):
    pydantic_type = create_shoestore_model(model=model)
    return pydantic_type(model).schema_json()
