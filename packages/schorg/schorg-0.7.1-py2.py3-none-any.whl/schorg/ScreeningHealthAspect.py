"""
Content about how to screen or further filter a topic.

https://schema.org/ScreeningHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ScreeningHealthAspectInheritedProperties(TypedDict):
    """Content about how to screen or further filter a topic.

    References:
        https://schema.org/ScreeningHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class ScreeningHealthAspectProperties(TypedDict):
    """Content about how to screen or further filter a topic.

    References:
        https://schema.org/ScreeningHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ScreeningHealthAspectInheritedProperties , ScreeningHealthAspectProperties, TypedDict):
    pass


class ScreeningHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ScreeningHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ScreeningHealthAspectProperties, ScreeningHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ScreeningHealthAspect"
    return model
    

ScreeningHealthAspect = create_schema_org_model()


def create_screeninghealthaspect_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_screeninghealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


