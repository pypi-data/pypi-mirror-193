"""
A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.

https://schema.org/TheaterGroup
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TheaterGroupInheritedProperties(TypedDict):
    """A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.

    References:
        https://schema.org/TheaterGroup
    Note:
        Model Depth 4
    Attributes:
    """

    


class TheaterGroupProperties(TypedDict):
    """A theater group or company, for example, the Royal Shakespeare Company or Druid Theatre.

    References:
        https://schema.org/TheaterGroup
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(TheaterGroupInheritedProperties , TheaterGroupProperties, TypedDict):
    pass


class TheaterGroupBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TheaterGroup",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TheaterGroupProperties, TheaterGroupInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TheaterGroup"
    return model
    

TheaterGroup = create_schema_org_model()


def create_theatergroup_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_theatergroup_model(model=model)
    return pydantic_type(model).schema_json()


