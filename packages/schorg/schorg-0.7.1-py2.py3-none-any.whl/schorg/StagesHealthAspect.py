"""
Stages that can be observed from a topic.

https://schema.org/StagesHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class StagesHealthAspectInheritedProperties(TypedDict):
    """Stages that can be observed from a topic.

    References:
        https://schema.org/StagesHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class StagesHealthAspectProperties(TypedDict):
    """Stages that can be observed from a topic.

    References:
        https://schema.org/StagesHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(StagesHealthAspectInheritedProperties , StagesHealthAspectProperties, TypedDict):
    pass


class StagesHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="StagesHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[StagesHealthAspectProperties, StagesHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "StagesHealthAspect"
    return model
    

StagesHealthAspect = create_schema_org_model()


def create_stageshealthaspect_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_stageshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


