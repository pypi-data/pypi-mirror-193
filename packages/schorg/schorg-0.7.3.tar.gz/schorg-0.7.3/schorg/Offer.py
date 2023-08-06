"""
An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.Note: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).

https://schema.org/Offer
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfferInheritedProperties(TypedDict):
    """An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.Note: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).

    References:
        https://schema.org/Offer
    Note:
        Model Depth 3
    Attributes:
    """


class OfferProperties(TypedDict):
    """An offer to transfer some rights to an item or to provide a service — for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.Note: As the [[businessFunction]] property, which identifies the form of offer (e.g. sell, lease, repair, dispose), defaults to http://purl.org/goodrelations/v1#Sell; an Offer without a defined businessFunction value can be assumed to be an offer to sell.For [GTIN](http://www.gs1.org/barcodes/technical/idkeys/gtin)-related fields, see [Check Digit calculator](http://www.gs1.org/barcodes/support/check_digit_calculator) and [validation guide](http://www.gs1us.org/resources/standards/gtin-validation-guide) from [GS1](http://www.gs1.org/).

    References:
        https://schema.org/Offer
    Note:
        Model Depth 3
    Attributes:
        hasMeasurement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A product measurement, for example the inseam of pants, the wheel size of a bicycle, or the gauge of a screw. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        eligibleQuantity: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.
        deliveryLeadTime: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The typical delay between the receipt of the order and the goods either leaving the warehouse or being prepared for pickup, in case the delivery method is on site pickup.
        availabilityEnds: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The end of the availability of the product or service included in the offer.
        seller: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        availabilityStarts: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The beginning of the availability of the product or service included in the offer.
        areaServed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where a service or offered item is provided.
        advanceBookingRequirement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The amount of time that is required between accepting the offer and the actual usage of the resource or service.
        priceValidUntil: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date after which the price is no longer available.
        gtin14: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        reviews: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Review of the item.
        warranty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The warranty promise(s) included in the offer.
        inventoryLevel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The current approximate inventory level for the item or items.
        eligibleDuration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration for which the given offer is valid.
        availability: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.
        itemCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        checkoutPageURLTemplate: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A URL template (RFC 6570) for a checkout page for an offer. This approach allows merchants to specify a URL for online checkout of the offered product, by interpolating parameters such as the logged in user ID, product ID, quantity, discount code etc. Parameter naming and standardization are not specified here.
        price: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
        review: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A review of the item.
        gtin: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) express GTINs as URLs (URIs, IRIs, etc.). Details including regular expression examples can be found in, Section 6 of the GS1 URI Syntax specification; see also [schema.org tracking issue](https://github.com/schemaorg/schemaorg/issues/3156#issuecomment-1209522809) for schema.org-specific discussion. A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.
        itemOffered: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An item being offered (or demanded). The transactional nature of the offer or demand is documented using [[businessFunction]], e.g. sell, lease etc. While several common expected types are listed explicitly in this definition, others can be used. Using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        mobileUrl: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The [[mobileUrl]] property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.To discourage over-use, and reflecting intial usecases, the property is expected only on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [[url]] property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]] for more mobile-oriented pages. The property is intended for the case when items (primarily [[Product]] and [[Offer]]) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.
        shippingDetails: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates information about the shipping policies and options associated with an [[Offer]].
        hasMerchantReturnPolicy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies a MerchantReturnPolicy that may be applicable.
        businessFunction: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.
        isFamilyFriendly: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): Indicates whether this content is family friendly.
        leaseLength: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.
        gtin12: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        validThrough: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.
        hasAdultConsideration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Used to tag an item to be intended or suitable for consumption or use by adults only.
        includesObject: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This links to a node or nodes indicating the exact quantity of the products included in  an [[Offer]] or [[ProductCollection]].
        eligibleRegion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.See also [[ineligibleRegion]].
        asin: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.
        gtin8: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        ineligibleRegion: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.See also [[eligibleRegion]].
        priceSpecification: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One or more detailed price specifications, indicating the unit price and delivery or payment charges.
        validFrom: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The date when the item becomes valid.
        eligibleTransactionVolume: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.
        mpn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
        category: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        aggregateRating: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The overall rating, based on a collection of reviews or ratings, of the item.
        offeredBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to the organization or person making the offer.
        addOn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).
        availableAtOrFrom: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The place(s) from which the offer can be obtained (e.g. store locations).
        priceCurrency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        eligibleCustomerType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type(s) of customers for which the given offer is valid.
        gtin13: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        serialNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.
        sku: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.
        acceptedPaymentMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The payment method(s) accepted by seller for this offer.
        availableDeliveryMethod: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The delivery method(s) available for this offer.
    """

    hasMeasurement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    eligibleQuantity: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    deliveryLeadTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    availabilityEnds: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    seller: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availabilityStarts: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    areaServed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    advanceBookingRequirement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    priceValidUntil: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    gtin14: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reviews: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    warranty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    inventoryLevel: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    eligibleDuration: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    availability: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    itemCondition: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    checkoutPageURLTemplate: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    price: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    review: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    itemOffered: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    mobileUrl: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    shippingDetails: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    hasMerchantReturnPolicy: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    businessFunction: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    isFamilyFriendly: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]
    leaseLength: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin12: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    validThrough: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    hasAdultConsideration: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    includesObject: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    eligibleRegion: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    asin: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    gtin8: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ineligibleRegion: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    priceSpecification: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    validFrom: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    eligibleTransactionVolume: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    mpn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    category: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    aggregateRating: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    offeredBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    addOn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    availableAtOrFrom: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    priceCurrency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    eligibleCustomerType: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    gtin13: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    serialNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sku: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    acceptedPaymentMethod: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    availableDeliveryMethod: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class OfferAllProperties(OfferInheritedProperties, OfferProperties, TypedDict):
    pass


class OfferBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Offer", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"hasMeasurement": {"exclude": True}}
        fields = {"eligibleQuantity": {"exclude": True}}
        fields = {"deliveryLeadTime": {"exclude": True}}
        fields = {"availabilityEnds": {"exclude": True}}
        fields = {"seller": {"exclude": True}}
        fields = {"availabilityStarts": {"exclude": True}}
        fields = {"areaServed": {"exclude": True}}
        fields = {"advanceBookingRequirement": {"exclude": True}}
        fields = {"priceValidUntil": {"exclude": True}}
        fields = {"gtin14": {"exclude": True}}
        fields = {"reviews": {"exclude": True}}
        fields = {"warranty": {"exclude": True}}
        fields = {"inventoryLevel": {"exclude": True}}
        fields = {"eligibleDuration": {"exclude": True}}
        fields = {"availability": {"exclude": True}}
        fields = {"itemCondition": {"exclude": True}}
        fields = {"checkoutPageURLTemplate": {"exclude": True}}
        fields = {"price": {"exclude": True}}
        fields = {"review": {"exclude": True}}
        fields = {"gtin": {"exclude": True}}
        fields = {"itemOffered": {"exclude": True}}
        fields = {"mobileUrl": {"exclude": True}}
        fields = {"shippingDetails": {"exclude": True}}
        fields = {"hasMerchantReturnPolicy": {"exclude": True}}
        fields = {"businessFunction": {"exclude": True}}
        fields = {"isFamilyFriendly": {"exclude": True}}
        fields = {"leaseLength": {"exclude": True}}
        fields = {"gtin12": {"exclude": True}}
        fields = {"validThrough": {"exclude": True}}
        fields = {"hasAdultConsideration": {"exclude": True}}
        fields = {"includesObject": {"exclude": True}}
        fields = {"eligibleRegion": {"exclude": True}}
        fields = {"asin": {"exclude": True}}
        fields = {"gtin8": {"exclude": True}}
        fields = {"ineligibleRegion": {"exclude": True}}
        fields = {"priceSpecification": {"exclude": True}}
        fields = {"validFrom": {"exclude": True}}
        fields = {"eligibleTransactionVolume": {"exclude": True}}
        fields = {"mpn": {"exclude": True}}
        fields = {"category": {"exclude": True}}
        fields = {"aggregateRating": {"exclude": True}}
        fields = {"offeredBy": {"exclude": True}}
        fields = {"addOn": {"exclude": True}}
        fields = {"availableAtOrFrom": {"exclude": True}}
        fields = {"priceCurrency": {"exclude": True}}
        fields = {"eligibleCustomerType": {"exclude": True}}
        fields = {"gtin13": {"exclude": True}}
        fields = {"serialNumber": {"exclude": True}}
        fields = {"sku": {"exclude": True}}
        fields = {"acceptedPaymentMethod": {"exclude": True}}
        fields = {"availableDeliveryMethod": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OfferProperties, OfferInheritedProperties, OfferAllProperties
    ] = OfferAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Offer"
    return model


Offer = create_schema_org_model()


def create_offer_model(
    model: Union[OfferProperties, OfferInheritedProperties, OfferAllProperties]
):
    _type = deepcopy(OfferAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OfferAllProperties):
    pydantic_type = create_offer_model(model=model)
    return pydantic_type(model).schema_json()
