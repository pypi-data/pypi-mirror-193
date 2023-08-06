"""
Indicates that the event was changed to allow online participation. See [[eventAttendanceMode]] for specifics of whether it is now fully or partially online.

https://schema.org/EventMovedOnline
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class EventMovedOnlineAllProperties(
    EventMovedOnlineInheritedProperties, EventMovedOnlineProperties, TypedDict
):
    pass


class EventMovedOnlineBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EventMovedOnline", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EventMovedOnlineProperties,
        EventMovedOnlineInheritedProperties,
        EventMovedOnlineAllProperties,
    ] = EventMovedOnlineAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventMovedOnline"
    return model


EventMovedOnline = create_schema_org_model()


def create_eventmovedonline_model(
    model: Union[
        EventMovedOnlineProperties,
        EventMovedOnlineInheritedProperties,
        EventMovedOnlineAllProperties,
    ]
):
    _type = deepcopy(EventMovedOnlineAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EventMovedOnlineAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EventMovedOnlineAllProperties):
    pydantic_type = create_eventmovedonline_model(model=model)
    return pydantic_type(model).schema_json()
