"""
OrderStatus representing that an order is being processed.

https://schema.org/OrderProcessing
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(OrderProcessingInheritedProperties , OrderProcessingProperties, TypedDict):
    pass


class OrderProcessingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OrderProcessing",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OrderProcessingProperties, OrderProcessingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderProcessing"
    return model
    

OrderProcessing = create_schema_org_model()


def create_orderprocessing_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_orderprocessing_model(model=model)
    return pydantic_type(model).schema_json()


