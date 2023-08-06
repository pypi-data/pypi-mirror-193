"""
Represents EU Energy Efficiency Class E as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryE
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class EUEnergyEfficiencyCategoryEAllProperties(
    EUEnergyEfficiencyCategoryEInheritedProperties,
    EUEnergyEfficiencyCategoryEProperties,
    TypedDict,
):
    pass


class EUEnergyEfficiencyCategoryEBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EUEnergyEfficiencyCategoryE", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EUEnergyEfficiencyCategoryEProperties,
        EUEnergyEfficiencyCategoryEInheritedProperties,
        EUEnergyEfficiencyCategoryEAllProperties,
    ] = EUEnergyEfficiencyCategoryEAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryE"
    return model


EUEnergyEfficiencyCategoryE = create_schema_org_model()


def create_euenergyefficiencycategorye_model(
    model: Union[
        EUEnergyEfficiencyCategoryEProperties,
        EUEnergyEfficiencyCategoryEInheritedProperties,
        EUEnergyEfficiencyCategoryEAllProperties,
    ]
):
    _type = deepcopy(EUEnergyEfficiencyCategoryEAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EUEnergyEfficiencyCategoryEAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EUEnergyEfficiencyCategoryEAllProperties):
    pydantic_type = create_euenergyefficiencycategorye_model(model=model)
    return pydantic_type(model).schema_json()
