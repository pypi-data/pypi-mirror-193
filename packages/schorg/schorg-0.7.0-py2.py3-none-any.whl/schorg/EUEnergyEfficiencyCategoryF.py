"""
Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryF
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryFInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryF
    Note:
        Model Depth 6
    Attributes:
    """

    


class EUEnergyEfficiencyCategoryFProperties(TypedDict):
    """Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryF
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EUEnergyEfficiencyCategoryFInheritedProperties , EUEnergyEfficiencyCategoryFProperties, TypedDict):
    pass


class EUEnergyEfficiencyCategoryFBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EUEnergyEfficiencyCategoryF",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EUEnergyEfficiencyCategoryFProperties, EUEnergyEfficiencyCategoryFInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryF"
    return model
    

EUEnergyEfficiencyCategoryF = create_schema_org_model()


def create_euenergyefficiencycategoryf_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_euenergyefficiencycategoryf_model(model=model)
    return pydantic_type(model).schema_json()


