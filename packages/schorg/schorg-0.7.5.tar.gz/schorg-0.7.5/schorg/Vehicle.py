"""
A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.

https://schema.org/Vehicle
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VehicleInheritedProperties(TypedDict):
    """A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.

    References:
        https://schema.org/Vehicle
    Note:
        Model Depth 3
    Attributes:
        hasMeasurement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A product measurement, for example the inseam of pants, the wheel size of a bicycle, or the gauge of a screw. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        countryOfAssembly: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The place where the product was assembled.
        width: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The width of the item.
        isAccessoryOrSparePartFor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to another product (or multiple products) for which this product is an accessory or spare part.
        isConsumableFor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to another product (or multiple products) for which this product is a consumable.
        depth: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The depth of the item.
        additionalProperty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
        isVariantOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the kind of product that this is a variant of. In the case of [[ProductModel]], this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with [[ProductGroup]], this property can apply to any [[Product]] included in the group.
        slogan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A slogan or motto associated with the item.
        manufacturer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The manufacturer of the product.
        gtin14: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        keywords: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        positiveNotes: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Provides positive considerations regarding something, for example product highlights or (alongside [[negativeNotes]]) pro/con lists for reviews.In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).
        reviews: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Review of the item.
        height: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The height of the item.
        model: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.
        itemCondition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        award: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An award won by or for this item.
        nsn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number) (nsn) of a [[Product]].
        awards: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Awards won by or for this item.
        review: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A review of the item.
        gtin: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) express GTINs as URLs (URIs, IRIs, etc.). Details including regular expression examples can be found in, Section 6 of the GS1 URI Syntax specification; see also [schema.org tracking issue](https://github.com/schemaorg/schemaorg/issues/3156#issuecomment-1209522809) for schema.org-specific discussion. A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.
        isRelatedTo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to another, somehow related product (or multiple products).
        negativeNotes: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Provides negative considerations regarding something, most typically in pro/con lists for reviews (alongside [[positiveNotes]]). For symmetry In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]] used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used on [[Product]].The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).
        funding: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        mobileUrl: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The [[mobileUrl]] property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.To discourage over-use, and reflecting intial usecases, the property is expected only on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [[url]] property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]] for more mobile-oriented pages. The property is intended for the case when items (primarily [[Product]] and [[Offer]]) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.
        hasEnergyConsumptionDetails: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Defines the energy efficiency Category (also known as "class" or "rating") for a product according to an international energy efficiency standard.
        weight: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The weight of the product or person.
        hasMerchantReturnPolicy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies a MerchantReturnPolicy that may be applicable.
        pattern: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'. Values are typically expressed as text, although links to controlled value schemes are also supported.
        isFamilyFriendly: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): Indicates whether this content is family friendly.
        gtin12: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        isSimilarTo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to another, functionally similar product (or multiple products).
        productID: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The product identifier, such as ISBN. For example: ``` meta itemprop="productID" content="isbn:123-456-789" ```.
        countryOfOrigin: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The country of origin of something, including products as well as creative  works such as movie and TV content.In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.
        hasAdultConsideration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Used to tag an item to be intended or suitable for consumption or use by adults only.
        purchaseDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date the item, e.g. vehicle, was purchased by the current owner.
        audience: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An intended audience, i.e. a group for whom something was created.
        logo: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An associated logo.
        countryOfLastProcessing: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The place where the item (typically [[Product]]) was last processed and tested before importation.
        asin: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.
        gtin8: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        releaseDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The release date of a product or product model. This can be used to distinguish the exact variant of a product.
        brand: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
        productionDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date of production of the item, e.g. vehicle.
        inProductGroupWithID: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]].
        size: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A standardized size of a product or creative work, specified either through a simple textual string (for example 'XL', '32Wx34L'), a  QuantitativeValue with a unitCode, or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]], [[height]], [[depth]] and [[weight]] properties may be more applicable.
        mpn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
        category: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        aggregateRating: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The overall rating, based on a collection of reviews or ratings, of the item.
        color: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The color of the product.
        material: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A material that something is made from, e.g. leather, wool, cotton, paper.
        offers: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        gtin13: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        sku: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.
    """

    hasMeasurement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    countryOfAssembly: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    width: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isAccessoryOrSparePartFor: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    isConsumableFor: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    depth: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    additionalProperty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    isVariantOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    slogan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    manufacturer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin14: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    keywords: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    positiveNotes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reviews: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    height: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    model: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    itemCondition: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    award: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    nsn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    awards: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    review: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    isRelatedTo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    negativeNotes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    mobileUrl: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasEnergyConsumptionDetails: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    weight: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasMerchantReturnPolicy: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    pattern: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isFamilyFriendly: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]
    gtin12: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isSimilarTo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    productID: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    countryOfOrigin: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    hasAdultConsideration: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    purchaseDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    audience: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    logo: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    countryOfLastProcessing: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    asin: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    gtin8: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    releaseDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    brand: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    productionDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    inProductGroupWithID: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    size: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    mpn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    category: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    aggregateRating: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    color: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    material: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    offers: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gtin13: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    sku: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class VehicleProperties(TypedDict):
    """A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.

    References:
        https://schema.org/Vehicle
    Note:
        Model Depth 3
    Attributes:
        vehicleSpecialUsage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale.
        trailerWeight: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The permitted weight of a trailer attached to the vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        cargoVolume: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.Typical unit code(s): LTR for liters, FTQ for cubic foot/feetNote: You can use [[minValue]] and [[maxValue]] to indicate ranges.
        steeringPosition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The position of the steering wheel or similar device (mostly for cars).
        fuelConsumption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km).* Note 1: There are unfortunately no standard unit codes for liters per 100 km.  Use [[unitText]] to indicate the unit of measurement, e.g. L/100 km.* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel consumption to another value.
        modelDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The release date of a vehicle model (often used to differentiate versions of the same make and model).
        vehicleTransmission: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars).
        emissionsCO2: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The CO2 emissions in g/km. When used in combination with a QuantitativeValue, put "g/km" into the unitText property of that value, since there is no UN/CEFACT Common Code for "g/km".
        meetsEmissionStandard: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates that the vehicle meets the respective emission standard.
        payload: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The permitted weight of passengers and cargo, EXCLUDING the weight of the empty vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: Many databases specify the permitted TOTAL weight instead, which is the sum of [[weight]] and [[payload]]* Note 2: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 3: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 4: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        fuelCapacity: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The capacity of the fuel tank or in the case of electric cars, the battery. If there are multiple components for storage, this should indicate the total of all storage of the same type.Typical unit code(s): LTR for liters, GLL of US gallons, GLI for UK / imperial gallons, AMH for ampere-hours (for electrical vehicles).
        wheelbase: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The distance between the centers of the front and rear wheels.Typical unit code(s): CMT for centimeters, MTR for meters, INH for inches, FOT for foot/feet
        vehicleIdentificationNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles.
        vehicleInteriorType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience.
        vehicleEngine: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Information about the engine or engines of the vehicle.
        numberOfDoors: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number of doors.Typical unit code(s): C62
        vehicleInteriorColor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The color or color combination of the interior of the vehicle.
        driveWheelConfiguration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle's engine via the drivetrain.
        numberOfAxles: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number of axles.Typical unit code(s): C62
        vehicleSeatingCapacity: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.Typical unit code(s): C62 for persons.
        numberOfPreviousOwners: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number of owners of the vehicle, including the current one.Typical unit code(s): C62
        purchaseDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date the item, e.g. vehicle, was purchased by the current owner.
        bodyType: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates the design and body style of the vehicle (e.g. station wagon, hatchback, etc.).
        fuelType: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.
        speed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The speed range of the vehicle. If the vehicle is powered by an engine, the upper limit of the speed range (indicated by [[maxValue]]) should be the maximum speed achievable under regular conditions.Typical unit code(s): KMH for km/h, HM for mile per hour (0.447 04 m/s), KNT for knot*Note 1: Use [[minValue]] and [[maxValue]] to indicate the range. Typically, the minimal value is zero.* Note 2: There are many different ways of measuring the speed range. You can link to information about how the given value has been determined using the [[valueReference]] property.
        mileageFromOdometer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The total distance travelled by the particular vehicle since its initial production, as read from its odometer.Typical unit code(s): KMT for kilometers, SMI for statute miles
        productionDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date of production of the item, e.g. vehicle.
        knownVehicleDamages: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A textual description of known damages, both repaired and unrepaired.
        dateVehicleFirstRegistered: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The date of the first registration of the vehicle with the respective public authorities.
        weightTotal: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The permitted total weight of the loaded vehicle, including passengers and cargo and the weight of the empty vehicle.Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        numberOfAirbags: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number or type of airbags in the vehicle.
        fuelEfficiency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L).* Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter. Use [[unitText]] to indicate the unit of measurement, e.g. mpg or km/L.* Note 2: There are two ways of indicating the fuel consumption, [[fuelConsumption]] (e.g. 8 liters per 100 km) and [[fuelEfficiency]] (e.g. 30 miles per gallon). They are reciprocal.* Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use [[valueReference]] to link the value for the fuel economy to another value.
        vehicleModelDate: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): The release date of a vehicle model (often used to differentiate versions of the same make and model).
        numberOfForwardGears: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The total number of forward gears available for the transmission system of the vehicle.Typical unit code(s): C62
        callSign: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [callsign](https://en.wikipedia.org/wiki/Call_sign), as used in broadcasting and radio communications to identify people, radio and TV stations, or vehicles.
        vehicleConfiguration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'.
        tongueWeight: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The permitted vertical load (TWR) of a trailer attached to the vehicle. Also referred to as Tongue Load Rating (TLR) or Vertical Load Rating (VLR).Typical unit code(s): KGM for kilogram, LBR for pound* Note 1: You can indicate additional information in the [[name]] of the [[QuantitativeValue]] node.* Note 2: You may also link to a [[QualitativeValue]] node that provides additional information using [[valueReference]].* Note 3: Note that you can use [[minValue]] and [[maxValue]] to indicate ranges.
        accelerationTime: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The time needed to accelerate the vehicle from a given start velocity to a given target velocity.Typical unit code(s): SEC for seconds* Note: There are unfortunately no standard unit codes for seconds/0..100 km/h or seconds/0..60 mph. Simply use "SEC" for seconds and indicate the velocities in the [[name]] of the [[QuantitativeValue]], or use [[valueReference]] with a [[QuantitativeValue]] of 0..60 mph or 0..100 km/h to specify the reference speeds.
        seatingCapacity: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The number of persons that can be seated (e.g. in a vehicle), both in terms of the physical space available, and in terms of limitations set by law.Typical unit code(s): C62 for persons
    """

    vehicleSpecialUsage: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    trailerWeight: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cargoVolume: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    steeringPosition: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    fuelConsumption: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    modelDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    vehicleTransmission: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    emissionsCO2: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    meetsEmissionStandard: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    payload: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    fuelCapacity: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    wheelbase: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    vehicleIdentificationNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    vehicleInteriorType: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    vehicleEngine: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfDoors: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    vehicleInteriorColor: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    driveWheelConfiguration: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    numberOfAxles: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    vehicleSeatingCapacity: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    numberOfPreviousOwners: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    purchaseDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    bodyType: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    fuelType: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    speed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    mileageFromOdometer: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    productionDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    knownVehicleDamages: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    dateVehicleFirstRegistered: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    weightTotal: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfAirbags: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    fuelEfficiency: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    vehicleModelDate: NotRequired[
        Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]
    ]
    numberOfForwardGears: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    callSign: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    vehicleConfiguration: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    tongueWeight: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    accelerationTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    seatingCapacity: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class VehicleAllProperties(VehicleInheritedProperties, VehicleProperties, TypedDict):
    pass


class VehicleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Vehicle", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"hasMeasurement": {"exclude": True}}
        fields = {"countryOfAssembly": {"exclude": True}}
        fields = {"width": {"exclude": True}}
        fields = {"isAccessoryOrSparePartFor": {"exclude": True}}
        fields = {"isConsumableFor": {"exclude": True}}
        fields = {"depth": {"exclude": True}}
        fields = {"additionalProperty": {"exclude": True}}
        fields = {"isVariantOf": {"exclude": True}}
        fields = {"slogan": {"exclude": True}}
        fields = {"manufacturer": {"exclude": True}}
        fields = {"gtin14": {"exclude": True}}
        fields = {"keywords": {"exclude": True}}
        fields = {"positiveNotes": {"exclude": True}}
        fields = {"reviews": {"exclude": True}}
        fields = {"height": {"exclude": True}}
        fields = {"model": {"exclude": True}}
        fields = {"itemCondition": {"exclude": True}}
        fields = {"award": {"exclude": True}}
        fields = {"nsn": {"exclude": True}}
        fields = {"awards": {"exclude": True}}
        fields = {"review": {"exclude": True}}
        fields = {"gtin": {"exclude": True}}
        fields = {"isRelatedTo": {"exclude": True}}
        fields = {"negativeNotes": {"exclude": True}}
        fields = {"funding": {"exclude": True}}
        fields = {"mobileUrl": {"exclude": True}}
        fields = {"hasEnergyConsumptionDetails": {"exclude": True}}
        fields = {"weight": {"exclude": True}}
        fields = {"hasMerchantReturnPolicy": {"exclude": True}}
        fields = {"pattern": {"exclude": True}}
        fields = {"isFamilyFriendly": {"exclude": True}}
        fields = {"gtin12": {"exclude": True}}
        fields = {"isSimilarTo": {"exclude": True}}
        fields = {"productID": {"exclude": True}}
        fields = {"countryOfOrigin": {"exclude": True}}
        fields = {"hasAdultConsideration": {"exclude": True}}
        fields = {"purchaseDate": {"exclude": True}}
        fields = {"audience": {"exclude": True}}
        fields = {"logo": {"exclude": True}}
        fields = {"countryOfLastProcessing": {"exclude": True}}
        fields = {"asin": {"exclude": True}}
        fields = {"gtin8": {"exclude": True}}
        fields = {"releaseDate": {"exclude": True}}
        fields = {"brand": {"exclude": True}}
        fields = {"productionDate": {"exclude": True}}
        fields = {"inProductGroupWithID": {"exclude": True}}
        fields = {"size": {"exclude": True}}
        fields = {"mpn": {"exclude": True}}
        fields = {"category": {"exclude": True}}
        fields = {"aggregateRating": {"exclude": True}}
        fields = {"color": {"exclude": True}}
        fields = {"material": {"exclude": True}}
        fields = {"offers": {"exclude": True}}
        fields = {"gtin13": {"exclude": True}}
        fields = {"sku": {"exclude": True}}
        fields = {"vehicleSpecialUsage": {"exclude": True}}
        fields = {"trailerWeight": {"exclude": True}}
        fields = {"cargoVolume": {"exclude": True}}
        fields = {"steeringPosition": {"exclude": True}}
        fields = {"fuelConsumption": {"exclude": True}}
        fields = {"modelDate": {"exclude": True}}
        fields = {"vehicleTransmission": {"exclude": True}}
        fields = {"emissionsCO2": {"exclude": True}}
        fields = {"meetsEmissionStandard": {"exclude": True}}
        fields = {"payload": {"exclude": True}}
        fields = {"fuelCapacity": {"exclude": True}}
        fields = {"wheelbase": {"exclude": True}}
        fields = {"vehicleIdentificationNumber": {"exclude": True}}
        fields = {"vehicleInteriorType": {"exclude": True}}
        fields = {"vehicleEngine": {"exclude": True}}
        fields = {"numberOfDoors": {"exclude": True}}
        fields = {"vehicleInteriorColor": {"exclude": True}}
        fields = {"driveWheelConfiguration": {"exclude": True}}
        fields = {"numberOfAxles": {"exclude": True}}
        fields = {"vehicleSeatingCapacity": {"exclude": True}}
        fields = {"numberOfPreviousOwners": {"exclude": True}}
        fields = {"purchaseDate": {"exclude": True}}
        fields = {"bodyType": {"exclude": True}}
        fields = {"fuelType": {"exclude": True}}
        fields = {"speed": {"exclude": True}}
        fields = {"mileageFromOdometer": {"exclude": True}}
        fields = {"productionDate": {"exclude": True}}
        fields = {"knownVehicleDamages": {"exclude": True}}
        fields = {"dateVehicleFirstRegistered": {"exclude": True}}
        fields = {"weightTotal": {"exclude": True}}
        fields = {"numberOfAirbags": {"exclude": True}}
        fields = {"fuelEfficiency": {"exclude": True}}
        fields = {"vehicleModelDate": {"exclude": True}}
        fields = {"numberOfForwardGears": {"exclude": True}}
        fields = {"callSign": {"exclude": True}}
        fields = {"vehicleConfiguration": {"exclude": True}}
        fields = {"tongueWeight": {"exclude": True}}
        fields = {"accelerationTime": {"exclude": True}}
        fields = {"seatingCapacity": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        VehicleProperties, VehicleInheritedProperties, VehicleAllProperties
    ] = VehicleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Vehicle"
    return model


Vehicle = create_schema_org_model()


def create_vehicle_model(
    model: Union[VehicleProperties, VehicleInheritedProperties, VehicleAllProperties]
):
    _type = deepcopy(VehicleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Vehicle. Please see: https://schema.org/Vehicle"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: VehicleAllProperties):
    pydantic_type = create_vehicle_model(model=model)
    return pydantic_type(model).schema_json()
