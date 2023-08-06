"""
Indicates the usage of the vehicle as a rental car.

https://schema.org/RentalVehicleUsage
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RentalVehicleUsageInheritedProperties(TypedDict):
    """Indicates the usage of the vehicle as a rental car.

    References:
        https://schema.org/RentalVehicleUsage
    Note:
        Model Depth 5
    Attributes:
    """


class RentalVehicleUsageProperties(TypedDict):
    """Indicates the usage of the vehicle as a rental car.

    References:
        https://schema.org/RentalVehicleUsage
    Note:
        Model Depth 5
    Attributes:
    """


class RentalVehicleUsageAllProperties(
    RentalVehicleUsageInheritedProperties, RentalVehicleUsageProperties, TypedDict
):
    pass


class RentalVehicleUsageBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RentalVehicleUsage", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RentalVehicleUsageProperties,
        RentalVehicleUsageInheritedProperties,
        RentalVehicleUsageAllProperties,
    ] = RentalVehicleUsageAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RentalVehicleUsage"
    return model


RentalVehicleUsage = create_schema_org_model()


def create_rentalvehicleusage_model(
    model: Union[
        RentalVehicleUsageProperties,
        RentalVehicleUsageInheritedProperties,
        RentalVehicleUsageAllProperties,
    ]
):
    _type = deepcopy(RentalVehicleUsageAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RentalVehicleUsageAllProperties):
    pydantic_type = create_rentalvehicleusage_model(model=model)
    return pydantic_type(model).schema_json()
