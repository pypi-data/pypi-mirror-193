"""
Scheduling future actions, events, or tasks.Related actions:* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.

https://schema.org/ScheduleAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ScheduleActionInheritedProperties(TypedDict):
    """Scheduling future actions, events, or tasks.Related actions:* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.

    References:
        https://schema.org/ScheduleAction
    Note:
        Model Depth 5
    Attributes:
        scheduledTime: (Optional[Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]]): The time the object is scheduled to.
    """

    scheduledTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]
    ]


class ScheduleActionProperties(TypedDict):
    """Scheduling future actions, events, or tasks.Related actions:* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.

    References:
        https://schema.org/ScheduleAction
    Note:
        Model Depth 5
    Attributes:
    """


class ScheduleActionAllProperties(
    ScheduleActionInheritedProperties, ScheduleActionProperties, TypedDict
):
    pass


class ScheduleActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ScheduleAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"scheduledTime": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ScheduleActionProperties,
        ScheduleActionInheritedProperties,
        ScheduleActionAllProperties,
    ] = ScheduleActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ScheduleAction"
    return model


ScheduleAction = create_schema_org_model()


def create_scheduleaction_model(
    model: Union[
        ScheduleActionProperties,
        ScheduleActionInheritedProperties,
        ScheduleActionAllProperties,
    ]
):
    _type = deepcopy(ScheduleActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ScheduleAction. Please see: https://schema.org/ScheduleAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ScheduleActionAllProperties):
    pydantic_type = create_scheduleaction_model(model=model)
    return pydantic_type(model).schema_json()
