"""
OrderStatus representing that an order is in transit.

https://schema.org/OrderInTransit
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderInTransitInheritedProperties(TypedDict):
    """OrderStatus representing that an order is in transit.

    References:
        https://schema.org/OrderInTransit
    Note:
        Model Depth 6
    Attributes:
    """


class OrderInTransitProperties(TypedDict):
    """OrderStatus representing that an order is in transit.

    References:
        https://schema.org/OrderInTransit
    Note:
        Model Depth 6
    Attributes:
    """


class OrderInTransitAllProperties(
    OrderInTransitInheritedProperties, OrderInTransitProperties, TypedDict
):
    pass


class OrderInTransitBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OrderInTransit", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OrderInTransitProperties,
        OrderInTransitInheritedProperties,
        OrderInTransitAllProperties,
    ] = OrderInTransitAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderInTransit"
    return model


OrderInTransit = create_schema_org_model()


def create_orderintransit_model(
    model: Union[
        OrderInTransitProperties,
        OrderInTransitInheritedProperties,
        OrderInTransitAllProperties,
    ]
):
    _type = deepcopy(OrderInTransitAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OrderInTransitAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OrderInTransitAllProperties):
    pydantic_type = create_orderintransit_model(model=model)
    return pydantic_type(model).schema_json()
