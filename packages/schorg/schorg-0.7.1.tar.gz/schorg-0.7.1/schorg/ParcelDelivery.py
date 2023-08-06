"""
The delivery of a parcel either via the postal service or a commercial service.

https://schema.org/ParcelDelivery
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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
        itemShipped: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Item(s) being shipped.
        trackingNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Shipper tracking number.
        expectedArrivalUntil: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The latest date the package may arrive.
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        deliveryAddress: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Destination address.
        expectedArrivalFrom: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The earliest date the package may arrive.
        carrier: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): 'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.
        originAddress: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Shipper's address.
        deliveryStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): New entry added as the package passes through each leg of its journey (from shipment to final delivery).
        trackingUrl: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Tracking url for the parcel delivery.
        partOfOrder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The overall order the items in this delivery were included in.
        hasDeliveryMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Method used for delivery or shipping.
    """

    itemShipped: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    trackingNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    expectedArrivalUntil: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    deliveryAddress: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    expectedArrivalFrom: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    carrier: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    originAddress: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    deliveryStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    trackingUrl: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    partOfOrder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasDeliveryMethod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(ParcelDeliveryInheritedProperties , ParcelDeliveryProperties, TypedDict):
    pass


class ParcelDeliveryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ParcelDelivery",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'itemShipped': {'exclude': True}}
        fields = {'trackingNumber': {'exclude': True}}
        fields = {'expectedArrivalUntil': {'exclude': True}}
        fields = {'provider': {'exclude': True}}
        fields = {'deliveryAddress': {'exclude': True}}
        fields = {'expectedArrivalFrom': {'exclude': True}}
        fields = {'carrier': {'exclude': True}}
        fields = {'originAddress': {'exclude': True}}
        fields = {'deliveryStatus': {'exclude': True}}
        fields = {'trackingUrl': {'exclude': True}}
        fields = {'partOfOrder': {'exclude': True}}
        fields = {'hasDeliveryMethod': {'exclude': True}}
        


def create_schema_org_model(type_: Union[ParcelDeliveryProperties, ParcelDeliveryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ParcelDelivery"
    return model
    

ParcelDelivery = create_schema_org_model()


def create_parceldelivery_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_parceldelivery_model(model=model)
    return pydantic_type(model).schema_json()


