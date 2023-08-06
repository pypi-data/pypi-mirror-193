"""
Reserving a concrete object.Related actions:* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.

https://schema.org/ReserveAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReserveActionInheritedProperties(TypedDict):
    """Reserving a concrete object.Related actions:* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.

    References:
        https://schema.org/ReserveAction
    Note:
        Model Depth 5
    Attributes:
        scheduledTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The time the object is scheduled to.
    """

    scheduledTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    


class ReserveActionProperties(TypedDict):
    """Reserving a concrete object.Related actions:* [[ScheduleAction]]: Unlike ScheduleAction, ReserveAction reserves concrete objects (e.g. a table, a hotel) towards a time slot / spatial allocation.

    References:
        https://schema.org/ReserveAction
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ReserveActionInheritedProperties , ReserveActionProperties, TypedDict):
    pass


class ReserveActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReserveAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'scheduledTime': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ReserveActionProperties, ReserveActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReserveAction"
    return model
    

ReserveAction = create_schema_org_model()


def create_reserveaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reserveaction_model(model=model)
    return pydantic_type(model).schema_json()


