"""
Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.

https://schema.org/ProgramMembership
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ProgramMembershipInheritedProperties(TypedDict):
    """Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.

    References:
        https://schema.org/ProgramMembership
    Note:
        Model Depth 3
    Attributes:
    """

    


class ProgramMembershipProperties(TypedDict):
    """Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.

    References:
        https://schema.org/ProgramMembership
    Note:
        Model Depth 3
    Attributes:
        member: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.
        hostingOrganization: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The organization (airline, travelers' club, etc.) the membership is made with.
        membershipNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A unique identifier for the membership.
        members: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A member of this organization.
        membershipPointsEarned: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of membership points earned by the member. If necessary, the unitText can be used to express the units the points are issued in. (E.g. stars, miles, etc.)
        programName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The program providing the membership.
    """

    member: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hostingOrganization: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    membershipNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    members: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    membershipPointsEarned: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    programName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(ProgramMembershipInheritedProperties , ProgramMembershipProperties, TypedDict):
    pass


class ProgramMembershipBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ProgramMembership",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'member': {'exclude': True}}
        fields = {'hostingOrganization': {'exclude': True}}
        fields = {'membershipNumber': {'exclude': True}}
        fields = {'members': {'exclude': True}}
        fields = {'membershipPointsEarned': {'exclude': True}}
        fields = {'programName': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ProgramMembershipProperties, ProgramMembershipInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ProgramMembership"
    return model
    

ProgramMembership = create_schema_org_model()


def create_programmembership_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_programmembership_model(model=model)
    return pydantic_type(model).schema_json()


