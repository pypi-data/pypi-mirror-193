"""
Indicates the usage of the car as a taxi.

https://schema.org/TaxiVehicleUsage
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(TaxiVehicleUsageInheritedProperties , TaxiVehicleUsageProperties, TypedDict):
    pass


class TaxiVehicleUsageBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TaxiVehicleUsage",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TaxiVehicleUsageProperties, TaxiVehicleUsageInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TaxiVehicleUsage"
    return model
    

TaxiVehicleUsage = create_schema_org_model()


def create_taxivehicleusage_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_taxivehicleusage_model(model=model)
    return pydantic_type(model).schema_json()


