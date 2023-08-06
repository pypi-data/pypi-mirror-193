"""
Information about the causes and main actions that gave rise to the topic.

https://schema.org/CausesHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CausesHealthAspectInheritedProperties(TypedDict):
    """Information about the causes and main actions that gave rise to the topic.

    References:
        https://schema.org/CausesHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class CausesHealthAspectProperties(TypedDict):
    """Information about the causes and main actions that gave rise to the topic.

    References:
        https://schema.org/CausesHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(CausesHealthAspectInheritedProperties , CausesHealthAspectProperties, TypedDict):
    pass


class CausesHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CausesHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CausesHealthAspectProperties, CausesHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CausesHealthAspect"
    return model
    

CausesHealthAspect = create_schema_org_model()


def create_causeshealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_causeshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


