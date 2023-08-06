"""
Indicates that the item has sold out.

https://schema.org/SoldOut
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SoldOutInheritedProperties(TypedDict):
    """Indicates that the item has sold out.

    References:
        https://schema.org/SoldOut
    Note:
        Model Depth 5
    Attributes:
    """


class SoldOutProperties(TypedDict):
    """Indicates that the item has sold out.

    References:
        https://schema.org/SoldOut
    Note:
        Model Depth 5
    Attributes:
    """


class SoldOutAllProperties(SoldOutInheritedProperties, SoldOutProperties, TypedDict):
    pass


class SoldOutBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SoldOut", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SoldOutProperties, SoldOutInheritedProperties, SoldOutAllProperties
    ] = SoldOutAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SoldOut"
    return model


SoldOut = create_schema_org_model()


def create_soldout_model(
    model: Union[SoldOutProperties, SoldOutInheritedProperties, SoldOutAllProperties]
):
    _type = deepcopy(SoldOutAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SoldOutAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SoldOutAllProperties):
    pydantic_type = create_soldout_model(model=model)
    return pydantic_type(model).schema_json()
