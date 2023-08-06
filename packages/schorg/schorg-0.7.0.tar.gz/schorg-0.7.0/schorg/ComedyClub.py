"""
A comedy club.

https://schema.org/ComedyClub
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ComedyClubInheritedProperties(TypedDict):
    """A comedy club.

    References:
        https://schema.org/ComedyClub
    Note:
        Model Depth 5
    Attributes:
    """

    


class ComedyClubProperties(TypedDict):
    """A comedy club.

    References:
        https://schema.org/ComedyClub
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ComedyClubInheritedProperties , ComedyClubProperties, TypedDict):
    pass


class ComedyClubBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ComedyClub",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ComedyClubProperties, ComedyClubInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComedyClub"
    return model
    

ComedyClub = create_schema_org_model()


def create_comedyclub_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_comedyclub_model(model=model)
    return pydantic_type(model).schema_json()


