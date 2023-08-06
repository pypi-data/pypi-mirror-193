"""
The act of notifying an event organizer as to whether you expect to attend the event.

https://schema.org/RsvpAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RsvpActionInheritedProperties(TypedDict):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    References:
        https://schema.org/RsvpAction
    Note:
        Model Depth 6
    Attributes:
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
    """

    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class RsvpActionProperties(TypedDict):
    """The act of notifying an event organizer as to whether you expect to attend the event.

    References:
        https://schema.org/RsvpAction
    Note:
        Model Depth 6
    Attributes:
        additionalNumberOfGuests: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): If responding yes, the number of guests who will attend in addition to the invitee.
        comment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Comments, typically from users.
        rsvpResponse: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The response (yes, no, maybe) to the RSVP.
    """

    additionalNumberOfGuests: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    comment: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    rsvpResponse: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class RsvpActionAllProperties(
    RsvpActionInheritedProperties, RsvpActionProperties, TypedDict
):
    pass


class RsvpActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RsvpAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"event": {"exclude": True}}
        fields = {"additionalNumberOfGuests": {"exclude": True}}
        fields = {"comment": {"exclude": True}}
        fields = {"rsvpResponse": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RsvpActionProperties, RsvpActionInheritedProperties, RsvpActionAllProperties
    ] = RsvpActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RsvpAction"
    return model


RsvpAction = create_schema_org_model()


def create_rsvpaction_model(
    model: Union[
        RsvpActionProperties, RsvpActionInheritedProperties, RsvpActionAllProperties
    ]
):
    _type = deepcopy(RsvpActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of RsvpAction. Please see: https://schema.org/RsvpAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: RsvpActionAllProperties):
    pydantic_type = create_rsvpaction_model(model=model)
    return pydantic_type(model).schema_json()
