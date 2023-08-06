"""
A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.

https://schema.org/Demand
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DemandInheritedProperties(TypedDict):
    """A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.

    References:
        https://schema.org/Demand
    Note:
        Model Depth 3
    Attributes:
    """

    


class DemandProperties(TypedDict):
    """A demand entity represents the public, not necessarily binding, not necessarily exclusive, announcement by an organization or person to seek a certain type of goods or services. For describing demand using this type, the very same properties used for Offer apply.

    References:
        https://schema.org/Demand
    Note:
        Model Depth 3
    Attributes:
        eligibleQuantity: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.
        deliveryLeadTime: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.
        availabilityEnds: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end of the availability of the product or service included in the offer.
        seller: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        availabilityStarts: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The beginning of the availability of the product or service included in the offer.
        areaServed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where a service or offered item is provided.
        advanceBookingRequirement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The amount of time that is required between accepting the offer and the actual usage of the resource or service.
        gtin14: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        warranty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The warranty promise(s) included in the offer.
        inventoryLevel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The current approximate inventory level for the item or items.
        eligibleDuration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration for which the given offer is valid.
        availability: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.
        itemCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        gtin: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) express GTINs as URLs (URIs, IRIs, etc.). Details including regular expression examples can be found in, Section 6 of the GS1 URI Syntax specification; see also [schema.org tracking issue](https://github.com/schemaorg/schemaorg/issues/3156#issuecomment-1209522809) for schema.org-specific discussion. A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.
        itemOffered: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An item being offered (or demanded). The transactional nature of the offer or demand is documented using [[businessFunction]], e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        businessFunction: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.
        gtin12: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        validThrough: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        includesObject: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This links to a node or nodes indicating the exact quantity of the products included in  an [[Offer]] or [[ProductCollection]].
        eligibleRegion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.See also [[ineligibleRegion]].    
        asin: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.
        gtin8: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        ineligibleRegion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.See also [[eligibleRegion]].      
        priceSpecification: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One or more detailed price specifications, indicating the unit price and delivery or payment charges.
        validFrom: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The date when the item becomes valid.
        eligibleTransactionVolume: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.
        mpn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
        availableAtOrFrom: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The place(s) from which the offer can be obtained (e.g. store locations).
        eligibleCustomerType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type(s) of customers for which the given offer is valid.
        gtin13: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        serialNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.
        sku: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.
        acceptedPaymentMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The payment method(s) accepted by seller for this offer.
        availableDeliveryMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The delivery method(s) available for this offer.
    """

    eligibleQuantity: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    deliveryLeadTime: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availabilityEnds: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    seller: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availabilityStarts: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    areaServed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    advanceBookingRequirement: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin14: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    warranty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    inventoryLevel: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    eligibleDuration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availability: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    itemCondition: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    itemOffered: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    businessFunction: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin12: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    validThrough: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    includesObject: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    eligibleRegion: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    asin: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    gtin8: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ineligibleRegion: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    priceSpecification: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    validFrom: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    eligibleTransactionVolume: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    mpn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availableAtOrFrom: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    eligibleCustomerType: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin13: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    serialNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sku: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    acceptedPaymentMethod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availableDeliveryMethod: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(DemandInheritedProperties , DemandProperties, TypedDict):
    pass


class DemandBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Demand",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'eligibleQuantity': {'exclude': True}}
        fields = {'deliveryLeadTime': {'exclude': True}}
        fields = {'availabilityEnds': {'exclude': True}}
        fields = {'seller': {'exclude': True}}
        fields = {'availabilityStarts': {'exclude': True}}
        fields = {'areaServed': {'exclude': True}}
        fields = {'advanceBookingRequirement': {'exclude': True}}
        fields = {'gtin14': {'exclude': True}}
        fields = {'warranty': {'exclude': True}}
        fields = {'inventoryLevel': {'exclude': True}}
        fields = {'eligibleDuration': {'exclude': True}}
        fields = {'availability': {'exclude': True}}
        fields = {'itemCondition': {'exclude': True}}
        fields = {'gtin': {'exclude': True}}
        fields = {'itemOffered': {'exclude': True}}
        fields = {'businessFunction': {'exclude': True}}
        fields = {'gtin12': {'exclude': True}}
        fields = {'validThrough': {'exclude': True}}
        fields = {'includesObject': {'exclude': True}}
        fields = {'eligibleRegion': {'exclude': True}}
        fields = {'asin': {'exclude': True}}
        fields = {'gtin8': {'exclude': True}}
        fields = {'ineligibleRegion': {'exclude': True}}
        fields = {'priceSpecification': {'exclude': True}}
        fields = {'validFrom': {'exclude': True}}
        fields = {'eligibleTransactionVolume': {'exclude': True}}
        fields = {'mpn': {'exclude': True}}
        fields = {'availableAtOrFrom': {'exclude': True}}
        fields = {'eligibleCustomerType': {'exclude': True}}
        fields = {'gtin13': {'exclude': True}}
        fields = {'serialNumber': {'exclude': True}}
        fields = {'sku': {'exclude': True}}
        fields = {'acceptedPaymentMethod': {'exclude': True}}
        fields = {'availableDeliveryMethod': {'exclude': True}}
        


def create_schema_org_model(type_: Union[DemandProperties, DemandInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Demand"
    return model
    

Demand = create_schema_org_model()


def create_demand_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_demand_model(model=model)
    return pydantic_type(model).schema_json()


