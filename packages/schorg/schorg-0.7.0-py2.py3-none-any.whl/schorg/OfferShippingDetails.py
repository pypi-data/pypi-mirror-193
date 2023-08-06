"""
OfferShippingDetails represents information about shipping destinations.Multiple of these entities can be used to represent different shipping rates for different destinations:One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.Multiple of these entities can be used to represent different shipping costs and delivery times.Two entities that are identical but differ in rate and time:E.g. Cheaper and slower: $5 in 5-7 daysor Fast and expensive: $15 in 1-2 days.

https://schema.org/OfferShippingDetails
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfferShippingDetailsInheritedProperties(TypedDict):
    """OfferShippingDetails represents information about shipping destinations.Multiple of these entities can be used to represent different shipping rates for different destinations:One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.Multiple of these entities can be used to represent different shipping costs and delivery times.Two entities that are identical but differ in rate and time:E.g. Cheaper and slower: $5 in 5-7 daysor Fast and expensive: $15 in 1-2 days.

    References:
        https://schema.org/OfferShippingDetails
    Note:
        Model Depth 4
    Attributes:
    """

    


class OfferShippingDetailsProperties(TypedDict):
    """OfferShippingDetails represents information about shipping destinations.Multiple of these entities can be used to represent different shipping rates for different destinations:One entity for Alaska/Hawaii. A different one for continental US. A different one for all France.Multiple of these entities can be used to represent different shipping costs and delivery times.Two entities that are identical but differ in rate and time:E.g. Cheaper and slower: $5 in 5-7 daysor Fast and expensive: $15 in 1-2 days.

    References:
        https://schema.org/OfferShippingDetails
    Note:
        Model Depth 4
    Attributes:
        width: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The width of the item.
        shippingSettingsLink: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Link to a page containing [[ShippingRateSettings]] and [[DeliveryTimeSettings]] details.
        depth: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The depth of the item.
        shippingDestination: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): indicates (possibly multiple) shipping destinations. These can be defined in several ways, e.g. postalCode ranges.
        shippingLabel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Label to match an [[OfferShippingDetails]] with a [[ShippingRateSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).
        height: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The height of the item.
        doesNotShip: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates when shipping to a particular [[shippingDestination]] is not available.
        weight: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The weight of the product or person.
        deliveryTime: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The total delay between the receipt of the order and the goods reaching the final customer.
        shippingOrigin: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the origin of a shipment, i.e. where it should be coming from.
        transitTimeLabel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Label to match an [[OfferShippingDetails]] with a [[DeliveryTimeSettings]] (within the context of a [[shippingSettingsLink]] cross-reference).
        shippingRate: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The shipping rate is the cost of shipping to the specified destination. Typically, the maxValue and currency values (of the [[MonetaryAmount]]) are most appropriate.
    """

    width: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    shippingSettingsLink: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    depth: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    shippingDestination: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    shippingLabel: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    height: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    doesNotShip: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    weight: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    deliveryTime: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    shippingOrigin: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    transitTimeLabel: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    shippingRate: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(OfferShippingDetailsInheritedProperties , OfferShippingDetailsProperties, TypedDict):
    pass


class OfferShippingDetailsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OfferShippingDetails",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'width': {'exclude': True}}
        fields = {'shippingSettingsLink': {'exclude': True}}
        fields = {'depth': {'exclude': True}}
        fields = {'shippingDestination': {'exclude': True}}
        fields = {'shippingLabel': {'exclude': True}}
        fields = {'height': {'exclude': True}}
        fields = {'doesNotShip': {'exclude': True}}
        fields = {'weight': {'exclude': True}}
        fields = {'deliveryTime': {'exclude': True}}
        fields = {'shippingOrigin': {'exclude': True}}
        fields = {'transitTimeLabel': {'exclude': True}}
        fields = {'shippingRate': {'exclude': True}}
        


def create_schema_org_model(type_: Union[OfferShippingDetailsProperties, OfferShippingDetailsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OfferShippingDetails"
    return model
    

OfferShippingDetails = create_schema_org_model()


def create_offershippingdetails_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_offershippingdetails_model(model=model)
    return pydantic_type(model).schema_json()


