"""
ShippingDeliveryTime provides various pieces of information about delivery times for shipping.

https://schema.org/ShippingDeliveryTime
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ShippingDeliveryTimeInheritedProperties(TypedDict):
    """ShippingDeliveryTime provides various pieces of information about delivery times for shipping.

    References:
        https://schema.org/ShippingDeliveryTime
    Note:
        Model Depth 4
    Attributes:
    """


class ShippingDeliveryTimeProperties(TypedDict):
    """ShippingDeliveryTime provides various pieces of information about delivery times for shipping.

    References:
        https://schema.org/ShippingDeliveryTime
    Note:
        Model Depth 4
    Attributes:
        cutoffTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): Order cutoff time allows merchants to describe the time after which they will no longer process orders received on that day. For orders processed after cutoff time, one day gets added to the delivery time estimate. This property is expected to be most typically used via the [[ShippingRateSettings]] publication pattern. The time is indicated using the ISO-8601 Time format, e.g. "23:30:00-05:00" would represent 6:30 pm Eastern Standard Time (EST) which is 5 hours behind Coordinated Universal Time (UTC).
        transitTime: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The typical delay the order has been sent for delivery and the goods reach the final customer. Typical properties: minValue, maxValue, unitCode (d for DAY).
        handlingTime: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup. Typical properties: minValue, maxValue, unitCode (d for DAY).  This is by common convention assumed to mean business days (if a unitCode is used, coded as "d"), i.e. only counting days when the business normally operates.
        businessDays: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Days of the week when the merchant typically operates, indicated via opening hours markup.
    """

    cutoffTime: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    transitTime: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    handlingTime: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    businessDays: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ShippingDeliveryTimeAllProperties(
    ShippingDeliveryTimeInheritedProperties, ShippingDeliveryTimeProperties, TypedDict
):
    pass


class ShippingDeliveryTimeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ShippingDeliveryTime", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"cutoffTime": {"exclude": True}}
        fields = {"transitTime": {"exclude": True}}
        fields = {"handlingTime": {"exclude": True}}
        fields = {"businessDays": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ShippingDeliveryTimeProperties,
        ShippingDeliveryTimeInheritedProperties,
        ShippingDeliveryTimeAllProperties,
    ] = ShippingDeliveryTimeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ShippingDeliveryTime"
    return model


ShippingDeliveryTime = create_schema_org_model()


def create_shippingdeliverytime_model(
    model: Union[
        ShippingDeliveryTimeProperties,
        ShippingDeliveryTimeInheritedProperties,
        ShippingDeliveryTimeAllProperties,
    ]
):
    _type = deepcopy(ShippingDeliveryTimeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ShippingDeliveryTimeAllProperties):
    pydantic_type = create_shippingdeliverytime_model(model=model)
    return pydantic_type(model).schema_json()
