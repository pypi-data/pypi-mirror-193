"""
An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world.

https://schema.org/VirtualLocation
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VirtualLocationInheritedProperties(TypedDict):
    """An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world.

    References:
        https://schema.org/VirtualLocation
    Note:
        Model Depth 3
    Attributes:
    """


class VirtualLocationProperties(TypedDict):
    """An online or virtual location for attending events. For example, one may attend an online seminar or educational event. While a virtual location may be used as the location of an event, virtual locations should not be confused with physical locations in the real world.

    References:
        https://schema.org/VirtualLocation
    Note:
        Model Depth 3
    Attributes:
    """


class VirtualLocationAllProperties(
    VirtualLocationInheritedProperties, VirtualLocationProperties, TypedDict
):
    pass


class VirtualLocationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="VirtualLocation", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        VirtualLocationProperties,
        VirtualLocationInheritedProperties,
        VirtualLocationAllProperties,
    ] = VirtualLocationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VirtualLocation"
    return model


VirtualLocation = create_schema_org_model()


def create_virtuallocation_model(
    model: Union[
        VirtualLocationProperties,
        VirtualLocationInheritedProperties,
        VirtualLocationAllProperties,
    ]
):
    _type = deepcopy(VirtualLocationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of VirtualLocationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: VirtualLocationAllProperties):
    pydantic_type = create_virtuallocation_model(model=model)
    return pydantic_type(model).schema_json()
