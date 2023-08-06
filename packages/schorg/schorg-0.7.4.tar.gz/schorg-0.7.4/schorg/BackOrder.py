"""
Indicates that the item is available on back order.

https://schema.org/BackOrder
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BackOrderInheritedProperties(TypedDict):
    """Indicates that the item is available on back order.

    References:
        https://schema.org/BackOrder
    Note:
        Model Depth 5
    Attributes:
    """


class BackOrderProperties(TypedDict):
    """Indicates that the item is available on back order.

    References:
        https://schema.org/BackOrder
    Note:
        Model Depth 5
    Attributes:
    """


class BackOrderAllProperties(
    BackOrderInheritedProperties, BackOrderProperties, TypedDict
):
    pass


class BackOrderBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BackOrder", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BackOrderProperties, BackOrderInheritedProperties, BackOrderAllProperties
    ] = BackOrderAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BackOrder"
    return model


BackOrder = create_schema_org_model()


def create_backorder_model(
    model: Union[
        BackOrderProperties, BackOrderInheritedProperties, BackOrderAllProperties
    ]
):
    _type = deepcopy(BackOrderAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BackOrderAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BackOrderAllProperties):
    pydantic_type = create_backorder_model(model=model)
    return pydantic_type(model).schema_json()
