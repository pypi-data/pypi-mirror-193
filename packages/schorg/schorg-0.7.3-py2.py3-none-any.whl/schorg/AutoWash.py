"""
A car wash business.

https://schema.org/AutoWash
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class AutoWashAllProperties(AutoWashInheritedProperties, AutoWashProperties, TypedDict):
    pass


class AutoWashBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AutoWash", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AutoWashProperties, AutoWashInheritedProperties, AutoWashAllProperties
    ] = AutoWashAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AutoWash"
    return model


AutoWash = create_schema_org_model()


def create_autowash_model(
    model: Union[AutoWashProperties, AutoWashInheritedProperties, AutoWashAllProperties]
):
    _type = deepcopy(AutoWashAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AutoWashAllProperties):
    pydantic_type = create_autowash_model(model=model)
    return pydantic_type(model).schema_json()
