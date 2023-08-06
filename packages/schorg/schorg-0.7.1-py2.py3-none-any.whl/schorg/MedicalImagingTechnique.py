"""
Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

https://schema.org/MedicalImagingTechnique
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalImagingTechniqueInheritedProperties(TypedDict):
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

    References:
        https://schema.org/MedicalImagingTechnique
    Note:
        Model Depth 5
    Attributes:
    """

    


class MedicalImagingTechniqueProperties(TypedDict):
    """Any medical imaging modality typically used for diagnostic purposes. Enumerated type.

    References:
        https://schema.org/MedicalImagingTechnique
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MedicalImagingTechniqueInheritedProperties , MedicalImagingTechniqueProperties, TypedDict):
    pass


class MedicalImagingTechniqueBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalImagingTechnique",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MedicalImagingTechniqueProperties, MedicalImagingTechniqueInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalImagingTechnique"
    return model
    

MedicalImagingTechnique = create_schema_org_model()


def create_medicalimagingtechnique_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalimagingtechnique_model(model=model)
    return pydantic_type(model).schema_json()


