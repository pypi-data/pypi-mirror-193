"""
OrderStatus representing availability of an order for pickup.

https://schema.org/OrderPickupAvailable
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderPickupAvailableInheritedProperties(TypedDict):
    """OrderStatus representing availability of an order for pickup.

    References:
        https://schema.org/OrderPickupAvailable
    Note:
        Model Depth 6
    Attributes:
    """


class OrderPickupAvailableProperties(TypedDict):
    """OrderStatus representing availability of an order for pickup.

    References:
        https://schema.org/OrderPickupAvailable
    Note:
        Model Depth 6
    Attributes:
    """


class OrderPickupAvailableAllProperties(
    OrderPickupAvailableInheritedProperties, OrderPickupAvailableProperties, TypedDict
):
    pass


class OrderPickupAvailableBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OrderPickupAvailable", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OrderPickupAvailableProperties,
        OrderPickupAvailableInheritedProperties,
        OrderPickupAvailableAllProperties,
    ] = OrderPickupAvailableAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderPickupAvailable"
    return model


OrderPickupAvailable = create_schema_org_model()


def create_orderpickupavailable_model(
    model: Union[
        OrderPickupAvailableProperties,
        OrderPickupAvailableInheritedProperties,
        OrderPickupAvailableAllProperties,
    ]
):
    _type = deepcopy(OrderPickupAvailableAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OrderPickupAvailableAllProperties):
    pydantic_type = create_orderpickupavailable_model(model=model)
    return pydantic_type(model).schema_json()
