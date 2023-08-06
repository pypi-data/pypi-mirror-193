"""
A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.

https://schema.org/Surgical
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SurgicalInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.

    References:
        https://schema.org/Surgical
    Note:
        Model Depth 6
    Attributes:
    """

    


class SurgicalProperties(TypedDict):
    """A specific branch of medical science that pertains to treating diseases, injuries and deformities by manual and instrumental means.

    References:
        https://schema.org/Surgical
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(SurgicalInheritedProperties , SurgicalProperties, TypedDict):
    pass


class SurgicalBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Surgical",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SurgicalProperties, SurgicalInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Surgical"
    return model
    

Surgical = create_schema_org_model()


def create_surgical_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_surgical_model(model=model)
    return pydantic_type(model).schema_json()


