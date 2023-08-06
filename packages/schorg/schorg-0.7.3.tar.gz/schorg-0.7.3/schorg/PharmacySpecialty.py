"""
The practice or art and science of preparing and dispensing drugs and medicines.

https://schema.org/PharmacySpecialty
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PharmacySpecialtyInheritedProperties(TypedDict):
    """The practice or art and science of preparing and dispensing drugs and medicines.

    References:
        https://schema.org/PharmacySpecialty
    Note:
        Model Depth 6
    Attributes:
    """


class PharmacySpecialtyProperties(TypedDict):
    """The practice or art and science of preparing and dispensing drugs and medicines.

    References:
        https://schema.org/PharmacySpecialty
    Note:
        Model Depth 6
    Attributes:
    """


class PharmacySpecialtyAllProperties(
    PharmacySpecialtyInheritedProperties, PharmacySpecialtyProperties, TypedDict
):
    pass


class PharmacySpecialtyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PharmacySpecialty", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PharmacySpecialtyProperties,
        PharmacySpecialtyInheritedProperties,
        PharmacySpecialtyAllProperties,
    ] = PharmacySpecialtyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PharmacySpecialty"
    return model


PharmacySpecialty = create_schema_org_model()


def create_pharmacyspecialty_model(
    model: Union[
        PharmacySpecialtyProperties,
        PharmacySpecialtyInheritedProperties,
        PharmacySpecialtyAllProperties,
    ]
):
    _type = deepcopy(PharmacySpecialtyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PharmacySpecialtyAllProperties):
    pydantic_type = create_pharmacyspecialty_model(model=model)
    return pydantic_type(model).schema_json()
