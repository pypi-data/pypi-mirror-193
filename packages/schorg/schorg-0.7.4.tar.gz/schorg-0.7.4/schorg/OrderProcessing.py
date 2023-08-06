"""
OrderStatus representing that an order is being processed.

https://schema.org/OrderProcessing
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderProcessingInheritedProperties(TypedDict):
    """OrderStatus representing that an order is being processed.

    References:
        https://schema.org/OrderProcessing
    Note:
        Model Depth 6
    Attributes:
    """


class OrderProcessingProperties(TypedDict):
    """OrderStatus representing that an order is being processed.

    References:
        https://schema.org/OrderProcessing
    Note:
        Model Depth 6
    Attributes:
    """


class OrderProcessingAllProperties(
    OrderProcessingInheritedProperties, OrderProcessingProperties, TypedDict
):
    pass


class OrderProcessingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OrderProcessing", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OrderProcessingProperties,
        OrderProcessingInheritedProperties,
        OrderProcessingAllProperties,
    ] = OrderProcessingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderProcessing"
    return model


OrderProcessing = create_schema_org_model()


def create_orderprocessing_model(
    model: Union[
        OrderProcessingProperties,
        OrderProcessingInheritedProperties,
        OrderProcessingAllProperties,
    ]
):
    _type = deepcopy(OrderProcessingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OrderProcessingAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OrderProcessingAllProperties):
    pydantic_type = create_orderprocessing_model(model=model)
    return pydantic_type(model).schema_json()
