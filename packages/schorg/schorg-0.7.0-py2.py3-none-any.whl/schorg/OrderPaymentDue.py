"""
OrderStatus representing that payment is due on an order.

https://schema.org/OrderPaymentDue
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderPaymentDueInheritedProperties(TypedDict):
    """OrderStatus representing that payment is due on an order.

    References:
        https://schema.org/OrderPaymentDue
    Note:
        Model Depth 6
    Attributes:
    """

    


class OrderPaymentDueProperties(TypedDict):
    """OrderStatus representing that payment is due on an order.

    References:
        https://schema.org/OrderPaymentDue
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(OrderPaymentDueInheritedProperties , OrderPaymentDueProperties, TypedDict):
    pass


class OrderPaymentDueBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OrderPaymentDue",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OrderPaymentDueProperties, OrderPaymentDueInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderPaymentDue"
    return model
    

OrderPaymentDue = create_schema_org_model()


def create_orderpaymentdue_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_orderpaymentdue_model(model=model)
    return pydantic_type(model).schema_json()


