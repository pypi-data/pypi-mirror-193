"""
The event has been postponed and no new date has been set. The event's previousStartDate should be set.

https://schema.org/EventPostponed
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EventPostponedInheritedProperties(TypedDict):
    """The event has been postponed and no new date has been set. The event's previousStartDate should be set.

    References:
        https://schema.org/EventPostponed
    Note:
        Model Depth 6
    Attributes:
    """

    


class EventPostponedProperties(TypedDict):
    """The event has been postponed and no new date has been set. The event's previousStartDate should be set.

    References:
        https://schema.org/EventPostponed
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EventPostponedInheritedProperties , EventPostponedProperties, TypedDict):
    pass


class EventPostponedBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EventPostponed",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EventPostponedProperties, EventPostponedInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventPostponed"
    return model
    

EventPostponed = create_schema_org_model()


def create_eventpostponed_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_eventpostponed_model(model=model)
    return pydantic_type(model).schema_json()


