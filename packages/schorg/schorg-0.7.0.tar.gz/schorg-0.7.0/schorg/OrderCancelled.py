"""
OrderStatus representing cancellation of an order.

https://schema.org/OrderCancelled
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(OrderCancelledInheritedProperties , OrderCancelledProperties, TypedDict):
    pass


class OrderCancelledBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OrderCancelled",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OrderCancelledProperties, OrderCancelledInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderCancelled"
    return model
    

OrderCancelled = create_schema_org_model()


def create_ordercancelled_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_ordercancelled_model(model=model)
    return pydantic_type(model).schema_json()


