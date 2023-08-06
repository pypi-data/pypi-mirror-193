"""
OrderStatus representing that an order has been returned.

https://schema.org/OrderReturned
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderReturnedInheritedProperties(TypedDict):
    """OrderStatus representing that an order has been returned.

    References:
        https://schema.org/OrderReturned
    Note:
        Model Depth 6
    Attributes:
    """


class OrderReturnedProperties(TypedDict):
    """OrderStatus representing that an order has been returned.

    References:
        https://schema.org/OrderReturned
    Note:
        Model Depth 6
    Attributes:
    """


class OrderReturnedAllProperties(
    OrderReturnedInheritedProperties, OrderReturnedProperties, TypedDict
):
    pass


class OrderReturnedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OrderReturned", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OrderReturnedProperties,
        OrderReturnedInheritedProperties,
        OrderReturnedAllProperties,
    ] = OrderReturnedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderReturned"
    return model


OrderReturned = create_schema_org_model()


def create_orderreturned_model(
    model: Union[
        OrderReturnedProperties,
        OrderReturnedInheritedProperties,
        OrderReturnedAllProperties,
    ]
):
    _type = deepcopy(OrderReturnedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OrderReturnedAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OrderReturnedAllProperties):
    pydantic_type = create_orderreturned_model(model=model)
    return pydantic_type(model).schema_json()
