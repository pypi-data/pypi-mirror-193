"""
Indicates the usage of the car as a taxi.

https://schema.org/TaxiVehicleUsage
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TaxiVehicleUsageInheritedProperties(TypedDict):
    """Indicates the usage of the car as a taxi.

    References:
        https://schema.org/TaxiVehicleUsage
    Note:
        Model Depth 5
    Attributes:
    """


class TaxiVehicleUsageProperties(TypedDict):
    """Indicates the usage of the car as a taxi.

    References:
        https://schema.org/TaxiVehicleUsage
    Note:
        Model Depth 5
    Attributes:
    """


class TaxiVehicleUsageAllProperties(
    TaxiVehicleUsageInheritedProperties, TaxiVehicleUsageProperties, TypedDict
):
    pass


class TaxiVehicleUsageBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TaxiVehicleUsage", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TaxiVehicleUsageProperties,
        TaxiVehicleUsageInheritedProperties,
        TaxiVehicleUsageAllProperties,
    ] = TaxiVehicleUsageAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TaxiVehicleUsage"
    return model


TaxiVehicleUsage = create_schema_org_model()


def create_taxivehicleusage_model(
    model: Union[
        TaxiVehicleUsageProperties,
        TaxiVehicleUsageInheritedProperties,
        TaxiVehicleUsageAllProperties,
    ]
):
    _type = deepcopy(TaxiVehicleUsageAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TaxiVehicleUsage. Please see: https://schema.org/TaxiVehicleUsage"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TaxiVehicleUsageAllProperties):
    pydantic_type = create_taxivehicleusage_model(model=model)
    return pydantic_type(model).schema_json()
