"""
Represents EU Energy Efficiency Class C as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryC
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryCInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class C as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryC
    Note:
        Model Depth 6
    Attributes:
    """

    


class EUEnergyEfficiencyCategoryCProperties(TypedDict):
    """Represents EU Energy Efficiency Class C as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryC
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EUEnergyEfficiencyCategoryCInheritedProperties , EUEnergyEfficiencyCategoryCProperties, TypedDict):
    pass


class EUEnergyEfficiencyCategoryCBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EUEnergyEfficiencyCategoryC",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EUEnergyEfficiencyCategoryCProperties, EUEnergyEfficiencyCategoryCInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryC"
    return model
    

EUEnergyEfficiencyCategoryC = create_schema_org_model()


def create_euenergyefficiencycategoryc_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_euenergyefficiencycategoryc_model(model=model)
    return pydantic_type(model).schema_json()


