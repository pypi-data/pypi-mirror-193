"""
Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryB
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryBInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryB
    Note:
        Model Depth 6
    Attributes:
    """


class EUEnergyEfficiencyCategoryBProperties(TypedDict):
    """Represents EU Energy Efficiency Class B as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryB
    Note:
        Model Depth 6
    Attributes:
    """


class EUEnergyEfficiencyCategoryBAllProperties(
    EUEnergyEfficiencyCategoryBInheritedProperties,
    EUEnergyEfficiencyCategoryBProperties,
    TypedDict,
):
    pass


class EUEnergyEfficiencyCategoryBBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EUEnergyEfficiencyCategoryB", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EUEnergyEfficiencyCategoryBProperties,
        EUEnergyEfficiencyCategoryBInheritedProperties,
        EUEnergyEfficiencyCategoryBAllProperties,
    ] = EUEnergyEfficiencyCategoryBAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryB"
    return model


EUEnergyEfficiencyCategoryB = create_schema_org_model()


def create_euenergyefficiencycategoryb_model(
    model: Union[
        EUEnergyEfficiencyCategoryBProperties,
        EUEnergyEfficiencyCategoryBInheritedProperties,
        EUEnergyEfficiencyCategoryBAllProperties,
    ]
):
    _type = deepcopy(EUEnergyEfficiencyCategoryBAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EUEnergyEfficiencyCategoryBAllProperties):
    pydantic_type = create_euenergyefficiencycategoryb_model(model=model)
    return pydantic_type(model).schema_json()
