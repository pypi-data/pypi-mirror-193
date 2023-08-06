"""
A bike store.

https://schema.org/BikeStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BikeStoreInheritedProperties(TypedDict):
    """A bike store.

    References:
        https://schema.org/BikeStore
    Note:
        Model Depth 5
    Attributes:
    """


class BikeStoreProperties(TypedDict):
    """A bike store.

    References:
        https://schema.org/BikeStore
    Note:
        Model Depth 5
    Attributes:
    """


class BikeStoreAllProperties(
    BikeStoreInheritedProperties, BikeStoreProperties, TypedDict
):
    pass


class BikeStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BikeStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BikeStoreProperties, BikeStoreInheritedProperties, BikeStoreAllProperties
    ] = BikeStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BikeStore"
    return model


BikeStore = create_schema_org_model()


def create_bikestore_model(
    model: Union[
        BikeStoreProperties, BikeStoreInheritedProperties, BikeStoreAllProperties
    ]
):
    _type = deepcopy(BikeStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BikeStoreAllProperties):
    pydantic_type = create_bikestore_model(model=model)
    return pydantic_type(model).schema_json()
