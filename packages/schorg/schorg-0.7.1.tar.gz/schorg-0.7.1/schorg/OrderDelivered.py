"""
OrderStatus representing successful delivery of an order.

https://schema.org/OrderDelivered
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderDeliveredInheritedProperties(TypedDict):
    """OrderStatus representing successful delivery of an order.

    References:
        https://schema.org/OrderDelivered
    Note:
        Model Depth 6
    Attributes:
    """

    


class OrderDeliveredProperties(TypedDict):
    """OrderStatus representing successful delivery of an order.

    References:
        https://schema.org/OrderDelivered
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(OrderDeliveredInheritedProperties , OrderDeliveredProperties, TypedDict):
    pass


class OrderDeliveredBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OrderDelivered",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OrderDeliveredProperties, OrderDeliveredInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderDelivered"
    return model
    

OrderDelivered = create_schema_org_model()


def create_orderdelivered_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_orderdelivered_model(model=model)
    return pydantic_type(model).schema_json()


