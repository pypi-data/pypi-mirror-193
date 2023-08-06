"""
An indication for treating an underlying condition, symptom, etc.

https://schema.org/TreatmentIndication
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TreatmentIndicationInheritedProperties(TypedDict):
    """An indication for treating an underlying condition, symptom, etc.

    References:
        https://schema.org/TreatmentIndication
    Note:
        Model Depth 4
    Attributes:
    """

    


class TreatmentIndicationProperties(TypedDict):
    """An indication for treating an underlying condition, symptom, etc.

    References:
        https://schema.org/TreatmentIndication
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(TreatmentIndicationInheritedProperties , TreatmentIndicationProperties, TypedDict):
    pass


class TreatmentIndicationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TreatmentIndication",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[TreatmentIndicationProperties, TreatmentIndicationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TreatmentIndication"
    return model
    

TreatmentIndication = create_schema_org_model()


def create_treatmentindication_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_treatmentindication_model(model=model)
    return pydantic_type(model).schema_json()


