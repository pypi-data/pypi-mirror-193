"""
Represents EU Energy Efficiency Class A+++ as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryA3Plus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class EUEnergyEfficiencyCategoryA3PlusAllProperties(
    EUEnergyEfficiencyCategoryA3PlusInheritedProperties,
    EUEnergyEfficiencyCategoryA3PlusProperties,
    TypedDict,
):
    pass


class EUEnergyEfficiencyCategoryA3PlusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EUEnergyEfficiencyCategoryA3Plus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EUEnergyEfficiencyCategoryA3PlusProperties,
        EUEnergyEfficiencyCategoryA3PlusInheritedProperties,
        EUEnergyEfficiencyCategoryA3PlusAllProperties,
    ] = EUEnergyEfficiencyCategoryA3PlusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryA3Plus"
    return model


EUEnergyEfficiencyCategoryA3Plus = create_schema_org_model()


def create_euenergyefficiencycategorya3plus_model(
    model: Union[
        EUEnergyEfficiencyCategoryA3PlusProperties,
        EUEnergyEfficiencyCategoryA3PlusInheritedProperties,
        EUEnergyEfficiencyCategoryA3PlusAllProperties,
    ]
):
    _type = deepcopy(EUEnergyEfficiencyCategoryA3PlusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EUEnergyEfficiencyCategoryA3PlusAllProperties):
    pydantic_type = create_euenergyefficiencycategorya3plus_model(model=model)
    return pydantic_type(model).schema_json()
