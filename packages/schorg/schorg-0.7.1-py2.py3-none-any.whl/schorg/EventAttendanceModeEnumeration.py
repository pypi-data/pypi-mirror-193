"""
An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline.

https://schema.org/EventAttendanceModeEnumeration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EventAttendanceModeEnumerationInheritedProperties(TypedDict):
    """An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline.

    References:
        https://schema.org/EventAttendanceModeEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class EventAttendanceModeEnumerationProperties(TypedDict):
    """An EventAttendanceModeEnumeration value is one of potentially several modes of organising an event, relating to whether it is online or offline.

    References:
        https://schema.org/EventAttendanceModeEnumeration
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(EventAttendanceModeEnumerationInheritedProperties , EventAttendanceModeEnumerationProperties, TypedDict):
    pass


class EventAttendanceModeEnumerationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EventAttendanceModeEnumeration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[EventAttendanceModeEnumerationProperties, EventAttendanceModeEnumerationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventAttendanceModeEnumeration"
    return model
    

EventAttendanceModeEnumeration = create_schema_org_model()


def create_eventattendancemodeenumeration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_eventattendancemodeenumeration_model(model=model)
    return pydantic_type(model).schema_json()


