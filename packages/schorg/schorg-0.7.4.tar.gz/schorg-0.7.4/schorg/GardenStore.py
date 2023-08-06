"""
A garden store.

https://schema.org/GardenStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GardenStoreInheritedProperties(TypedDict):
    """A garden store.

    References:
        https://schema.org/GardenStore
    Note:
        Model Depth 5
    Attributes:
    """


class GardenStoreProperties(TypedDict):
    """A garden store.

    References:
        https://schema.org/GardenStore
    Note:
        Model Depth 5
    Attributes:
    """


class GardenStoreAllProperties(
    GardenStoreInheritedProperties, GardenStoreProperties, TypedDict
):
    pass


class GardenStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GardenStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GardenStoreProperties, GardenStoreInheritedProperties, GardenStoreAllProperties
    ] = GardenStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GardenStore"
    return model


GardenStore = create_schema_org_model()


def create_gardenstore_model(
    model: Union[
        GardenStoreProperties, GardenStoreInheritedProperties, GardenStoreAllProperties
    ]
):
    _type = deepcopy(GardenStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of GardenStoreAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GardenStoreAllProperties):
    pydantic_type = create_gardenstore_model(model=model)
    return pydantic_type(model).schema_json()
