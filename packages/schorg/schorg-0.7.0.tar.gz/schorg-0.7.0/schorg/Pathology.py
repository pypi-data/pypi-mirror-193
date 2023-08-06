"""
A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.

https://schema.org/Pathology
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PathologyInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.

    References:
        https://schema.org/Pathology
    Note:
        Model Depth 6
    Attributes:
    """

    


class PathologyProperties(TypedDict):
    """A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.

    References:
        https://schema.org/Pathology
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(PathologyInheritedProperties , PathologyProperties, TypedDict):
    pass


class PathologyBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Pathology",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PathologyProperties, PathologyInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Pathology"
    return model
    

Pathology = create_schema_org_model()


def create_pathology_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_pathology_model(model=model)
    return pydantic_type(model).schema_json()


