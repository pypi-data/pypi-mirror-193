"""
A canal, like the Panama Canal.

https://schema.org/Canal
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CanalInheritedProperties(TypedDict):
    """A canal, like the Panama Canal.

    References:
        https://schema.org/Canal
    Note:
        Model Depth 5
    Attributes:
    """

    


class CanalProperties(TypedDict):
    """A canal, like the Panama Canal.

    References:
        https://schema.org/Canal
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(CanalInheritedProperties , CanalProperties, TypedDict):
    pass


class CanalBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Canal",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[CanalProperties, CanalInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Canal"
    return model
    

Canal = create_schema_org_model()


def create_canal_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_canal_model(model=model)
    return pydantic_type(model).schema_json()


