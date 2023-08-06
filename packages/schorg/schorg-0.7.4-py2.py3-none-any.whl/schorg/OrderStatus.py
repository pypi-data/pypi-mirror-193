"""
Enumerated status values for Order.

https://schema.org/OrderStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderStatusInheritedProperties(TypedDict):
    """Enumerated status values for Order.

    References:
        https://schema.org/OrderStatus
    Note:
        Model Depth 5
    Attributes:
    """


class OrderStatusProperties(TypedDict):
    """Enumerated status values for Order.

    References:
        https://schema.org/OrderStatus
    Note:
        Model Depth 5
    Attributes:
    """


class OrderStatusAllProperties(
    OrderStatusInheritedProperties, OrderStatusProperties, TypedDict
):
    pass


class OrderStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OrderStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OrderStatusProperties, OrderStatusInheritedProperties, OrderStatusAllProperties
    ] = OrderStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderStatus"
    return model


OrderStatus = create_schema_org_model()


def create_orderstatus_model(
    model: Union[
        OrderStatusProperties, OrderStatusInheritedProperties, OrderStatusAllProperties
    ]
):
    _type = deepcopy(OrderStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OrderStatusAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OrderStatusAllProperties):
    pydantic_type = create_orderstatus_model(model=model)
    return pydantic_type(model).schema_json()
