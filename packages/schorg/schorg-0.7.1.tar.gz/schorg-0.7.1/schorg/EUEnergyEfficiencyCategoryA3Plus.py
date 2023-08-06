"""
Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryA3Plus
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryA3PlusInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryA3Plus
    Note:
        Model Depth 6
    Attributes:
    """

    


class EUEnergyEfficiencyCategoryA3PlusProperties(TypedDict):
    """Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryA3Plus
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EUEnergyEfficiencyCategoryA3PlusInheritedProperties , EUEnergyEfficiencyCategoryA3PlusProperties, TypedDict):
    pass


class EUEnergyEfficiencyCategoryA3PlusBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EUEnergyEfficiencyCategoryA3Plus",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EUEnergyEfficiencyCategoryA3PlusProperties, EUEnergyEfficiencyCategoryA3PlusInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryA3Plus"
    return model
    

EUEnergyEfficiencyCategoryA3Plus = create_schema_org_model()


def create_euenergyefficiencycategorya3plus_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_euenergyefficiencycategorya3plus_model(model=model)
    return pydantic_type(model).schema_json()


