"""
Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.

https://schema.org/EUEnergyEfficiencyEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EUEnergyEfficiencyEnumerationInheritedProperties(TypedDict):
    """Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.

    References:
        https://schema.org/EUEnergyEfficiencyEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class EUEnergyEfficiencyEnumerationProperties(TypedDict):
    """Enumerates the EU energy efficiency classes A-G as well as A+, A++, and A+++ as defined in EU directive 2017/1369.

    References:
        https://schema.org/EUEnergyEfficiencyEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class EUEnergyEfficiencyEnumerationAllProperties(
    EUEnergyEfficiencyEnumerationInheritedProperties,
    EUEnergyEfficiencyEnumerationProperties,
    TypedDict,
):
    pass


class EUEnergyEfficiencyEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EUEnergyEfficiencyEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EUEnergyEfficiencyEnumerationProperties,
        EUEnergyEfficiencyEnumerationInheritedProperties,
        EUEnergyEfficiencyEnumerationAllProperties,
    ] = EUEnergyEfficiencyEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EUEnergyEfficiencyEnumeration"
    return model


EUEnergyEfficiencyEnumeration = create_schema_org_model()


def create_euenergyefficiencyenumeration_model(
    model: Union[
        EUEnergyEfficiencyEnumerationProperties,
        EUEnergyEfficiencyEnumerationInheritedProperties,
        EUEnergyEfficiencyEnumerationAllProperties,
    ]
):
    _type = deepcopy(EUEnergyEfficiencyEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EUEnergyEfficiencyEnumerationAllProperties):
    pydantic_type = create_euenergyefficiencyenumeration_model(model=model)
    return pydantic_type(model).schema_json()
