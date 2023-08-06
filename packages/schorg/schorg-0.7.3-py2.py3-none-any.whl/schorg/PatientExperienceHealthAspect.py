"""
Content about the real life experience of patients or people that have lived a similar experience about the topic. May be forums, topics, Q-and-A and related material.

https://schema.org/PatientExperienceHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class PatientExperienceHealthAspectAllProperties(
    PatientExperienceHealthAspectInheritedProperties,
    PatientExperienceHealthAspectProperties,
    TypedDict,
):
    pass


class PatientExperienceHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PatientExperienceHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PatientExperienceHealthAspectProperties,
        PatientExperienceHealthAspectInheritedProperties,
        PatientExperienceHealthAspectAllProperties,
    ] = PatientExperienceHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PatientExperienceHealthAspect"
    return model


PatientExperienceHealthAspect = create_schema_org_model()


def create_patientexperiencehealthaspect_model(
    model: Union[
        PatientExperienceHealthAspectProperties,
        PatientExperienceHealthAspectInheritedProperties,
        PatientExperienceHealthAspectAllProperties,
    ]
):
    _type = deepcopy(PatientExperienceHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PatientExperienceHealthAspectAllProperties):
    pydantic_type = create_patientexperiencehealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
