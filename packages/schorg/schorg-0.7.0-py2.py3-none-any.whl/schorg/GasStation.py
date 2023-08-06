"""
A gas station.

https://schema.org/GasStation
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GasStationInheritedProperties(TypedDict):
    """A gas station.

    References:
        https://schema.org/GasStation
    Note:
        Model Depth 5
    Attributes:
    """

    


class GasStationProperties(TypedDict):
    """A gas station.

    References:
        https://schema.org/GasStation
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(GasStationInheritedProperties , GasStationProperties, TypedDict):
    pass


class GasStationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GasStation",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[GasStationProperties, GasStationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GasStation"
    return model
    

GasStation = create_schema_org_model()


def create_gasstation_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_gasstation_model(model=model)
    return pydantic_type(model).schema_json()


