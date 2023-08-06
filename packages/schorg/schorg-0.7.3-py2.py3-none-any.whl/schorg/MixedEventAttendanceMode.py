"""
MixedEventAttendanceMode - an event that is conducted as a combination of both offline and online modes.

https://schema.org/MixedEventAttendanceMode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MixedEventAttendanceModeInheritedProperties(TypedDict):
    """MixedEventAttendanceMode - an event that is conducted as a combination of both offline and online modes.

    References:
        https://schema.org/MixedEventAttendanceMode
    Note:
        Model Depth 5
    Attributes:
    """


class MixedEventAttendanceModeProperties(TypedDict):
    """MixedEventAttendanceMode - an event that is conducted as a combination of both offline and online modes.

    References:
        https://schema.org/MixedEventAttendanceMode
    Note:
        Model Depth 5
    Attributes:
    """


class MixedEventAttendanceModeAllProperties(
    MixedEventAttendanceModeInheritedProperties,
    MixedEventAttendanceModeProperties,
    TypedDict,
):
    pass


class MixedEventAttendanceModeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MixedEventAttendanceMode", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MixedEventAttendanceModeProperties,
        MixedEventAttendanceModeInheritedProperties,
        MixedEventAttendanceModeAllProperties,
    ] = MixedEventAttendanceModeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MixedEventAttendanceMode"
    return model


MixedEventAttendanceMode = create_schema_org_model()


def create_mixedeventattendancemode_model(
    model: Union[
        MixedEventAttendanceModeProperties,
        MixedEventAttendanceModeInheritedProperties,
        MixedEventAttendanceModeAllProperties,
    ]
):
    _type = deepcopy(MixedEventAttendanceModeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MixedEventAttendanceModeAllProperties):
    pydantic_type = create_mixedeventattendancemode_model(model=model)
    return pydantic_type(model).schema_json()
