"""
A city hall.

https://schema.org/CityHall
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CityHallInheritedProperties(TypedDict):
    """A city hall.

    References:
        https://schema.org/CityHall
    Note:
        Model Depth 5
    Attributes:
    """

    


class CityHallProperties(TypedDict):
    """A city hall.

    References:
        https://schema.org/CityHall
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(CityHallInheritedProperties , CityHallProperties, TypedDict):
    pass


class CityHallBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CityHall",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CityHallProperties, CityHallInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CityHall"
    return model
    

CityHall = create_schema_org_model()


def create_cityhall_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_cityhall_model(model=model)
    return pydantic_type(model).schema_json()


