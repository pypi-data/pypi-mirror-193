"""
OfflineEventAttendanceMode - an event that is primarily conducted offline. 

https://schema.org/OfflineEventAttendanceMode
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfflineEventAttendanceModeInheritedProperties(TypedDict):
    """OfflineEventAttendanceMode - an event that is primarily conducted offline. 

    References:
        https://schema.org/OfflineEventAttendanceMode
    Note:
        Model Depth 5
    Attributes:
    """

    


class OfflineEventAttendanceModeProperties(TypedDict):
    """OfflineEventAttendanceMode - an event that is primarily conducted offline. 

    References:
        https://schema.org/OfflineEventAttendanceMode
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(OfflineEventAttendanceModeInheritedProperties , OfflineEventAttendanceModeProperties, TypedDict):
    pass


class OfflineEventAttendanceModeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OfflineEventAttendanceMode",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OfflineEventAttendanceModeProperties, OfflineEventAttendanceModeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OfflineEventAttendanceMode"
    return model
    

OfflineEventAttendanceMode = create_schema_org_model()


def create_offlineeventattendancemode_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_offlineeventattendancemode_model(model=model)
    return pydantic_type(model).schema_json()


