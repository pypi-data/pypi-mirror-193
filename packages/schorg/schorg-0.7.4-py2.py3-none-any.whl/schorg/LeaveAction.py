"""
An agent leaves an event / group with participants/friends at a location.Related actions:* [[JoinAction]]: The antonym of LeaveAction.* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.

https://schema.org/LeaveAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LeaveActionInheritedProperties(TypedDict):
    """An agent leaves an event / group with participants/friends at a location.Related actions:* [[JoinAction]]: The antonym of LeaveAction.* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.

    References:
        https://schema.org/LeaveAction
    Note:
        Model Depth 4
    Attributes:
    """


class LeaveActionProperties(TypedDict):
    """An agent leaves an event / group with participants/friends at a location.Related actions:* [[JoinAction]]: The antonym of LeaveAction.* [[UnRegisterAction]]: Unlike UnRegisterAction, LeaveAction implies leaving a group/team of people rather than a service.

    References:
        https://schema.org/LeaveAction
    Note:
        Model Depth 4
    Attributes:
        event: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Upcoming or past event associated with this place, organization, or action.
    """

    event: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class LeaveActionAllProperties(
    LeaveActionInheritedProperties, LeaveActionProperties, TypedDict
):
    pass


class LeaveActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LeaveAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"event": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        LeaveActionProperties, LeaveActionInheritedProperties, LeaveActionAllProperties
    ] = LeaveActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LeaveAction"
    return model


LeaveAction = create_schema_org_model()


def create_leaveaction_model(
    model: Union[
        LeaveActionProperties, LeaveActionInheritedProperties, LeaveActionAllProperties
    ]
):
    _type = deepcopy(LeaveActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of LeaveActionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LeaveActionAllProperties):
    pydantic_type = create_leaveaction_model(model=model)
    return pydantic_type(model).schema_json()
