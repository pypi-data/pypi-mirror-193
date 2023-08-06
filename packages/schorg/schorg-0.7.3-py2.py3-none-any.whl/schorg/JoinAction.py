"""
An agent joins an event/group with participants/friends at a location.Related actions:* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team of people.* [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply that you'll be receiving updates.* [[FollowAction]]: Unlike FollowAction, JoinAction does not imply that you'll be polling for updates.

https://schema.org/JoinAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class JoinActionInheritedProperties(TypedDict):
    """An agent joins an event/group with participants/friends at a location.Related actions:* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team of people.* [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply that you'll be receiving updates.* [[FollowAction]]: Unlike FollowAction, JoinAction does not imply that you'll be polling for updates.

    References:
        https://schema.org/JoinAction
    Note:
        Model Depth 4
    Attributes:
    """


class JoinActionProperties(TypedDict):
    """An agent joins an event/group with participants/friends at a location.Related actions:* [[RegisterAction]]: Unlike RegisterAction, JoinAction refers to joining a group/team of people.* [[SubscribeAction]]: Unlike SubscribeAction, JoinAction does not imply that you'll be receiving updates.* [[FollowAction]]: Unlike FollowAction, JoinAction does not imply that you'll be polling for updates.

    References:
        https://schema.org/JoinAction
    Note:
        Model Depth 4
    Attributes:
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
    """

    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class JoinActionAllProperties(
    JoinActionInheritedProperties, JoinActionProperties, TypedDict
):
    pass


class JoinActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="JoinAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"event": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        JoinActionProperties, JoinActionInheritedProperties, JoinActionAllProperties
    ] = JoinActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "JoinAction"
    return model


JoinAction = create_schema_org_model()


def create_joinaction_model(
    model: Union[
        JoinActionProperties, JoinActionInheritedProperties, JoinActionAllProperties
    ]
):
    _type = deepcopy(JoinActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: JoinActionAllProperties):
    pydantic_type = create_joinaction_model(model=model)
    return pydantic_type(model).schema_json()
