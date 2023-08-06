"""
Information about coping or life related to the topic.

https://schema.org/LivingWithHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LivingWithHealthAspectInheritedProperties(TypedDict):
    """Information about coping or life related to the topic.

    References:
        https://schema.org/LivingWithHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class LivingWithHealthAspectProperties(TypedDict):
    """Information about coping or life related to the topic.

    References:
        https://schema.org/LivingWithHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(LivingWithHealthAspectInheritedProperties , LivingWithHealthAspectProperties, TypedDict):
    pass


class LivingWithHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LivingWithHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LivingWithHealthAspectProperties, LivingWithHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LivingWithHealthAspect"
    return model
    

LivingWithHealthAspect = create_schema_org_model()


def create_livingwithhealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_livingwithhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


