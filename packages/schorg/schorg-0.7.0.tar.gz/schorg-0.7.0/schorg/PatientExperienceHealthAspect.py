"""
Content about the real life experience of patients or people that have lived a similar experience about the topic. May be forums, topics, Q-and-A and related material.

https://schema.org/PatientExperienceHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PatientExperienceHealthAspectInheritedProperties(TypedDict):
    """Content about the real life experience of patients or people that have lived a similar experience about the topic. May be forums, topics, Q-and-A and related material.

    References:
        https://schema.org/PatientExperienceHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class PatientExperienceHealthAspectProperties(TypedDict):
    """Content about the real life experience of patients or people that have lived a similar experience about the topic. May be forums, topics, Q-and-A and related material.

    References:
        https://schema.org/PatientExperienceHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PatientExperienceHealthAspectInheritedProperties , PatientExperienceHealthAspectProperties, TypedDict):
    pass


class PatientExperienceHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PatientExperienceHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PatientExperienceHealthAspectProperties, PatientExperienceHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PatientExperienceHealthAspect"
    return model
    

PatientExperienceHealthAspect = create_schema_org_model()


def create_patientexperiencehealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_patientexperiencehealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


