"""
A city or town.

https://schema.org/City
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CityInheritedProperties(TypedDict):
    """A city or town.

    References:
        https://schema.org/City
    Note:
        Model Depth 4
    Attributes:
    """

    


class CityProperties(TypedDict):
    """A city or town.

    References:
        https://schema.org/City
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(CityInheritedProperties , CityProperties, TypedDict):
    pass


class CityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="City",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CityProperties, CityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "City"
    return model
    

City = create_schema_org_model()


def create_city_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_city_model(model=model)
    return pydantic_type(model).schema_json()


