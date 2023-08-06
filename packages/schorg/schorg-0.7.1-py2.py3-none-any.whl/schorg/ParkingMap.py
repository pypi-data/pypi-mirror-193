"""
A parking map.

https://schema.org/ParkingMap
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ParkingMapInheritedProperties , ParkingMapProperties, TypedDict):
    pass


class ParkingMapBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ParkingMap",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ParkingMapProperties, ParkingMapInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ParkingMap"
    return model
    

ParkingMap = create_schema_org_model()


def create_parkingmap_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_parkingmap_model(model=model)
    return pydantic_type(model).schema_json()


