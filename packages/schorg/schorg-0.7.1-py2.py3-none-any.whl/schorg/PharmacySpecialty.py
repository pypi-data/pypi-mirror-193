"""
The practice or art and science of preparing and dispensing drugs and medicines.

https://schema.org/PharmacySpecialty
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(PharmacySpecialtyInheritedProperties , PharmacySpecialtyProperties, TypedDict):
    pass


class PharmacySpecialtyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PharmacySpecialty",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PharmacySpecialtyProperties, PharmacySpecialtyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PharmacySpecialty"
    return model
    

PharmacySpecialty = create_schema_org_model()


def create_pharmacyspecialty_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_pharmacyspecialty_model(model=model)
    return pydantic_type(model).schema_json()


