"""
Represents EU Energy Efficiency Class G as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryG
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryGInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class G as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryG
    Note:
        Model Depth 6
    Attributes:
    """

    


class EUEnergyEfficiencyCategoryGProperties(TypedDict):
    """Represents EU Energy Efficiency Class G as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryG
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EUEnergyEfficiencyCategoryGInheritedProperties , EUEnergyEfficiencyCategoryGProperties, TypedDict):
    pass


class EUEnergyEfficiencyCategoryGBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EUEnergyEfficiencyCategoryG",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EUEnergyEfficiencyCategoryGProperties, EUEnergyEfficiencyCategoryGInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryG"
    return model
    

EUEnergyEfficiencyCategoryG = create_schema_org_model()


def create_euenergyefficiencycategoryg_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_euenergyefficiencycategoryg_model(model=model)
    return pydantic_type(model).schema_json()


