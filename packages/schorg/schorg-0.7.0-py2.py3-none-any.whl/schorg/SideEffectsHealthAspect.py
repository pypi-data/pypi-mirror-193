"""
Side effects that can be observed from the usage of the topic.

https://schema.org/SideEffectsHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SideEffectsHealthAspectInheritedProperties(TypedDict):
    """Side effects that can be observed from the usage of the topic.

    References:
        https://schema.org/SideEffectsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class SideEffectsHealthAspectProperties(TypedDict):
    """Side effects that can be observed from the usage of the topic.

    References:
        https://schema.org/SideEffectsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SideEffectsHealthAspectInheritedProperties , SideEffectsHealthAspectProperties, TypedDict):
    pass


class SideEffectsHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SideEffectsHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SideEffectsHealthAspectProperties, SideEffectsHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SideEffectsHealthAspect"
    return model
    

SideEffectsHealthAspect = create_schema_org_model()


def create_sideeffectshealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_sideeffectshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


