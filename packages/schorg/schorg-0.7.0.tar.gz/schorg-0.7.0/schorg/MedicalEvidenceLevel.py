"""
Level of evidence for a medical guideline. Enumerated type.

https://schema.org/MedicalEvidenceLevel
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalEvidenceLevelInheritedProperties(TypedDict):
    """Level of evidence for a medical guideline. Enumerated type.

    References:
        https://schema.org/MedicalEvidenceLevel
    Note:
        Model Depth 5
    Attributes:
    """

    


class MedicalEvidenceLevelProperties(TypedDict):
    """Level of evidence for a medical guideline. Enumerated type.

    References:
        https://schema.org/MedicalEvidenceLevel
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MedicalEvidenceLevelInheritedProperties , MedicalEvidenceLevelProperties, TypedDict):
    pass


class MedicalEvidenceLevelBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalEvidenceLevel",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MedicalEvidenceLevelProperties, MedicalEvidenceLevelInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalEvidenceLevel"
    return model
    

MedicalEvidenceLevel = create_schema_org_model()


def create_medicalevidencelevel_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalevidencelevel_model(model=model)
    return pydantic_type(model).schema_json()


