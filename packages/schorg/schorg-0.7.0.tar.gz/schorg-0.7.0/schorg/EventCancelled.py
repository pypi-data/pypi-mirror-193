"""
The event has been cancelled. If the event has multiple startDate values, all are assumed to be cancelled. Either startDate or previousStartDate may be used to specify the event's cancelled date(s).

https://schema.org/EventCancelled
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(EventCancelledInheritedProperties , EventCancelledProperties, TypedDict):
    pass


class EventCancelledBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EventCancelled",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EventCancelledProperties, EventCancelledInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventCancelled"
    return model
    

EventCancelled = create_schema_org_model()


def create_eventcancelled_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_eventcancelled_model(model=model)
    return pydantic_type(model).schema_json()


