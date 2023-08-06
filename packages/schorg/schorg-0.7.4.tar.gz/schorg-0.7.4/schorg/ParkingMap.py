"""
A parking map.

https://schema.org/ParkingMap
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ParkingMapInheritedProperties(TypedDict):
    """A parking map.

    References:
        https://schema.org/ParkingMap
    Note:
        Model Depth 5
    Attributes:
    """


class ParkingMapProperties(TypedDict):
    """A parking map.

    References:
        https://schema.org/ParkingMap
    Note:
        Model Depth 5
    Attributes:
    """


class ParkingMapAllProperties(
    ParkingMapInheritedProperties, ParkingMapProperties, TypedDict
):
    pass


class ParkingMapBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ParkingMap", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ParkingMapProperties, ParkingMapInheritedProperties, ParkingMapAllProperties
    ] = ParkingMapAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ParkingMap"
    return model


ParkingMap = create_schema_org_model()


def create_parkingmap_model(
    model: Union[
        ParkingMapProperties, ParkingMapInheritedProperties, ParkingMapAllProperties
    ]
):
    _type = deepcopy(ParkingMapAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ParkingMapAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ParkingMapAllProperties):
    pydantic_type = create_parkingmap_model(model=model)
    return pydantic_type(model).schema_json()
