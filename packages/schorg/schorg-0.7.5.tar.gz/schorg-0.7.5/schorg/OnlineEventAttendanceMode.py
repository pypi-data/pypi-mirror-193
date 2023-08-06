"""
OnlineEventAttendanceMode - an event that is primarily conducted online. 

https://schema.org/OnlineEventAttendanceMode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnlineEventAttendanceModeInheritedProperties(TypedDict):
    """OnlineEventAttendanceMode - an event that is primarily conducted online.

    References:
        https://schema.org/OnlineEventAttendanceMode
    Note:
        Model Depth 5
    Attributes:
    """


class OnlineEventAttendanceModeProperties(TypedDict):
    """OnlineEventAttendanceMode - an event that is primarily conducted online.

    References:
        https://schema.org/OnlineEventAttendanceMode
    Note:
        Model Depth 5
    Attributes:
    """


class OnlineEventAttendanceModeAllProperties(
    OnlineEventAttendanceModeInheritedProperties,
    OnlineEventAttendanceModeProperties,
    TypedDict,
):
    pass


class OnlineEventAttendanceModeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OnlineEventAttendanceMode", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OnlineEventAttendanceModeProperties,
        OnlineEventAttendanceModeInheritedProperties,
        OnlineEventAttendanceModeAllProperties,
    ] = OnlineEventAttendanceModeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnlineEventAttendanceMode"
    return model


OnlineEventAttendanceMode = create_schema_org_model()


def create_onlineeventattendancemode_model(
    model: Union[
        OnlineEventAttendanceModeProperties,
        OnlineEventAttendanceModeInheritedProperties,
        OnlineEventAttendanceModeAllProperties,
    ]
):
    _type = deepcopy(OnlineEventAttendanceModeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OnlineEventAttendanceMode. Please see: https://schema.org/OnlineEventAttendanceMode"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OnlineEventAttendanceModeAllProperties):
    pydantic_type = create_onlineeventattendancemode_model(model=model)
    return pydantic_type(model).schema_json()
