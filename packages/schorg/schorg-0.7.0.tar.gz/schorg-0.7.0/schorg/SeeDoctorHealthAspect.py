"""
Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation.

https://schema.org/SeeDoctorHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SeeDoctorHealthAspectInheritedProperties(TypedDict):
    """Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation.

    References:
        https://schema.org/SeeDoctorHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class SeeDoctorHealthAspectProperties(TypedDict):
    """Information about questions that may be asked, when to see a professional, measures before seeing a doctor or content about the first consultation.

    References:
        https://schema.org/SeeDoctorHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SeeDoctorHealthAspectInheritedProperties , SeeDoctorHealthAspectProperties, TypedDict):
    pass


class SeeDoctorHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SeeDoctorHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SeeDoctorHealthAspectProperties, SeeDoctorHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SeeDoctorHealthAspect"
    return model
    

SeeDoctorHealthAspect = create_schema_org_model()


def create_seedoctorhealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_seedoctorhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


