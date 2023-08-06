"""
A Role that represents a Web link, e.g. as expressed via the 'url' property. Its linkRelationship property can indicate URL-based and plain textual link types, e.g. those in IANA link registry or others such as 'amphtml'. This structure provides a placeholder where details from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds.

https://schema.org/LinkRole
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LinkRoleInheritedProperties(TypedDict):
    """A Role that represents a Web link, e.g. as expressed via the 'url' property. Its linkRelationship property can indicate URL-based and plain textual link types, e.g. those in IANA link registry or others such as 'amphtml'. This structure provides a placeholder where details from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds.

    References:
        https://schema.org/LinkRole
    Note:
        Model Depth 4
    Attributes:
        roleName: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named 'inker', 'penciller', and 'letterer'; or an athlete in a SportsTeam might play in the position named 'Quarterback'.
        namedPosition: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A position played, performed or filled by a person or organization, as part of an organization. For example, an athlete in a SportsTeam might play in the position named 'Quarterback'.
        startDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    roleName: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    namedPosition: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]


class LinkRoleProperties(TypedDict):
    """A Role that represents a Web link, e.g. as expressed via the 'url' property. Its linkRelationship property can indicate URL-based and plain textual link types, e.g. those in IANA link registry or others such as 'amphtml'. This structure provides a placeholder where details from HTML's link element can be represented outside of HTML, e.g. in JSON-LD feeds.

    References:
        https://schema.org/LinkRole
    Note:
        Model Depth 4
    Attributes:
        linkRelationship: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the relationship type of a Web link.
        inLanguage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
    """

    linkRelationship: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    inLanguage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class LinkRoleAllProperties(LinkRoleInheritedProperties, LinkRoleProperties, TypedDict):
    pass


class LinkRoleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LinkRole", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"roleName": {"exclude": True}}
        fields = {"namedPosition": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}
        fields = {"linkRelationship": {"exclude": True}}
        fields = {"inLanguage": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        LinkRoleProperties, LinkRoleInheritedProperties, LinkRoleAllProperties
    ] = LinkRoleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LinkRole"
    return model


LinkRole = create_schema_org_model()


def create_linkrole_model(
    model: Union[LinkRoleProperties, LinkRoleInheritedProperties, LinkRoleAllProperties]
):
    _type = deepcopy(LinkRoleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LinkRoleAllProperties):
    pydantic_type = create_linkrole_model(model=model)
    return pydantic_type(model).schema_json()
