"""
A car wash business.

https://schema.org/AutoWash
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AutoWashInheritedProperties(TypedDict):
    """A car wash business.

    References:
        https://schema.org/AutoWash
    Note:
        Model Depth 5
    Attributes:
    """

    


class AutoWashProperties(TypedDict):
    """A car wash business.

    References:
        https://schema.org/AutoWash
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AutoWashInheritedProperties , AutoWashProperties, TypedDict):
    pass


class AutoWashBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AutoWash",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AutoWashProperties, AutoWashInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AutoWash"
    return model
    

AutoWash = create_schema_org_model()


def create_autowash_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_autowash_model(model=model)
    return pydantic_type(model).schema_json()


