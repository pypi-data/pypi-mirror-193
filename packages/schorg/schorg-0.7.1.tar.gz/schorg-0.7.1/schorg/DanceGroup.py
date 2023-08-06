"""
A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

https://schema.org/DanceGroup
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DanceGroupInheritedProperties(TypedDict):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

    References:
        https://schema.org/DanceGroup
    Note:
        Model Depth 4
    Attributes:
    """

    


class DanceGroupProperties(TypedDict):
    """A dance group&#x2014;for example, the Alvin Ailey Dance Theater or Riverdance.

    References:
        https://schema.org/DanceGroup
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(DanceGroupInheritedProperties , DanceGroupProperties, TypedDict):
    pass


class DanceGroupBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DanceGroup",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DanceGroupProperties, DanceGroupInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DanceGroup"
    return model
    

DanceGroup = create_schema_org_model()


def create_dancegroup_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_dancegroup_model(model=model)
    return pydantic_type(model).schema_json()


