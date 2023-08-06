"""
Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryA
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyCategoryAInheritedProperties(TypedDict):
    """Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryA
    Note:
        Model Depth 6
    Attributes:
    """


class EUEnergyEfficiencyCategoryAProperties(TypedDict):
    """Represents EU Energy Efficiency Class A as defined in EU energy labeling regulations.

    References:
        https://schema.org/EUEnergyEfficiencyCategoryA
    Note:
        Model Depth 6
    Attributes:
    """


class EUEnergyEfficiencyCategoryAAllProperties(
    EUEnergyEfficiencyCategoryAInheritedProperties,
    EUEnergyEfficiencyCategoryAProperties,
    TypedDict,
):
    pass


class EUEnergyEfficiencyCategoryABaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EUEnergyEfficiencyCategoryA", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EUEnergyEfficiencyCategoryAProperties,
        EUEnergyEfficiencyCategoryAInheritedProperties,
        EUEnergyEfficiencyCategoryAAllProperties,
    ] = EUEnergyEfficiencyCategoryAAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryA"
    return model


EUEnergyEfficiencyCategoryA = create_schema_org_model()


def create_euenergyefficiencycategorya_model(
    model: Union[
        EUEnergyEfficiencyCategoryAProperties,
        EUEnergyEfficiencyCategoryAInheritedProperties,
        EUEnergyEfficiencyCategoryAAllProperties,
    ]
):
    _type = deepcopy(EUEnergyEfficiencyCategoryAAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EUEnergyEfficiencyCategoryAAllProperties):
    pydantic_type = create_euenergyefficiencycategorya_model(model=model)
    return pydantic_type(model).schema_json()
