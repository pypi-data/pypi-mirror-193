"""
The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default.

https://schema.org/EventScheduled
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EventScheduledInheritedProperties(TypedDict):
    """The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default.

    References:
        https://schema.org/EventScheduled
    Note:
        Model Depth 6
    Attributes:
    """


class EventScheduledProperties(TypedDict):
    """The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default.

    References:
        https://schema.org/EventScheduled
    Note:
        Model Depth 6
    Attributes:
    """


class EventScheduledAllProperties(
    EventScheduledInheritedProperties, EventScheduledProperties, TypedDict
):
    pass


class EventScheduledBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EventScheduled", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EventScheduledProperties,
        EventScheduledInheritedProperties,
        EventScheduledAllProperties,
    ] = EventScheduledAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventScheduled"
    return model


EventScheduled = create_schema_org_model()


def create_eventscheduled_model(
    model: Union[
        EventScheduledProperties,
        EventScheduledInheritedProperties,
        EventScheduledAllProperties,
    ]
):
    _type = deepcopy(EventScheduledAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EventScheduled. Please see: https://schema.org/EventScheduled"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EventScheduledAllProperties):
    pydantic_type = create_eventscheduled_model(model=model)
    return pydantic_type(model).schema_json()
