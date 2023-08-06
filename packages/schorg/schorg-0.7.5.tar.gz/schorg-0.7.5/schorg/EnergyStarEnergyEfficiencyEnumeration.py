"""
Used to indicate whether a product is EnergyStar certified.

https://schema.org/EnergyStarEnergyEfficiencyEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EnergyStarEnergyEfficiencyEnumerationInheritedProperties(TypedDict):
    """Used to indicate whether a product is EnergyStar certified.

    References:
        https://schema.org/EnergyStarEnergyEfficiencyEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class EnergyStarEnergyEfficiencyEnumerationProperties(TypedDict):
    """Used to indicate whether a product is EnergyStar certified.

    References:
        https://schema.org/EnergyStarEnergyEfficiencyEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class EnergyStarEnergyEfficiencyEnumerationAllProperties(
    EnergyStarEnergyEfficiencyEnumerationInheritedProperties,
    EnergyStarEnergyEfficiencyEnumerationProperties,
    TypedDict,
):
    pass


class EnergyStarEnergyEfficiencyEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(
        default="EnergyStarEnergyEfficiencyEnumeration", alias="@id"
    )
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EnergyStarEnergyEfficiencyEnumerationProperties,
        EnergyStarEnergyEfficiencyEnumerationInheritedProperties,
        EnergyStarEnergyEfficiencyEnumerationAllProperties,
    ] = EnergyStarEnergyEfficiencyEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EnergyStarEnergyEfficiencyEnumeration"
    return model


EnergyStarEnergyEfficiencyEnumeration = create_schema_org_model()


def create_energystarenergyefficiencyenumeration_model(
    model: Union[
        EnergyStarEnergyEfficiencyEnumerationProperties,
        EnergyStarEnergyEfficiencyEnumerationInheritedProperties,
        EnergyStarEnergyEfficiencyEnumerationAllProperties,
    ]
):
    _type = deepcopy(EnergyStarEnergyEfficiencyEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EnergyStarEnergyEfficiencyEnumeration. Please see: https://schema.org/EnergyStarEnergyEfficiencyEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EnergyStarEnergyEfficiencyEnumerationAllProperties):
    pydantic_type = create_energystarenergyefficiencyenumeration_model(model=model)
    return pydantic_type(model).schema_json()
