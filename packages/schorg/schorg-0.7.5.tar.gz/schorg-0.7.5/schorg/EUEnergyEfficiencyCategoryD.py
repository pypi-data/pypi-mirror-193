"""
Represents EU Energy Efficiency Class D as defined in EU energy labeling regulations.

https://schema.org/EUEnergyEfficiencyCategoryD
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class EUEnergyEfficiencyCategoryDAllProperties(
    EUEnergyEfficiencyCategoryDInheritedProperties,
    EUEnergyEfficiencyCategoryDProperties,
    TypedDict,
):
    pass


class EUEnergyEfficiencyCategoryDBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EUEnergyEfficiencyCategoryD", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EUEnergyEfficiencyCategoryDProperties,
        EUEnergyEfficiencyCategoryDInheritedProperties,
        EUEnergyEfficiencyCategoryDAllProperties,
    ] = EUEnergyEfficiencyCategoryDAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyCategoryD"
    return model


EUEnergyEfficiencyCategoryD = create_schema_org_model()


def create_euenergyefficiencycategoryd_model(
    model: Union[
        EUEnergyEfficiencyCategoryDProperties,
        EUEnergyEfficiencyCategoryDInheritedProperties,
        EUEnergyEfficiencyCategoryDAllProperties,
    ]
):
    _type = deepcopy(EUEnergyEfficiencyCategoryDAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EUEnergyEfficiencyCategoryD. Please see: https://schema.org/EUEnergyEfficiencyCategoryD"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EUEnergyEfficiencyCategoryDAllProperties):
    pydantic_type = create_euenergyefficiencycategoryd_model(model=model)
    return pydantic_type(model).schema_json()
