"""
Used to describe membership in a loyalty programs (e.g. "StarAliance"), traveler clubs (e.g. "AAA"), purchase clubs ("Safeway Club"), etc.

https://schema.org/ProgramMembership
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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
        member: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.
        hostingOrganization: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The organization (airline, travelers' club, etc.) the membership is made with.
        membershipNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A unique identifier for the membership.
        members: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A member of this organization.
        membershipPointsEarned: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The number of membership points earned by the member. If necessary, the unitText can be used to express the units the points are issued in. (E.g. stars, miles, etc.)
        programName: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The program providing the membership.
    """

    member: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hostingOrganization: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    membershipNumber: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    members: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    membershipPointsEarned: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    programName: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ProgramMembershipAllProperties(
    ProgramMembershipInheritedProperties, ProgramMembershipProperties, TypedDict
):
    pass


class ProgramMembershipBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ProgramMembership", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"member": {"exclude": True}}
        fields = {"hostingOrganization": {"exclude": True}}
        fields = {"membershipNumber": {"exclude": True}}
        fields = {"members": {"exclude": True}}
        fields = {"membershipPointsEarned": {"exclude": True}}
        fields = {"programName": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ProgramMembershipProperties,
        ProgramMembershipInheritedProperties,
        ProgramMembershipAllProperties,
    ] = ProgramMembershipAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ProgramMembership"
    return model


ProgramMembership = create_schema_org_model()


def create_programmembership_model(
    model: Union[
        ProgramMembershipProperties,
        ProgramMembershipInheritedProperties,
        ProgramMembershipAllProperties,
    ]
):
    _type = deepcopy(ProgramMembershipAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ProgramMembershipAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ProgramMembershipAllProperties):
    pydantic_type = create_programmembership_model(model=model)
    return pydantic_type(model).schema_json()
