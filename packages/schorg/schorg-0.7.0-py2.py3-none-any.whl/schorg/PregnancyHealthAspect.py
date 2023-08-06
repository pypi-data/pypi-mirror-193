"""
Content discussing pregnancy-related aspects of a health topic.

https://schema.org/PregnancyHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PregnancyHealthAspectInheritedProperties(TypedDict):
    """Content discussing pregnancy-related aspects of a health topic.

    References:
        https://schema.org/PregnancyHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class PregnancyHealthAspectProperties(TypedDict):
    """Content discussing pregnancy-related aspects of a health topic.

    References:
        https://schema.org/PregnancyHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PregnancyHealthAspectInheritedProperties , PregnancyHealthAspectProperties, TypedDict):
    pass


class PregnancyHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PregnancyHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PregnancyHealthAspectProperties, PregnancyHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PregnancyHealthAspect"
    return model
    

PregnancyHealthAspect = create_schema_org_model()


def create_pregnancyhealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_pregnancyhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


