"""
Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online.

https://schema.org/EventMovedOnline
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EventMovedOnlineInheritedProperties(TypedDict):
    """Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online.

    References:
        https://schema.org/EventMovedOnline
    Note:
        Model Depth 6
    Attributes:
    """

    


class EventMovedOnlineProperties(TypedDict):
    """Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online.

    References:
        https://schema.org/EventMovedOnline
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EventMovedOnlineInheritedProperties , EventMovedOnlineProperties, TypedDict):
    pass


class EventMovedOnlineBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EventMovedOnline",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EventMovedOnlineProperties, EventMovedOnlineInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventMovedOnline"
    return model
    

EventMovedOnline = create_schema_org_model()


def create_eventmovedonline_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_eventmovedonline_model(model=model)
    return pydantic_type(model).schema_json()


