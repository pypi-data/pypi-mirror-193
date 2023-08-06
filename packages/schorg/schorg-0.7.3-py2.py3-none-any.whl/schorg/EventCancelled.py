"""
The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event's cancelled date(s).

https://schema.org/EventCancelled
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EventCancelledInheritedProperties(TypedDict):
    """The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event's cancelled date(s).

    References:
        https://schema.org/EventCancelled
    Note:
        Model Depth 6
    Attributes:
    """


class EventCancelledProperties(TypedDict):
    """The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event's cancelled date(s).

    References:
        https://schema.org/EventCancelled
    Note:
        Model Depth 6
    Attributes:
    """


class EventCancelledAllProperties(
    EventCancelledInheritedProperties, EventCancelledProperties, TypedDict
):
    pass


class EventCancelledBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EventCancelled", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EventCancelledProperties,
        EventCancelledInheritedProperties,
        EventCancelledAllProperties,
    ] = EventCancelledAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventCancelled"
    return model


EventCancelled = create_schema_org_model()


def create_eventcancelled_model(
    model: Union[
        EventCancelledProperties,
        EventCancelledInheritedProperties,
        EventCancelledAllProperties,
    ]
):
    _type = deepcopy(EventCancelledAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EventCancelledAllProperties):
    pydantic_type = create_eventcancelled_model(model=model)
    return pydantic_type(model).schema_json()
