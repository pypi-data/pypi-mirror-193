"""
A ProductGroup represents a group of [[Product]]s that vary only in certain well-described ways, such as by [[size]], [[color]], [[material]] etc.While a ProductGroup itself is not directly offered for sale, the various varying products that it represents can be. The ProductGroup serves as a prototype or template, standing in for all of the products who have an [[isVariantOf]] relationship to it. As such, properties (including additional types) can be applied to the ProductGroup to represent characteristics shared by each of the (possibly very many) variants. Properties that reference a ProductGroup are not included in this mechanism; neither are the following specific properties [[variesBy]], [[hasVariant]], [[url]]. 

https://schema.org/ProductGroup
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ProductGroupInheritedProperties(TypedDict):
    """A ProductGroup represents a group of [[Product]]s that vary only in certain well-described ways, such as by [[size]], [[color]], [[material]] etc.While a ProductGroup itself is not directly offered for sale, the various varying products that it represents can be. The ProductGroup serves as a prototype or template, standing in for all of the products who have an [[isVariantOf]] relationship to it. As such, properties (including additional types) can be applied to the ProductGroup to represent characteristics shared by each of the (possibly very many) variants. Properties that reference a ProductGroup are not included in this mechanism; neither are the following specific properties [[variesBy]], [[hasVariant]], [[url]].

    References:
        https://schema.org/ProductGroup
    Note:
        Model Depth 3
    Attributes:
        hasMeasurement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A product measurement, for example the inseam of pants, the wheel size of a bicycle, or the gauge of a screw. Usually an exact measurement, but can also be a range of measurements for adjustable products, for example belts and ski bindings.
        countryOfAssembly: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The place where the product was assembled.
        width: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The width of the item.
        isAccessoryOrSparePartFor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A pointer to another product (or multiple products) for which this product is an accessory or spare part.
        isConsumableFor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A pointer to another product (or multiple products) for which this product is a consumable.
        depth: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The depth of the item.
        additionalProperty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
        isVariantOf: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the kind of product that this is a variant of. In the case of [[ProductModel]], this is a pointer (from a ProductModel) to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive. In the case of a [[ProductGroup]], the group description also serves as a template, representing a set of Products that vary on explicitly defined, specific dimensions only (so it defines both a set of variants, as well as which values distinguish amongst those variants). When used with [[ProductGroup]], this property can apply to any [[Product]] included in the group.
        slogan: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A slogan or motto associated with the item.
        manufacturer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The manufacturer of the product.
        gtin14: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The GTIN-14 code of the product, or the product to which the offer refers. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        keywords: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        positiveNotes: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Provides positive considerations regarding something, for example product highlights or (alongside [[negativeNotes]]) pro/con lists for reviews.In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).
        reviews: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Review of the item.
        height: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The height of the item.
        model: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.
        itemCondition: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A predefined value from OfferItemCondition specifying the condition of the product or service, or the products or services included in the offer. Also used for product return policies to specify the condition of products accepted for returns.
        award: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An award won by or for this item.
        nsn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the [NATO stock number](https://en.wikipedia.org/wiki/NATO_Stock_Number) (nsn) of a [[Product]].
        awards: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Awards won by or for this item.
        review: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A review of the item.
        gtin: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A Global Trade Item Number ([GTIN](https://www.gs1.org/standards/id-keys/gtin)). GTINs identify trade items, including products and services, using numeric identification codes.The GS1 [digital link specifications](https://www.gs1.org/standards/Digital-Link/) express GTINs as URLs (URIs, IRIs, etc.). Details including regular expression examples can be found in, Section 6 of the GS1 URI Syntax specification; see also [schema.org tracking issue](https://github.com/schemaorg/schemaorg/issues/3156#issuecomment-1209522809) for schema.org-specific discussion. A correct [[gtin]] value should be a valid GTIN, which means that it should be an all-numeric string of either 8, 12, 13 or 14 digits, or a "GS1 Digital Link" URL based on such a string. The numeric component should also have a [valid GS1 check digit](https://www.gs1.org/services/check-digit-calculator) and meet the other rules for valid GTINs. See also [GS1's GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) and [Wikipedia](https://en.wikipedia.org/wiki/Global_Trade_Item_Number) for more details. Left-padding of the gtin values is not required or encouraged. The [[gtin]] property generalizes the earlier [[gtin8]], [[gtin12]], [[gtin13]], and [[gtin14]] properties.Note also that this is a definition for how to include GTINs in Schema.org data, and not a definition of GTINs in general - see the GS1 documentation for authoritative details.
        isRelatedTo: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A pointer to another, somehow related product (or multiple products).
        negativeNotes: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Provides negative considerations regarding something, most typically in pro/con lists for reviews (alongside [[positiveNotes]]). For symmetry In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]] used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used on [[Product]].The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).
        funding: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        mobileUrl: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The [[mobileUrl]] property is provided for specific situations in which data consumers need to determine whether one of several provided URLs is a dedicated 'mobile site'.To discourage over-use, and reflecting intial usecases, the property is expected only on [[Product]] and [[Offer]], rather than [[Thing]]. The general trend in web technology is towards [responsive design](https://en.wikipedia.org/wiki/Responsive_web_design) in which content can be flexibly adapted to a wide range of browsing environments. Pages and sites referenced with the long-established [[url]] property should ideally also be usable on a wide variety of devices, including mobile phones. In most cases, it would be pointless and counter productive to attempt to update all [[url]] markup to use [[mobileUrl]] for more mobile-oriented pages. The property is intended for the case when items (primarily [[Product]] and [[Offer]]) have extra URLs hosted on an additional "mobile site" alongside the main one. It should not be taken as an endorsement of this publication style.
        hasEnergyConsumptionDetails: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Defines the energy efficiency Category (also known as "class" or "rating") for a product according to an international energy efficiency standard.
        weight: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The weight of the product or person.
        hasMerchantReturnPolicy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifies a MerchantReturnPolicy that may be applicable.
        pattern: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A pattern that something has, for example 'polka dot', 'striped', 'Canadian flag'. Values are typically expressed as text, although links to controlled value schemes are also supported.
        isFamilyFriendly: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether this content is family friendly.
        gtin12: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        isSimilarTo: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A pointer to another, functionally similar product (or multiple products).
        productID: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The product identifier, such as ISBN. For example: ``` meta itemprop="productID" content="isbn:123-456-789" ```.
        countryOfOrigin: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The country of origin of something, including products as well as creative  works such as movie and TV content.In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.
        hasAdultConsideration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Used to tag an item to be intended or suitable for consumption or use by adults only.
        purchaseDate: (Optional[Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]]): The date the item, e.g. vehicle, was purchased by the current owner.
        audience: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An intended audience, i.e. a group for whom something was created.
        logo: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): An associated logo.
        countryOfLastProcessing: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The place where the item (typically [[Product]]) was last processed and tested before importation.
        asin: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): An Amazon Standard Identification Number (ASIN) is a 10-character alphanumeric unique identifier assigned by Amazon.com and its partners for product identification within the Amazon organization (summary from [Wikipedia](https://en.wikipedia.org/wiki/Amazon_Standard_Identification_Number)'s article).Note also that this is a definition for how to include ASINs in Schema.org data, and not a definition of ASINs in general - see documentation from Amazon for authoritative details.ASINs are most commonly encoded as text strings, but the [asin] property supports URL/URI as potential values too.
        gtin8: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        releaseDate: (Optional[Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]]): The release date of a product or product model. This can be used to distinguish the exact variant of a product.
        brand: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
        productionDate: (Optional[Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]]): The date of production of the item, e.g. vehicle.
        inProductGroupWithID: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the [[productGroupID]] for a [[ProductGroup]] that this product [[isVariantOf]].
        size: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A standardized size of a product or creative work, specified either through a simple textual string (for example 'XL', '32Wx34L'), a  QuantitativeValue with a unitCode, or a comprehensive and structured [[SizeSpecification]]; in other cases, the [[width]], [[height]], [[depth]] and [[weight]] properties may be more applicable.
        mpn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.
        category: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
        aggregateRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The overall rating, based on a collection of reviews or ratings, of the item.
        color: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The color of the product.
        material: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A material that something is made from, e.g. leather, wool, cotton, paper.
        offers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        gtin13: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceding zero. See [GS1 GTIN Summary](http://www.gs1.org/barcodes/technical/idkeys/gtin) for more details.
        sku: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.
    """

    hasMeasurement: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    countryOfAssembly: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    width: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isAccessoryOrSparePartFor: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    isConsumableFor: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    depth: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    additionalProperty: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    isVariantOf: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    slogan: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    manufacturer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gtin14: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    keywords: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    positiveNotes: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    reviews: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    height: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    model: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    itemCondition: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    award: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    nsn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    awards: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    review: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gtin: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    isRelatedTo: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    negativeNotes: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    funding: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    mobileUrl: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hasEnergyConsumptionDetails: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    weight: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hasMerchantReturnPolicy: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    pattern: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isFamilyFriendly: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    gtin12: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isSimilarTo: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    productID: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    countryOfOrigin: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    hasAdultConsideration: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    purchaseDate: NotRequired[
        Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]
    ]
    audience: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    logo: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    countryOfLastProcessing: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    asin: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    gtin8: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    releaseDate: NotRequired[
        Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]
    ]
    brand: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    productionDate: NotRequired[
        Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]
    ]
    inProductGroupWithID: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    size: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    mpn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    category: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    aggregateRating: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    color: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    material: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    offers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gtin13: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sku: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class ProductGroupProperties(TypedDict):
    """A ProductGroup represents a group of [[Product]]s that vary only in certain well-described ways, such as by [[size]], [[color]], [[material]] etc.While a ProductGroup itself is not directly offered for sale, the various varying products that it represents can be. The ProductGroup serves as a prototype or template, standing in for all of the products who have an [[isVariantOf]] relationship to it. As such, properties (including additional types) can be applied to the ProductGroup to represent characteristics shared by each of the (possibly very many) variants. Properties that reference a ProductGroup are not included in this mechanism; neither are the following specific properties [[variesBy]], [[hasVariant]], [[url]].

    References:
        https://schema.org/ProductGroup
    Note:
        Model Depth 3
    Attributes:
        variesBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the property or properties by which the variants in a [[ProductGroup]] vary, e.g. their size, color etc. Schema.org properties can be referenced by their short name e.g. "color"; terms defined elsewhere can be referenced with their URIs.
        hasVariant: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a [[Product]] that is a member of this [[ProductGroup]] (or [[ProductModel]]).
        productGroupID: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates a textual identifier for a ProductGroup.
    """

    variesBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    hasVariant: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    productGroupID: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class ProductGroupAllProperties(
    ProductGroupInheritedProperties, ProductGroupProperties, TypedDict
):
    pass


class ProductGroupBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ProductGroup", alias="@id")
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
        fields = {"variesBy": {"exclude": True}}
        fields = {"hasVariant": {"exclude": True}}
        fields = {"productGroupID": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ProductGroupProperties,
        ProductGroupInheritedProperties,
        ProductGroupAllProperties,
    ] = ProductGroupAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ProductGroup"
    return model


ProductGroup = create_schema_org_model()


def create_productgroup_model(
    model: Union[
        ProductGroupProperties,
        ProductGroupInheritedProperties,
        ProductGroupAllProperties,
    ]
):
    _type = deepcopy(ProductGroupAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ProductGroupAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ProductGroupAllProperties):
    pydantic_type = create_productgroup_model(model=model)
    return pydantic_type(model).schema_json()
