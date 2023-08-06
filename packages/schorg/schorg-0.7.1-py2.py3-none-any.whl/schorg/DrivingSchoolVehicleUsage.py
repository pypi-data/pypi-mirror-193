"""
Indicates the usage of the vehicle for driving school.

https://schema.org/DrivingSchoolVehicleUsage
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrivingSchoolVehicleUsageInheritedProperties(TypedDict):
    """Indicates the usage of the vehicle for driving school.

    References:
        https://schema.org/DrivingSchoolVehicleUsage
    Note:
        Model Depth 5
    Attributes:
    """

    


class DrivingSchoolVehicleUsageProperties(TypedDict):
    """Indicates the usage of the vehicle for driving school.

    References:
        https://schema.org/DrivingSchoolVehicleUsage
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(DrivingSchoolVehicleUsageInheritedProperties , DrivingSchoolVehicleUsageProperties, TypedDict):
    pass


class DrivingSchoolVehicleUsageBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DrivingSchoolVehicleUsage",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DrivingSchoolVehicleUsageProperties, DrivingSchoolVehicleUsageInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrivingSchoolVehicleUsage"
    return model
    

DrivingSchoolVehicleUsage = create_schema_org_model()


def create_drivingschoolvehicleusage_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_drivingschoolvehicleusage_model(model=model)
    return pydantic_type(model).schema_json()


