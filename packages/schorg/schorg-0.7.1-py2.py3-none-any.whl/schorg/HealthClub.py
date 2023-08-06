"""
A health club.

https://schema.org/HealthClub
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthClubInheritedProperties(TypedDict):
    """A health club.

    References:
        https://schema.org/HealthClub
    Note:
        Model Depth 5
    Attributes:
    """

    


class HealthClubProperties(TypedDict):
    """A health club.

    References:
        https://schema.org/HealthClub
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HealthClubInheritedProperties , HealthClubProperties, TypedDict):
    pass


class HealthClubBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HealthClub",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HealthClubProperties, HealthClubInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthClub"
    return model
    

HealthClub = create_schema_org_model()


def create_healthclub_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_healthclub_model(model=model)
    return pydantic_type(model).schema_json()


