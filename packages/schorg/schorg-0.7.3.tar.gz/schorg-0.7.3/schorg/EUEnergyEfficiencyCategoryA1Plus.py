"""
Represents EU Energy Efficiency Class A+ as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryA1Plus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryA1PlusInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class A+ as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryA1Plus
    Note:
        Model Depth 6
    Attributes:
    """


class EUEnergyEfficiencyCategoryA1PlusProperties(TypedDict):
    """Represents EU Energy Efficiency Class A+ as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryA1Plus
    Note:
        Model Depth 6
    Attributes:
    """


class EUEnergyEfficiencyCategoryA1PlusAllProperties(
    EUEnergyEfficiencyCategoryA1PlusInheritedProperties,
    EUEnergyEfficiencyCategoryA1PlusProperties,
    TypedDict,
):
    pass


class EUEnergyEfficiencyCategoryA1PlusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EUEnergyEfficiencyCategoryA1Plus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EUEnergyEfficiencyCategoryA1PlusProperties,
        EUEnergyEfficiencyCategoryA1PlusInheritedProperties,
        EUEnergyEfficiencyCategoryA1PlusAllProperties,
    ] = EUEnergyEfficiencyCategoryA1PlusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryA1Plus"
    return model


EUEnergyEfficiencyCategoryA1Plus = create_schema_org_model()


def create_euenergyefficiencycategorya1plus_model(
    model: Union[
        EUEnergyEfficiencyCategoryA1PlusProperties,
        EUEnergyEfficiencyCategoryA1PlusInheritedProperties,
        EUEnergyEfficiencyCategoryA1PlusAllProperties,
    ]
):
    _type = deepcopy(EUEnergyEfficiencyCategoryA1PlusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EUEnergyEfficiencyCategoryA1PlusAllProperties):
    pydantic_type = create_euenergyefficiencycategorya1plus_model(model=model)
    return pydantic_type(model).schema_json()
