"""
A subclass of Role used to describe roles within organizations.

https://schema.org/OrganizationRole
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrganizationRoleInheritedProperties(TypedDict):
    """A subclass of Role used to describe roles within organizations.

    References:
        https://schema.org/OrganizationRole
    Note:
        Model Depth 4
    Attributes:
        roleName: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named 'inker', 'penciller', and 'letterer'; or an athlete in a SportsTeam might play in the position named 'Quarterback'.
        namedPosition: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A position played, performed or filled by a person or organization, as part of an organization. For example, an athlete in a SportsTeam might play in the position named 'Quarterback'.
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    roleName: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    namedPosition: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]


class OrganizationRoleProperties(TypedDict):
    """A subclass of Role used to describe roles within organizations.

    References:
        https://schema.org/OrganizationRole
    Note:
        Model Depth 4
    Attributes:
        numberedPosition: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): A number associated with a role in an organization, for example, the number on an athlete's jersey.
    """

    numberedPosition: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class OrganizationRoleAllProperties(
    OrganizationRoleInheritedProperties, OrganizationRoleProperties, TypedDict
):
    pass


class OrganizationRoleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OrganizationRole", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"roleName": {"exclude": True}}
        fields = {"namedPosition": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}
        fields = {"numberedPosition": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OrganizationRoleProperties,
        OrganizationRoleInheritedProperties,
        OrganizationRoleAllProperties,
    ] = OrganizationRoleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrganizationRole"
    return model


OrganizationRole = create_schema_org_model()


def create_organizationrole_model(
    model: Union[
        OrganizationRoleProperties,
        OrganizationRoleInheritedProperties,
        OrganizationRoleAllProperties,
    ]
):
    _type = deepcopy(OrganizationRoleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OrganizationRole. Please see: https://schema.org/OrganizationRole"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OrganizationRoleAllProperties):
    pydantic_type = create_organizationrole_model(model=model)
    return pydantic_type(model).schema_json()
