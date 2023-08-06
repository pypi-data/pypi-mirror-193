"""
Organization: Sports team.

https://schema.org/SportsTeam
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SportsTeamInheritedProperties(TypedDict):
    """Organization: Sports team.

    References:
        https://schema.org/SportsTeam
    Note:
        Model Depth 4
    Attributes:
        sport: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A type of sport (e.g. Baseball).
    """

    sport: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    


class SportsTeamProperties(TypedDict):
    """Organization: Sports team.

    References:
        https://schema.org/SportsTeam
    Note:
        Model Depth 4
    Attributes:
        athlete: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person that acts as performing member of a sports team; a player as opposed to a coach.
        gender: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Gender of something, typically a [[Person]], but possibly also fictional characters, animals, etc. While https://schema.org/Male and https://schema.org/Female may be used, text strings are also acceptable for people who do not identify as a binary gender. The [[gender]] property can also be used in an extended sense to cover e.g. the gender of sports teams. As with the gender of individuals, we do not try to enumerate all possibilities. A mixed-gender [[SportsTeam]] can be indicated with a text value of "Mixed".
        coach: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person that acts in a coaching role for a sports team.
    """

    athlete: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gender: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    coach: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(SportsTeamInheritedProperties , SportsTeamProperties, TypedDict):
    pass


class SportsTeamBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SportsTeam",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'sport': {'exclude': True}}
        fields = {'athlete': {'exclude': True}}
        fields = {'gender': {'exclude': True}}
        fields = {'coach': {'exclude': True}}
        


def create_schema_org_model(type_: Union[SportsTeamProperties, SportsTeamInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SportsTeam"
    return model
    

SportsTeam = create_schema_org_model()


def create_sportsteam_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_sportsteam_model(model=model)
    return pydantic_type(model).schema_json()


