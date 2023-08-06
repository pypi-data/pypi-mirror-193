"""
The event is taking place or has taken place on the startDate as scheduled. Use of this value is optional, as it is assumed by default.

https://schema.org/EventScheduled
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(EventScheduledInheritedProperties , EventScheduledProperties, TypedDict):
    pass


class EventScheduledBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EventScheduled",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EventScheduledProperties, EventScheduledInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventScheduled"
    return model
    

EventScheduled = create_schema_org_model()


def create_eventscheduled_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_eventscheduled_model(model=model)
    return pydantic_type(model).schema_json()


