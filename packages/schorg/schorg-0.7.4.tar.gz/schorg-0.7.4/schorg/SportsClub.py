"""
A sports club.

https://schema.org/SportsClub
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SportsClubInheritedProperties(TypedDict):
    """A sports club.

    References:
        https://schema.org/SportsClub
    Note:
        Model Depth 5
    Attributes:
    """


class SportsClubProperties(TypedDict):
    """A sports club.

    References:
        https://schema.org/SportsClub
    Note:
        Model Depth 5
    Attributes:
    """


class SportsClubAllProperties(
    SportsClubInheritedProperties, SportsClubProperties, TypedDict
):
    pass


class SportsClubBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SportsClub", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SportsClubProperties, SportsClubInheritedProperties, SportsClubAllProperties
    ] = SportsClubAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SportsClub"
    return model


SportsClub = create_schema_org_model()


def create_sportsclub_model(
    model: Union[
        SportsClubProperties, SportsClubInheritedProperties, SportsClubAllProperties
    ]
):
    _type = deepcopy(SportsClubAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SportsClubAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SportsClubAllProperties):
    pydantic_type = create_sportsclub_model(model=model)
    return pydantic_type(model).schema_json()
