"""
BroadcastRelease.

https://schema.org/BroadcastRelease
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(BroadcastReleaseInheritedProperties , BroadcastReleaseProperties, TypedDict):
    pass


class BroadcastReleaseBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BroadcastRelease",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BroadcastReleaseProperties, BroadcastReleaseInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BroadcastRelease"
    return model
    

BroadcastRelease = create_schema_org_model()


def create_broadcastrelease_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_broadcastrelease_model(model=model)
    return pydantic_type(model).schema_json()


