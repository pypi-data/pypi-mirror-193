"""
The delivery of a parcel either via the postal service or a commercial service.

https://schema.org/ParcelDelivery
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ParcelDeliveryInheritedProperties(TypedDict):
    """The delivery of a parcel either via the postal service or a commercial service.

    References:
        https://schema.org/ParcelDelivery
    Note:
        Model Depth 3
    Attributes:
    """


class ParcelDeliveryProperties(TypedDict):
    """The delivery of a parcel either via the postal service or a commercial service.

    References:
        https://schema.org/ParcelDelivery
    Note:
        Model Depth 3
    Attributes:
        itemShipped: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Item(s) being shipped.
        trackingNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Shipper tracking number.
        expectedArrivalUntil: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The latest date the package may arrive.
        provider: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        deliveryAddress: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Destination address.
        expectedArrivalFrom: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The earliest date the package may arrive.
        carrier: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): 'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.
        originAddress: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Shipper's address.
        deliveryStatus: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): New entry added as the package passes through each leg of its journey (from shipment to final delivery).
        trackingUrl: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Tracking url for the parcel delivery.
        partOfOrder: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The overall order the items in this delivery were included in.
        hasDeliveryMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Method used for delivery or shipping.
    """

    itemShipped: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    trackingNumber: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    expectedArrivalUntil: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    provider: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    deliveryAddress: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    expectedArrivalFrom: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    carrier: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    originAddress: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    deliveryStatus: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    trackingUrl: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    partOfOrder: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hasDeliveryMethod: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class ParcelDeliveryAllProperties(
    ParcelDeliveryInheritedProperties, ParcelDeliveryProperties, TypedDict
):
    pass


class ParcelDeliveryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ParcelDelivery", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"itemShipped": {"exclude": True}}
        fields = {"trackingNumber": {"exclude": True}}
        fields = {"expectedArrivalUntil": {"exclude": True}}
        fields = {"provider": {"exclude": True}}
        fields = {"deliveryAddress": {"exclude": True}}
        fields = {"expectedArrivalFrom": {"exclude": True}}
        fields = {"carrier": {"exclude": True}}
        fields = {"originAddress": {"exclude": True}}
        fields = {"deliveryStatus": {"exclude": True}}
        fields = {"trackingUrl": {"exclude": True}}
        fields = {"partOfOrder": {"exclude": True}}
        fields = {"hasDeliveryMethod": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ParcelDeliveryProperties,
        ParcelDeliveryInheritedProperties,
        ParcelDeliveryAllProperties,
    ] = ParcelDeliveryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ParcelDelivery"
    return model


ParcelDelivery = create_schema_org_model()


def create_parceldelivery_model(
    model: Union[
        ParcelDeliveryProperties,
        ParcelDeliveryInheritedProperties,
        ParcelDeliveryAllProperties,
    ]
):
    _type = deepcopy(ParcelDeliveryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ParcelDeliveryAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ParcelDeliveryAllProperties):
    pydantic_type = create_parceldelivery_model(model=model)
    return pydantic_type(model).schema_json()
