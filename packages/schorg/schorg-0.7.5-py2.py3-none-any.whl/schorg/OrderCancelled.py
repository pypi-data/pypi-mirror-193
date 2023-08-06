"""
OrderStatus representing cancellation of an order.

https://schema.org/OrderCancelled
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderCancelledInheritedProperties(TypedDict):
    """OrderStatus representing cancellation of an order.

    References:
        https://schema.org/OrderCancelled
    Note:
        Model Depth 6
    Attributes:
    """


class OrderCancelledProperties(TypedDict):
    """OrderStatus representing cancellation of an order.

    References:
        https://schema.org/OrderCancelled
    Note:
        Model Depth 6
    Attributes:
    """


class OrderCancelledAllProperties(
    OrderCancelledInheritedProperties, OrderCancelledProperties, TypedDict
):
    pass


class OrderCancelledBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OrderCancelled", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OrderCancelledProperties,
        OrderCancelledInheritedProperties,
        OrderCancelledAllProperties,
    ] = OrderCancelledAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderCancelled"
    return model


OrderCancelled = create_schema_org_model()


def create_ordercancelled_model(
    model: Union[
        OrderCancelledProperties,
        OrderCancelledInheritedProperties,
        OrderCancelledAllProperties,
    ]
):
    _type = deepcopy(OrderCancelledAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OrderCancelled. Please see: https://schema.org/OrderCancelled"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OrderCancelledAllProperties):
    pydantic_type = create_ordercancelled_model(model=model)
    return pydantic_type(model).schema_json()
