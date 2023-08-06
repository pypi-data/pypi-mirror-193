"""
BroadcastRelease.

https://schema.org/BroadcastRelease
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BroadcastReleaseInheritedProperties(TypedDict):
    """BroadcastRelease.

    References:
        https://schema.org/BroadcastRelease
    Note:
        Model Depth 5
    Attributes:
    """


class BroadcastReleaseProperties(TypedDict):
    """BroadcastRelease.

    References:
        https://schema.org/BroadcastRelease
    Note:
        Model Depth 5
    Attributes:
    """


class BroadcastReleaseAllProperties(
    BroadcastReleaseInheritedProperties, BroadcastReleaseProperties, TypedDict
):
    pass


class BroadcastReleaseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BroadcastRelease", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BroadcastReleaseProperties,
        BroadcastReleaseInheritedProperties,
        BroadcastReleaseAllProperties,
    ] = BroadcastReleaseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BroadcastRelease"
    return model


BroadcastRelease = create_schema_org_model()


def create_broadcastrelease_model(
    model: Union[
        BroadcastReleaseProperties,
        BroadcastReleaseInheritedProperties,
        BroadcastReleaseAllProperties,
    ]
):
    _type = deepcopy(BroadcastReleaseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BroadcastReleaseAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BroadcastReleaseAllProperties):
    pydantic_type = create_broadcastrelease_model(model=model)
    return pydantic_type(model).schema_json()
