"""
EventStatusType is an enumeration type whose instances represent several states that an Event may be in.

https://schema.org/EventStatusType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EventStatusTypeInheritedProperties(TypedDict):
    """EventStatusType is an enumeration type whose instances represent several states that an Event may be in.

    References:
        https://schema.org/EventStatusType
    Note:
        Model Depth 5
    Attributes:
    """


class EventStatusTypeProperties(TypedDict):
    """EventStatusType is an enumeration type whose instances represent several states that an Event may be in.

    References:
        https://schema.org/EventStatusType
    Note:
        Model Depth 5
    Attributes:
    """


class EventStatusTypeAllProperties(
    EventStatusTypeInheritedProperties, EventStatusTypeProperties, TypedDict
):
    pass


class EventStatusTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EventStatusType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EventStatusTypeProperties,
        EventStatusTypeInheritedProperties,
        EventStatusTypeAllProperties,
    ] = EventStatusTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EventStatusType"
    return model


EventStatusType = create_schema_org_model()


def create_eventstatustype_model(
    model: Union[
        EventStatusTypeProperties,
        EventStatusTypeInheritedProperties,
        EventStatusTypeAllProperties,
    ]
):
    _type = deepcopy(EventStatusTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EventStatusTypeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EventStatusTypeAllProperties):
    pydantic_type = create_eventstatustype_model(model=model)
    return pydantic_type(model).schema_json()
