"""
An order item is a line of an order. It includes the quantity and shipping details of a bought offer.

https://schema.org/OrderItem
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OrderItemInheritedProperties(TypedDict):
    """An order item is a line of an order. It includes the quantity and shipping details of a bought offer.

    References:
        https://schema.org/OrderItem
    Note:
        Model Depth 3
    Attributes:
    """

    


class OrderItemProperties(TypedDict):
    """An order item is a line of an order. It includes the quantity and shipping details of a bought offer.

    References:
        https://schema.org/OrderItem
    Note:
        Model Depth 3
    Attributes:
        orderItemStatus: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The current status of the order item.
        orderQuantity: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The number of the item ordered. If the property is not set, assume the quantity is one.
        orderDelivery: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The delivery of the parcel related to this order or order item.
        orderedItem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The item ordered.
        orderItemNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The identifier of the order item.
    """

    orderItemStatus: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    orderQuantity: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    orderDelivery: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    orderedItem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    orderItemNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(OrderItemInheritedProperties , OrderItemProperties, TypedDict):
    pass


class OrderItemBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OrderItem",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'orderItemStatus': {'exclude': True}}
        fields = {'orderQuantity': {'exclude': True}}
        fields = {'orderDelivery': {'exclude': True}}
        fields = {'orderedItem': {'exclude': True}}
        fields = {'orderItemNumber': {'exclude': True}}
        


def create_schema_org_model(type_: Union[OrderItemProperties, OrderItemInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OrderItem"
    return model
    

OrderItem = create_schema_org_model()


def create_orderitem_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_orderitem_model(model=model)
    return pydantic_type(model).schema_json()


