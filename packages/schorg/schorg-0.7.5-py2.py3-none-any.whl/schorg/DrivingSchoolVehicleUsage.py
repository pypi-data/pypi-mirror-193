"""
Indicates the usage of the vehicle for driving school.

https://schema.org/DrivingSchoolVehicleUsage
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class DrivingSchoolVehicleUsageAllProperties(
    DrivingSchoolVehicleUsageInheritedProperties,
    DrivingSchoolVehicleUsageProperties,
    TypedDict,
):
    pass


class DrivingSchoolVehicleUsageBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DrivingSchoolVehicleUsage", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DrivingSchoolVehicleUsageProperties,
        DrivingSchoolVehicleUsageInheritedProperties,
        DrivingSchoolVehicleUsageAllProperties,
    ] = DrivingSchoolVehicleUsageAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrivingSchoolVehicleUsage"
    return model


DrivingSchoolVehicleUsage = create_schema_org_model()


def create_drivingschoolvehicleusage_model(
    model: Union[
        DrivingSchoolVehicleUsageProperties,
        DrivingSchoolVehicleUsageInheritedProperties,
        DrivingSchoolVehicleUsageAllProperties,
    ]
):
    _type = deepcopy(DrivingSchoolVehicleUsageAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DrivingSchoolVehicleUsage. Please see: https://schema.org/DrivingSchoolVehicleUsage"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DrivingSchoolVehicleUsageAllProperties):
    pydantic_type = create_drivingschoolvehicleusage_model(model=model)
    return pydantic_type(model).schema_json()
