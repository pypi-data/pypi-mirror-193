"""
Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryD
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryDInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryD
    Note:
        Model Depth 6
    Attributes:
    """

    


class EUEnergyEfficiencyCategoryDProperties(TypedDict):
    """Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryD
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(EUEnergyEfficiencyCategoryDInheritedProperties , EUEnergyEfficiencyCategoryDProperties, TypedDict):
    pass


class EUEnergyEfficiencyCategoryDBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="EUEnergyEfficiencyCategoryD",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EUEnergyEfficiencyCategoryDProperties, EUEnergyEfficiencyCategoryDInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryD"
    return model
    

EUEnergyEfficiencyCategoryD = create_schema_org_model()


def create_euenergyefficiencycategoryd_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_euenergyefficiencycategoryd_model(model=model)
    return pydantic_type(model).schema_json()


