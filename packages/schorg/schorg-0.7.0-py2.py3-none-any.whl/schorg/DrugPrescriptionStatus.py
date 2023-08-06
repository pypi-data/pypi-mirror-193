"""
Indicates whether this drug is available by prescription or over-the-counter.

https://schema.org/DrugPrescriptionStatus
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DrugPrescriptionStatusInheritedProperties(TypedDict):
    """Indicates whether this drug is available by prescription or over-the-counter.

    References:
        https://schema.org/DrugPrescriptionStatus
    Note:
        Model Depth 5
    Attributes:
    """

    


class DrugPrescriptionStatusProperties(TypedDict):
    """Indicates whether this drug is available by prescription or over-the-counter.

    References:
        https://schema.org/DrugPrescriptionStatus
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(DrugPrescriptionStatusInheritedProperties , DrugPrescriptionStatusProperties, TypedDict):
    pass


class DrugPrescriptionStatusBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DrugPrescriptionStatus",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DrugPrescriptionStatusProperties, DrugPrescriptionStatusInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DrugPrescriptionStatus"
    return model
    

DrugPrescriptionStatus = create_schema_org_model()


def create_drugprescriptionstatus_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_drugprescriptionstatus_model(model=model)
    return pydantic_type(model).schema_json()


