"""
A nightclub or discotheque.

https://schema.org/NightClub
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NightClubInheritedProperties(TypedDict):
    """A nightclub or discotheque.

    References:
        https://schema.org/NightClub
    Note:
        Model Depth 5
    Attributes:
    """

    


class NightClubProperties(TypedDict):
    """A nightclub or discotheque.

    References:
        https://schema.org/NightClub
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(NightClubInheritedProperties , NightClubProperties, TypedDict):
    pass


class NightClubBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="NightClub",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[NightClubProperties, NightClubInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NightClub"
    return model
    

NightClub = create_schema_org_model()


def create_nightclub_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_nightclub_model(model=model)
    return pydantic_type(model).schema_json()


