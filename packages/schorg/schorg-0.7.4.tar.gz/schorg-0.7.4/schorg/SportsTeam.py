"""
Organization: Sports team.

https://schema.org/SportsTeam
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SportsTeamInheritedProperties(TypedDict):
    """Organization: Sports team.

    References:
        https://schema.org/SportsTeam
    Note:
        Model Depth 4
    Attributes:
        sport: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A type of sport (e.g. Baseball).
    """

    sport: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class SportsTeamProperties(TypedDict):
    """Organization: Sports team.

    References:
        https://schema.org/SportsTeam
    Note:
        Model Depth 4
    Attributes:
        athlete: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person that acts as performing member of a sports team; a player as opposed to a coach.
        gender: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Gender of something, typically a [[Person]], but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who do not identify as a binary gender. The [[gender]] property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender [[SportsTeam]] can be indicated with a text value of "Mixed".
        coach: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person that acts in a coaching role for a sports team.
    """

    athlete: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gender: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    coach: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class SportsTeamAllProperties(
    SportsTeamInheritedProperties, SportsTeamProperties, TypedDict
):
    pass


class SportsTeamBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SportsTeam", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"sport": {"exclude": True}}
        fields = {"athlete": {"exclude": True}}
        fields = {"gender": {"exclude": True}}
        fields = {"coach": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SportsTeamProperties, SportsTeamInheritedProperties, SportsTeamAllProperties
    ] = SportsTeamAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SportsTeam"
    return model


SportsTeam = create_schema_org_model()


def create_sportsteam_model(
    model: Union[
        SportsTeamProperties, SportsTeamInheritedProperties, SportsTeamAllProperties
    ]
):
    _type = deepcopy(SportsTeamAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SportsTeamAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SportsTeamAllProperties):
    pydantic_type = create_sportsteam_model(model=model)
    return pydantic_type(model).schema_json()
