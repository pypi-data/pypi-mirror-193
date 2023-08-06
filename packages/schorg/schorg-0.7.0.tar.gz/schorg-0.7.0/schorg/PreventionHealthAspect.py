"""
Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic.

https://schema.org/PreventionHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PreventionHealthAspectInheritedProperties(TypedDict):
    """Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic.

    References:
        https://schema.org/PreventionHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class PreventionHealthAspectProperties(TypedDict):
    """Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic.

    References:
        https://schema.org/PreventionHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PreventionHealthAspectInheritedProperties , PreventionHealthAspectProperties, TypedDict):
    pass


class PreventionHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PreventionHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PreventionHealthAspectProperties, PreventionHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PreventionHealthAspect"
    return model
    

PreventionHealthAspect = create_schema_org_model()


def create_preventionhealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_preventionhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


