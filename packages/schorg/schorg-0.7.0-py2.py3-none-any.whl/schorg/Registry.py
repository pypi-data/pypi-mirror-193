"""
A registry-based study design.

https://schema.org/Registry
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RegistryInheritedProperties(TypedDict):
    """A registry-based study design.

    References:
        https://schema.org/Registry
    Note:
        Model Depth 6
    Attributes:
    """

    


class RegistryProperties(TypedDict):
    """A registry-based study design.

    References:
        https://schema.org/Registry
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(RegistryInheritedProperties , RegistryProperties, TypedDict):
    pass


class RegistryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Registry",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RegistryProperties, RegistryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Registry"
    return model
    

Registry = create_schema_org_model()


def create_registry_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_registry_model(model=model)
    return pydantic_type(model).schema_json()


