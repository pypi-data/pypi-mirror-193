"""
Design models for observational medical studies. Enumerated type.

https://schema.org/MedicalObservationalStudyDesign
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalObservationalStudyDesignInheritedProperties(TypedDict):
    """Design models for observational medical studies. Enumerated type.

    References:
        https://schema.org/MedicalObservationalStudyDesign
    Note:
        Model Depth 5
    Attributes:
    """

    


class MedicalObservationalStudyDesignProperties(TypedDict):
    """Design models for observational medical studies. Enumerated type.

    References:
        https://schema.org/MedicalObservationalStudyDesign
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MedicalObservationalStudyDesignInheritedProperties , MedicalObservationalStudyDesignProperties, TypedDict):
    pass


class MedicalObservationalStudyDesignBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalObservationalStudyDesign",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MedicalObservationalStudyDesignProperties, MedicalObservationalStudyDesignInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalObservationalStudyDesign"
    return model
    

MedicalObservationalStudyDesign = create_schema_org_model()


def create_medicalobservationalstudydesign_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalobservationalstudydesign_model(model=model)
    return pydantic_type(model).schema_json()


