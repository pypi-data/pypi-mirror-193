"""
RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.

https://schema.org/RsvpResponseType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RsvpResponseTypeInheritedProperties(TypedDict):
    """RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.

    References:
        https://schema.org/RsvpResponseType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class RsvpResponseTypeProperties(TypedDict):
    """RsvpResponseType is an enumeration type whose instances represent responding to an RSVP request.

    References:
        https://schema.org/RsvpResponseType
    Note:
        Model Depth 4
    Attributes:
    """


class RsvpResponseTypeAllProperties(
    RsvpResponseTypeInheritedProperties, RsvpResponseTypeProperties, TypedDict
):
    pass


class RsvpResponseTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RsvpResponseType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RsvpResponseTypeProperties,
        RsvpResponseTypeInheritedProperties,
        RsvpResponseTypeAllProperties,
    ] = RsvpResponseTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RsvpResponseType"
    return model


RsvpResponseType = create_schema_org_model()


def create_rsvpresponsetype_model(
    model: Union[
        RsvpResponseTypeProperties,
        RsvpResponseTypeInheritedProperties,
        RsvpResponseTypeAllProperties,
    ]
):
    _type = deepcopy(RsvpResponseTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RsvpResponseTypeAllProperties):
    pydantic_type = create_rsvpresponsetype_model(model=model)
    return pydantic_type(model).schema_json()
