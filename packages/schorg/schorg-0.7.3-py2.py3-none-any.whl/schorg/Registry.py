"""
A registry-based study design.

https://schema.org/Registry
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class RegistryAllProperties(RegistryInheritedProperties, RegistryProperties, TypedDict):
    pass


class RegistryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Registry", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RegistryProperties, RegistryInheritedProperties, RegistryAllProperties
    ] = RegistryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Registry"
    return model


Registry = create_schema_org_model()


def create_registry_model(
    model: Union[RegistryProperties, RegistryInheritedProperties, RegistryAllProperties]
):
    _type = deepcopy(RegistryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RegistryAllProperties):
    pydantic_type = create_registry_model(model=model)
    return pydantic_type(model).schema_json()
