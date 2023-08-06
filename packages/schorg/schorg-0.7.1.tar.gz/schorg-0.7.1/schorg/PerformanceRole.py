"""
A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.

https://schema.org/PerformanceRole
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PerformanceRoleInheritedProperties(TypedDict):
    """A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.

    References:
        https://schema.org/PerformanceRole
    Note:
        Model Depth 4
    Attributes:
        roleName: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named 'inker', 'penciller', and 'letterer'; or an athlete in a SportsTeam might play in the position named 'Quarterback'.
        namedPosition: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A position played, performed or filled by a person or organization, as part of an organization. For example, an athlete in a SportsTeam might play in the position named 'Quarterback'.
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    roleName: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    namedPosition: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    startDate: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    endDate: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    


class PerformanceRoleProperties(TypedDict):
    """A PerformanceRole is a Role that some entity places with regard to a theatrical performance, e.g. in a Movie, TVSeries etc.

    References:
        https://schema.org/PerformanceRole
    Note:
        Model Depth 4
    Attributes:
        characterName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The name of a character played in some acting or performing role, i.e. in a PerformanceRole.
    """

    characterName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(PerformanceRoleInheritedProperties , PerformanceRoleProperties, TypedDict):
    pass


class PerformanceRoleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PerformanceRole",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'roleName': {'exclude': True}}
        fields = {'namedPosition': {'exclude': True}}
        fields = {'startDate': {'exclude': True}}
        fields = {'endDate': {'exclude': True}}
        fields = {'characterName': {'exclude': True}}
        


def create_schema_org_model(type_: Union[PerformanceRoleProperties, PerformanceRoleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PerformanceRole"
    return model
    

PerformanceRole = create_schema_org_model()


def create_performancerole_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_performancerole_model(model=model)
    return pydantic_type(model).schema_json()


