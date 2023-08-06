"""
Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryE
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryEInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryE
    Note:
        Model Depth 6
    Attributes:
    """

    


class EUEnergyEfficiencyCategoryEProperties(TypedDict):
    """Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryE
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EUEnergyEfficiencyCategoryEInheritedProperties , EUEnergyEfficiencyCategoryEProperties, TypedDict):
    pass


class EUEnergyEfficiencyCategoryEBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EUEnergyEfficiencyCategoryE",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EUEnergyEfficiencyCategoryEProperties, EUEnergyEfficiencyCategoryEInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryE"
    return model
    

EUEnergyEfficiencyCategoryE = create_schema_org_model()


def create_euenergyefficiencycategorye_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_euenergyefficiencycategorye_model(model=model)
    return pydantic_type(model).schema_json()


