"""
The act of intentionally disregarding the object. An agent ignores an object.

https://schema.org/IgnoreAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class IgnoreActionInheritedProperties(TypedDict):
    """The act of intentionally disregarding the object. An agent ignores an object.

    References:
        https://schema.org/IgnoreAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class IgnoreActionProperties(TypedDict):
    """The act of intentionally disregarding the object. An agent ignores an object.

    References:
        https://schema.org/IgnoreAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(IgnoreActionInheritedProperties , IgnoreActionProperties, TypedDict):
    pass


class IgnoreActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="IgnoreAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[IgnoreActionProperties, IgnoreActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "IgnoreAction"
    return model
    

IgnoreAction = create_schema_org_model()


def create_ignoreaction_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_ignoreaction_model(model=model)
    return pydantic_type(model).schema_json()


