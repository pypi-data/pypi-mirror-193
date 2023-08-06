"""
Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.

https://schema.org/EnergyEfficiencyEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EnergyEfficiencyEnumerationInheritedProperties(TypedDict):
    """Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.

    References:
        https://schema.org/EnergyEfficiencyEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class EnergyEfficiencyEnumerationProperties(TypedDict):
    """Enumerates energy efficiency levels (also known as "classes" or "ratings") and certifications that are part of several international energy efficiency standards.

    References:
        https://schema.org/EnergyEfficiencyEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class EnergyEfficiencyEnumerationAllProperties(
    EnergyEfficiencyEnumerationInheritedProperties,
    EnergyEfficiencyEnumerationProperties,
    TypedDict,
):
    pass


class EnergyEfficiencyEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EnergyEfficiencyEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        EnergyEfficiencyEnumerationProperties,
        EnergyEfficiencyEnumerationInheritedProperties,
        EnergyEfficiencyEnumerationAllProperties,
    ] = EnergyEfficiencyEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EnergyEfficiencyEnumeration"
    return model


EnergyEfficiencyEnumeration = create_schema_org_model()


def create_energyefficiencyenumeration_model(
    model: Union[
        EnergyEfficiencyEnumerationProperties,
        EnergyEfficiencyEnumerationInheritedProperties,
        EnergyEfficiencyEnumerationAllProperties,
    ]
):
    _type = deepcopy(EnergyEfficiencyEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EnergyEfficiencyEnumeration. Please see: https://schema.org/EnergyEfficiencyEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EnergyEfficiencyEnumerationAllProperties):
    pydantic_type = create_energyefficiencyenumeration_model(model=model)
    return pydantic_type(model).schema_json()
