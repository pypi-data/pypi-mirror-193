"""
When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.

https://schema.org/AggregateOffer
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AggregateOfferInheritedProperties(TypedDict):
    """When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.

    References:
        https://schema.org/AggregateOffer
    Note:
        Model Depth 4
    Attributes:
        hasMeasurement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A product measurement, for example the inseam of pants, the wheel size of a bicycle, or the gauge of a screw. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        eligibleQuantity: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.
        deliveryLeadTime: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.
        availabilityEnds: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The end of the availability of the product or service included in the offer.
        seller: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        availabilityStarts: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The beginning of the availability of the product or service included in the offer.
        areaServed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The geographic area where a service or offered item is provided.
        advanceBookingRequirement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The amount of time that is required between accepting the offer and the actual usage of the resource or service.
        priceValidUntil: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): The date after which the price is no longer available.
        gtin14: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        reviews: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Review of the item.
        warranty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The warranty promise(s) included in the offer.
        inventoryLevel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The current approximate inventory level for the item or items.
        eligibleDuration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration for which the given offer is valid.
        availability: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.
        itemCondition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        checkoutPageURLTemplate: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A URL template (RFC 6570) for a checkout page for an offer. This approach allows merchants to specify a URL for online checkout of the offered product, by interpolating parameters such as the logged in user ID, product ID, quantity, discount code etc. Parameter naming and standardization are not specified here.
        price: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.      
        review: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A review of the item.
        gtin: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) express GTINs as URLs (URIs, IRIs, etc.). Details including regular expression examples can be found in, Section 6 of the GS1 URI Syntax specification; see also [schema.org tracking issue](https://github.com/schemaorg/schemaorg/issues/3156#issuecomment-1209522809) for schema.org-specific discussion. A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.
        itemOffered: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An item being offered (or demanded). The transactional nature of the offer or demand is documented using [[businessFunction]], e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        mobileUrl: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The [[mobileUrl]] property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.To discourage over-use, and reflecting intial usecases, the property is expected only on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [[url]] property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]] for more mobile-oriented pages. The property is intended for the case when items (primarily [[Product]] and [[Offer]]) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.    
        shippingDetails: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates information about the shipping policies and options associated with an [[Offer]].
        hasMerchantReturnPolicy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifies a MerchantReturnPolicy that may be applicable.
        businessFunction: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.
        isFamilyFriendly: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether this content is family friendly.
        leaseLength: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.
        gtin12: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        validThrough: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        hasAdultConsideration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Used to tag an item to be intended or suitable for consumption or use by adults only.
        includesObject: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): This links to a node or nodes indicating the exact quantity of the products included in  an [[Offer]] or [[ProductCollection]].
        eligibleRegion: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.See also [[ineligibleRegion]].    
        asin: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.
        gtin8: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        ineligibleRegion: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.See also [[eligibleRegion]].      
        priceSpecification: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): One or more detailed price specifications, indicating the unit price and delivery or payment charges.
        validFrom: (Optional[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]): The date when the item becomes valid.
        eligibleTransactionVolume: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.
        mpn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
        category: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        aggregateRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The overall rating, based on a collection of reviews or ratings, of the item.
        offeredBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A pointer to the organization or person making the offer.
        addOn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).
        availableAtOrFrom: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The place(s) from which the offer can be obtained (e.g. store locations).
        priceCurrency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        eligibleCustomerType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type(s) of customers for which the given offer is valid.
        gtin13: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        serialNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.
        sku: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.
        acceptedPaymentMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The payment method(s) accepted by seller for this offer.
        availableDeliveryMethod: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The delivery method(s) available for this offer.
    """

    hasMeasurement: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    eligibleQuantity: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    deliveryLeadTime: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    availabilityEnds: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    seller: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    availabilityStarts: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    areaServed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    advanceBookingRequirement: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    priceValidUntil: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    gtin14: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    reviews: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    warranty: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    inventoryLevel: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    eligibleDuration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    availability: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    itemCondition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    checkoutPageURLTemplate: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    price: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    review: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gtin: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    itemOffered: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    mobileUrl: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    shippingDetails: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hasMerchantReturnPolicy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    businessFunction: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isFamilyFriendly: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    leaseLength: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gtin12: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    validThrough: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    hasAdultConsideration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    includesObject: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    eligibleRegion: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    asin: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    gtin8: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    ineligibleRegion: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    priceSpecification: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    validFrom: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str, date]], datetime, SchemaOrgObj, str, date]]
    eligibleTransactionVolume: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    mpn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    category: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    aggregateRating: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    offeredBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    addOn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    availableAtOrFrom: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    priceCurrency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    eligibleCustomerType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gtin13: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    serialNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sku: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    acceptedPaymentMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    availableDeliveryMethod: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AggregateOfferProperties(TypedDict):
    """When a single product is associated with multiple offers (for example, the same pair of shoes is offered by different merchants), then AggregateOffer can be used.Note: AggregateOffers are normally expected to associate multiple offers that all share the same defined [[businessFunction]] value, or default to http://purl.org/goodrelations/v1#Sell if businessFunction is not explicitly defined.

    References:
        https://schema.org/AggregateOffer
    Note:
        Model Depth 4
    Attributes:
        highPrice: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The highest price of all offers available.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        offerCount: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): The number of offers for the product.
        lowPrice: (Optional[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]): The lowest price of all offers available.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        offers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.      
    """

    highPrice: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    offerCount: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    lowPrice: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictInt, StrictFloat]], SchemaOrgObj, str, StrictInt, StrictFloat]]
    offers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(AggregateOfferInheritedProperties , AggregateOfferProperties, TypedDict):
    pass


class AggregateOfferBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AggregateOffer",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'hasMeasurement': {'exclude': True}}
        fields = {'eligibleQuantity': {'exclude': True}}
        fields = {'deliveryLeadTime': {'exclude': True}}
        fields = {'availabilityEnds': {'exclude': True}}
        fields = {'seller': {'exclude': True}}
        fields = {'availabilityStarts': {'exclude': True}}
        fields = {'areaServed': {'exclude': True}}
        fields = {'advanceBookingRequirement': {'exclude': True}}
        fields = {'priceValidUntil': {'exclude': True}}
        fields = {'gtin14': {'exclude': True}}
        fields = {'reviews': {'exclude': True}}
        fields = {'warranty': {'exclude': True}}
        fields = {'inventoryLevel': {'exclude': True}}
        fields = {'eligibleDuration': {'exclude': True}}
        fields = {'availability': {'exclude': True}}
        fields = {'itemCondition': {'exclude': True}}
        fields = {'checkoutPageURLTemplate': {'exclude': True}}
        fields = {'price': {'exclude': True}}
        fields = {'review': {'exclude': True}}
        fields = {'gtin': {'exclude': True}}
        fields = {'itemOffered': {'exclude': True}}
        fields = {'mobileUrl': {'exclude': True}}
        fields = {'shippingDetails': {'exclude': True}}
        fields = {'hasMerchantReturnPolicy': {'exclude': True}}
        fields = {'businessFunction': {'exclude': True}}
        fields = {'isFamilyFriendly': {'exclude': True}}
        fields = {'leaseLength': {'exclude': True}}
        fields = {'gtin12': {'exclude': True}}
        fields = {'validThrough': {'exclude': True}}
        fields = {'hasAdultConsideration': {'exclude': True}}
        fields = {'includesObject': {'exclude': True}}
        fields = {'eligibleRegion': {'exclude': True}}
        fields = {'asin': {'exclude': True}}
        fields = {'gtin8': {'exclude': True}}
        fields = {'ineligibleRegion': {'exclude': True}}
        fields = {'priceSpecification': {'exclude': True}}
        fields = {'validFrom': {'exclude': True}}
        fields = {'eligibleTransactionVolume': {'exclude': True}}
        fields = {'mpn': {'exclude': True}}
        fields = {'category': {'exclude': True}}
        fields = {'aggregateRating': {'exclude': True}}
        fields = {'offeredBy': {'exclude': True}}
        fields = {'addOn': {'exclude': True}}
        fields = {'availableAtOrFrom': {'exclude': True}}
        fields = {'priceCurrency': {'exclude': True}}
        fields = {'eligibleCustomerType': {'exclude': True}}
        fields = {'gtin13': {'exclude': True}}
        fields = {'serialNumber': {'exclude': True}}
        fields = {'sku': {'exclude': True}}
        fields = {'acceptedPaymentMethod': {'exclude': True}}
        fields = {'availableDeliveryMethod': {'exclude': True}}
        fields = {'highPrice': {'exclude': True}}
        fields = {'offerCount': {'exclude': True}}
        fields = {'lowPrice': {'exclude': True}}
        fields = {'offers': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AggregateOfferProperties, AggregateOfferInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AggregateOffer"
    return model
    

AggregateOffer = create_schema_org_model()


def create_aggregateoffer_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_aggregateoffer_model(model=model)
    return pydantic_type(model).schema_json()


