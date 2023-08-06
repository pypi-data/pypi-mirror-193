"""
The event has been rescheduled. The event's previousStartDate should be set to the old date and the startDate should be set to the event's new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated.)

https://schema.org/EventRescheduled
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EventRescheduledInheritedProperties(TypedDict):
    """The event has been rescheduled. The event's previousStartDate should be set to the old date and the startDate should be set to the event's new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated.)

    References:
        https://schema.org/EventRescheduled
    Note:
        Model Depth 6
    Attributes:
    """


class EventRescheduledProperties(TypedDict):
    """The event has been rescheduled. The event's previousStartDate should be set to the old date and the startDate should be set to the event's new date. (If the event has been rescheduled multiple times, the previousStartDate property may be repeated.)

    References:
        https://schema.org/EventRescheduled
    Note:
        Model Depth 6
    Attributes:
    """


class EventRescheduledAllProperties(
    EventRescheduledInheritedProperties, EventRescheduledProperties, TypedDict
):
    pass


class EventRescheduledBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EventRescheduled", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EventRescheduledProperties,
        EventRescheduledInheritedProperties,
        EventRescheduledAllProperties,
    ] = EventRescheduledAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventRescheduled"
    return model


EventRescheduled = create_schema_org_model()


def create_eventrescheduled_model(
    model: Union[
        EventRescheduledProperties,
        EventRescheduledInheritedProperties,
        EventRescheduledAllProperties,
    ]
):
    _type = deepcopy(EventRescheduledAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EventRescheduledAllProperties):
    pydantic_type = create_eventrescheduled_model(model=model)
    return pydantic_type(model).schema_json()
