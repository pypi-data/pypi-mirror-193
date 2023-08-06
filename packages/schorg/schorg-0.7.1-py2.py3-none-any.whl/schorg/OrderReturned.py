"""
OrderStatus representing that an order has been returned.

https://schema.org/OrderReturned
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(OrderReturnedInheritedProperties , OrderReturnedProperties, TypedDict):
    pass


class OrderReturnedBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OrderReturned",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OrderReturnedProperties, OrderReturnedInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderReturned"
    return model
    

OrderReturned = create_schema_org_model()


def create_orderreturned_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_orderreturned_model(model=model)
    return pydantic_type(model).schema_json()


