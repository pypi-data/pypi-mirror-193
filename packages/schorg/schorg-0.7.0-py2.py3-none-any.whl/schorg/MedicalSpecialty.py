"""
Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.

https://schema.org/MedicalSpecialty
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalSpecialtyInheritedProperties(TypedDict):
    """Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.

    References:
        https://schema.org/MedicalSpecialty
    Note:
        Model Depth 5
    Attributes:
    """

    


class MedicalSpecialtyProperties(TypedDict):
    """Any specific branch of medical science or practice. Medical specialities include clinical specialties that pertain to particular organ systems and their respective disease states, as well as allied health specialties. Enumerated type.

    References:
        https://schema.org/MedicalSpecialty
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MedicalSpecialtyInheritedProperties , MedicalSpecialtyProperties, TypedDict):
    pass


class MedicalSpecialtyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalSpecialty",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MedicalSpecialtyProperties, MedicalSpecialtyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalSpecialty"
    return model
    

MedicalSpecialty = create_schema_org_model()


def create_medicalspecialty_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalspecialty_model(model=model)
    return pydantic_type(model).schema_json()


