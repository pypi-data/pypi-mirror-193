"""
Content about the allergy-related aspects of a health topic.

https://schema.org/AllergiesHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AllergiesHealthAspectInheritedProperties(TypedDict):
    """Content about the allergy-related aspects of a health topic.

    References:
        https://schema.org/AllergiesHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllergiesHealthAspectProperties(TypedDict):
    """Content about the allergy-related aspects of a health topic.

    References:
        https://schema.org/AllergiesHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AllergiesHealthAspectInheritedProperties , AllergiesHealthAspectProperties, TypedDict):
    pass


class AllergiesHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AllergiesHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AllergiesHealthAspectProperties, AllergiesHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AllergiesHealthAspect"
    return model
    

AllergiesHealthAspect = create_schema_org_model()


def create_allergieshealthaspect_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_allergieshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


