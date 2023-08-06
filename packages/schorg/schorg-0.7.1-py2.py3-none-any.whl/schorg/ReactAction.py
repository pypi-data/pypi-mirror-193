"""
The act of responding instinctively and emotionally to an object, expressing a sentiment.

https://schema.org/ReactAction
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReactActionInheritedProperties(TypedDict):
    """The act of responding instinctively and emotionally to an object, expressing a sentiment.

    References:
        https://schema.org/ReactAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class ReactActionProperties(TypedDict):
    """The act of responding instinctively and emotionally to an object, expressing a sentiment.

    References:
        https://schema.org/ReactAction
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(ReactActionInheritedProperties , ReactActionProperties, TypedDict):
    pass


class ReactActionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReactAction",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReactActionProperties, ReactActionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReactAction"
    return model
    

ReactAction = create_schema_org_model()


def create_reactaction_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reactaction_model(model=model)
    return pydantic_type(model).schema_json()


