"""
Other prominent or relevant topics tied to the main topic.

https://schema.org/RelatedTopicsHealthAspect
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RelatedTopicsHealthAspectInheritedProperties(TypedDict):
    """Other prominent or relevant topics tied to the main topic.

    References:
        https://schema.org/RelatedTopicsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class RelatedTopicsHealthAspectProperties(TypedDict):
    """Other prominent or relevant topics tied to the main topic.

    References:
        https://schema.org/RelatedTopicsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(RelatedTopicsHealthAspectInheritedProperties , RelatedTopicsHealthAspectProperties, TypedDict):
    pass


class RelatedTopicsHealthAspectBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RelatedTopicsHealthAspect",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RelatedTopicsHealthAspectProperties, RelatedTopicsHealthAspectInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RelatedTopicsHealthAspect"
    return model
    

RelatedTopicsHealthAspect = create_schema_org_model()


def create_relatedtopicshealthaspect_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_relatedtopicshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()


