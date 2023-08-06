"""
Represents EU Energy Efficiency Class F as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryF
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class EUEnergyEfficiencyCategoryFAllProperties(
    EUEnergyEfficiencyCategoryFInheritedProperties,
    EUEnergyEfficiencyCategoryFProperties,
    TypedDict,
):
    pass


class EUEnergyEfficiencyCategoryFBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EUEnergyEfficiencyCategoryF", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EUEnergyEfficiencyCategoryFProperties,
        EUEnergyEfficiencyCategoryFInheritedProperties,
        EUEnergyEfficiencyCategoryFAllProperties,
    ] = EUEnergyEfficiencyCategoryFAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryF"
    return model


EUEnergyEfficiencyCategoryF = create_schema_org_model()


def create_euenergyefficiencycategoryf_model(
    model: Union[
        EUEnergyEfficiencyCategoryFProperties,
        EUEnergyEfficiencyCategoryFInheritedProperties,
        EUEnergyEfficiencyCategoryFAllProperties,
    ]
):
    _type = deepcopy(EUEnergyEfficiencyCategoryFAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EUEnergyEfficiencyCategoryFAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EUEnergyEfficiencyCategoryFAllProperties):
    pydantic_type = create_euenergyefficiencycategoryf_model(model=model)
    return pydantic_type(model).schema_json()
