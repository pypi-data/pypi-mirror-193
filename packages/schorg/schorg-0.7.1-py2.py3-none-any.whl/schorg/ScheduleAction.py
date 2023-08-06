"""
Scheduling future actions, events, or tasks.Related actions:* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.

https://schema.org/ScheduleAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ScheduleActionInheritedProperties(TypedDict):
    """Scheduling future actions, events, or tasks.Related actions:* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.

    References:
        https://schema.org/ScheduleAction
    Note:
        Model Depth 5
    Attributes:
        scheduledTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The time the object is scheduled to.
    """

    scheduledTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    


class ScheduleActionProperties(TypedDict):
    """Scheduling future actions, events, or tasks.Related actions:* [[ReserveAction]]: Unlike ReserveAction, ScheduleAction allocates future actions (e.g. an event, a task, etc) towards a time slot / spatial allocation.

    References:
        https://schema.org/ScheduleAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ScheduleActionInheritedProperties , ScheduleActionProperties, TypedDict):
    pass


class ScheduleActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ScheduleAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'scheduledTime': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ScheduleActionProperties, ScheduleActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ScheduleAction"
    return model
    

ScheduleAction = create_schema_org_model()


def create_scheduleaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_scheduleaction_model(model=model)
    return pydantic_type(model).schema_json()


