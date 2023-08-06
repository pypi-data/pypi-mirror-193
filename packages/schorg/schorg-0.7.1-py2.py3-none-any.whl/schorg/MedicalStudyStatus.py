"""
The status of a medical study. Enumerated type.

https://schema.org/MedicalStudyStatus
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalStudyStatusInheritedProperties(TypedDict):
    """The status of a medical study. Enumerated type.

    References:
        https://schema.org/MedicalStudyStatus
    Note:
        Model Depth 5
    Attributes:
    """

    


class MedicalStudyStatusProperties(TypedDict):
    """The status of a medical study. Enumerated type.

    References:
        https://schema.org/MedicalStudyStatus
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MedicalStudyStatusInheritedProperties , MedicalStudyStatusProperties, TypedDict):
    pass


class MedicalStudyStatusBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalStudyStatus",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MedicalStudyStatusProperties, MedicalStudyStatusInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalStudyStatus"
    return model
    

MedicalStudyStatus = create_schema_org_model()


def create_medicalstudystatus_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalstudystatus_model(model=model)
    return pydantic_type(model).schema_json()


