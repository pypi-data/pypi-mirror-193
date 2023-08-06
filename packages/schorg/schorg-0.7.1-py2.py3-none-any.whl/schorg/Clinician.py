"""
Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.

https://schema.org/Clinician
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ClinicianInheritedProperties(TypedDict):
    """Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.

    References:
        https://schema.org/Clinician
    Note:
        Model Depth 6
    Attributes:
    """

    


class ClinicianProperties(TypedDict):
    """Medical clinicians, including practicing physicians and other medical professionals involved in clinical practice.

    References:
        https://schema.org/Clinician
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(ClinicianInheritedProperties , ClinicianProperties, TypedDict):
    pass


class ClinicianBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Clinician",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ClinicianProperties, ClinicianInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Clinician"
    return model
    

Clinician = create_schema_org_model()


def create_clinician_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_clinician_model(model=model)
    return pydantic_type(model).schema_json()


