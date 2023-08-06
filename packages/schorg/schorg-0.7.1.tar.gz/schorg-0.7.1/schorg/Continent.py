"""
One of the continents (for example, Europe or Africa).

https://schema.org/Continent
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ContinentInheritedProperties(TypedDict):
    """One of the continents (for example, Europe or Africa).

    References:
        https://schema.org/Continent
    Note:
        Model Depth 4
    Attributes:
    """

    


class ContinentProperties(TypedDict):
    """One of the continents (for example, Europe or Africa).

    References:
        https://schema.org/Continent
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ContinentInheritedProperties , ContinentProperties, TypedDict):
    pass


class ContinentBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Continent",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ContinentProperties, ContinentInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Continent"
    return model
    

Continent = create_schema_org_model()


def create_continent_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_continent_model(model=model)
    return pydantic_type(model).schema_json()


