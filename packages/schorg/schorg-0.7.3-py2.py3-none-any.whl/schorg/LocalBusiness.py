"""
A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.

https://schema.org/LocalBusiness
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LocalBusinessInheritedProperties(TypedDict):
    """A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.

    References:
        https://schema.org/LocalBusiness
    Note:
        Model Depth 3
    Attributes:
        serviceArea: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where the service is provided.
        founder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person who founded this organization.
        isicV4: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
        hasPOS: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Points-of-Sales operated by the organization or person.
        globalLocationNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.
        member: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.
        knowsAbout: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Of a [[Person]], and less typically of an [[Organization]], to indicate a topic that is known about - suggesting possible expertise but not implying it. We do not distinguish skill levels here, or relate this to educational content, events, objectives or [[JobPosting]] descriptions.
        makesOffer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to products or services offered by the organization or person.
        ownershipFundingInfo: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a description of organizational ownership structure; funding and grants. In a news/media setting, this is with particular reference to editorial independence.   Note that the [[funder]] is also available and can be used to make basic funder information machine-readable.
        founders: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person who founded this organization.
        legalName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The official name of the organization, e.g. the registered company name.
        actionableFeedbackPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For a [[NewsMediaOrganization]] or other news-related [[Organization]], a statement about public engagement activities (for news media, the newsroom’s), including involving the public - digitally or otherwise -- in coverage decisions, reporting and activities after publication.
        areaServed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geographic area where a service or offered item is provided.
        parentOrganization: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The larger organization that this organization is a [[subOrganization]] of, if any.
        slogan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A slogan or motto associated with the item.
        department: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A relationship between an organization and a department of that organization, also described as an organization (allowing different urls, logos, opening hours). For example: a store with a pharmacy, or a bakery with a cafe.
        keywords: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        reviews: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Review of the item.
        memberOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An Organization (or ProgramMembership) to which this Person or Organization belongs.
        publishingPrinciples: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The publishingPrinciples property indicates (typically via [[URL]]) a document describing the editorial principles of an [[Organization]] (or individual, e.g. a [[Person]] writing a blog) that relate to their activities as a publisher, e.g. ethics or diversity policies. When applied to a [[CreativeWork]] (e.g. [[NewsArticle]]) the principles are those of the party primarily responsible for the creation of the [[CreativeWork]].While such policies are most typically expressed in natural language, sometimes related information (e.g. indicating a [[funder]]) can be expressed using schema.org terminology.
        employee: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Someone working for this organization.
        award: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An award won by or for this item.
        email: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Email address.
        contactPoints: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact point for a person or organization.
        diversityStaffingReport: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For an [[Organization]] (often but not necessarily a [[NewsMediaOrganization]]), a report on staffing diversity issues. In a news context this might be for example ASNE or RTDNA (US) reports, or self-reported.
        foundingDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date that this organization was founded.
        owns: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Products owned by the organization or person.
        awards: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Awards won by or for this item.
        review: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A review of the item.
        dissolutionDate: (Optional[Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]]): The date that this organization was dissolved.
        funding: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        interactionStatistic: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.
        events: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past events associated with this place or organization.
        seeks: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A pointer to products or services sought by the organization or person (demand).
        employees: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): People working for this organization.
        unnamedSourcesPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For an [[Organization]] (typically a [[NewsMediaOrganization]]), a statement about policy on use of unnamed sources and the decision process required.
        subOrganization: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A relationship between two organizations where the first includes the second, e.g., as a subsidiary. See also: the more specific 'department' property.
        foundingLocation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The place where the Organization was founded.
        funder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports (sponsors) something through some kind of financial contribution.
        iso6523Code: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An organization identifier as defined in ISO 6523(-1). Note that many existing organization identifiers such as [leiCode](https://schema.org/leiCode), [duns](https://schema.org/duns) and [vatID](https://schema.org/vatID) can be expressed as an ISO 6523 identifier by setting the ICD part of the ISO 6523 identifier accordingly.
        diversityPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Statement on diversity policy by an [[Organization]] e.g. a [[NewsMediaOrganization]]. For a [[NewsMediaOrganization]], a statement describing the newsroom’s diversity policy on both staffing and sources, typically providing staffing data.
        hasMerchantReturnPolicy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Specifies a MerchantReturnPolicy that may be applicable.
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
        duns: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Dun & Bradstreet DUNS number for identifying an organization or business person.
        alumni: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Alumni of an organization.
        ethicsPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Statement about ethics policy, e.g. of a [[NewsMediaOrganization]] regarding journalistic and publishing practices, or of a [[Restaurant]], a page describing food source policies. In the case of a [[NewsMediaOrganization]], an ethicsPolicy is typically a statement describing the personal, organizational, and corporate standards of behavior expected by the organization.
        leiCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An organization identifier that uniquely identifies a legal entity as defined in ISO 17442.
        vatID: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Value-added Tax ID of the organization or person.
        knowsLanguage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Of a [[Person]], and less typically of an [[Organization]], to indicate a known language. We do not distinguish skill levels or reading/writing/speaking/signing here. Use language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47).
        correctionsPolicy: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): For an [[Organization]] (e.g. [[NewsMediaOrganization]]), a statement describing (in news media, the newsroom’s) disclosure and correction policy for errors.
        logo: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An associated logo.
        hasCredential: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A credential awarded to the Person or Organization.
        address: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Physical address of the item.
        brand: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.
        nonprofitStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): nonprofitStatus indicates the legal status of a non-profit organization in its primary place of business.
        contactPoint: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A contact point for a person or organization.
        hasOfferCatalog: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates an OfferCatalog listing for this Organization, Person, or Service.
        members: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A member of this organization.
        aggregateRating: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The overall rating, based on a collection of reviews or ratings, of the item.
        faxNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The fax number.
        telephone: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The telephone number.
        taxID: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.
        naics: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The North American Industry Classification System (NAICS) code for a particular organization or business person.
        location: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        numberOfEmployees: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of employees in an organization, e.g. business.
        sponsor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
        geoCovers: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a covering geometry to a covered geometry. "Every point of b is a point of (the interior or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        longitude: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).
        smokingAllowed: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel room.
        isicV4: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.
        globalLocationNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The [Global Location Number](http://www.gs1.org/gln) (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.
        amenityFeature: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
        additionalProperty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A property-value pair representing an additional characteristic of the entity, e.g. a product feature or another characteristic for which there is no matching property in schema.org.Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. https://schema.org/width, https://schema.org/color, https://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
        slogan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A slogan or motto associated with the item.
        photos: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Photographs of this place.
        keywords: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        reviews: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Review of the item.
        tourBookingPage: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.
        geoWithin: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to one that contains it, i.e. it is inside (i.e. within) its interior. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        containsPlace: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The basic containment relation between a place and another that it contains.
        review: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A review of the item.
        hasMap: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A URL to a map of the place.
        containedIn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The basic containment relation between a place and one that contains it.
        events: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past events associated with this place or organization.
        geoOverlaps: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to another that geospatially overlaps it, i.e. they have some but not all points in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        geoEquals: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) are topologically equal, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM). "Two geometries are topologically equal if their interiors intersect and no part of the interior or boundary of one geometry intersects the exterior of the other" (a symmetric relationship).
        maps: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A URL to a map of the place.
        isAccessibleForFree: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): A flag to signal that the item, event, or place is accessible for free.
        event: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Upcoming or past event associated with this place, organization, or action.
        photo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A photograph of this place.
        containedInPlace: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The basic containment relation between a place and one that contains it.
        logo: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An associated logo.
        geoCrosses: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to another that crosses it: "a crosses b: they have some but not all interior points in common, and the dimension of the intersection is less than that of at least one of them". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        address: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Physical address of the item.
        geo: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The geo coordinates of the place.
        openingHoursSpecification: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The opening hours of a certain place.
        geoDisjoint: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) are topologically disjoint: "they have no point in common. They form a set of disconnected geometries." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        geoIntersects: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) have at least one point in common. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        latitude: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The latitude of a location. For example ```37.42242``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).
        maximumAttendeeCapacity: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The total number of individuals that may attend an event or venue.
        aggregateRating: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The overall rating, based on a collection of reviews or ratings, of the item.
        map: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A URL to a map of the place.
        branchCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A short textual code (also called "store code") that uniquely identifies a place of business. The code is typically assigned by the parentOrganization and used in structured URLs.For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.
        faxNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The fax number.
        publicAccess: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): A flag to signal that the [[Place]] is open to public visitors.  If this property is omitted there is no assumed default boolean value
        geoTouches: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) touch: "they have at least one boundary point in common, but no interior points." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        geoCoveredBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        telephone: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The telephone number.
        hasDriveThroughService: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): Indicates whether some facility (e.g. [[FoodEstablishment]], [[CovidTestingFacility]]) offers a service that can be used by driving through in a car. In the case of [[CovidTestingFacility]] such facilities could potentially help with social distancing from other potentially-infected users.
        specialOpeningHoursSpecification: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The special opening hours of a certain place.Use this to explicitly override general opening hours brought in scope by [[openingHoursSpecification]] or [[openingHours]].
        geoContains: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry. "a contains b iff no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
    """

    serviceArea: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    founder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    isicV4: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasPOS: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    globalLocationNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    member: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    knowsAbout: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    makesOffer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ownershipFundingInfo: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    founders: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    legalName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actionableFeedbackPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    areaServed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    parentOrganization: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    slogan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    department: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    keywords: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    reviews: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    memberOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    publishingPrinciples: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    employee: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    award: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    email: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    contactPoints: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    diversityStaffingReport: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    foundingDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    owns: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    awards: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    review: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    dissolutionDate: NotRequired[
        Union[List[Union[str, date, SchemaOrgObj]], str, date, SchemaOrgObj]
    ]
    funding: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    interactionStatistic: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    events: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    seeks: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    employees: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    unnamedSourcesPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    subOrganization: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    foundingLocation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    funder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    iso6523Code: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    diversityPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    hasMerchantReturnPolicy: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    duns: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    alumni: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ethicsPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    leiCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    vatID: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    knowsLanguage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    correctionsPolicy: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    logo: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    hasCredential: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    address: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    brand: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    nonprofitStatus: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    contactPoint: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasOfferCatalog: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    members: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    aggregateRating: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    faxNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    telephone: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    taxID: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    naics: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    location: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfEmployees: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    sponsor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoCovers: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    longitude: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    smokingAllowed: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]
    isicV4: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    globalLocationNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    amenityFeature: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    additionalProperty: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    slogan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    photos: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    keywords: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    reviews: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    tourBookingPage: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    geoWithin: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    containsPlace: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    review: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasMap: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    containedIn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    events: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoOverlaps: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoEquals: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    maps: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    isAccessibleForFree: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]
    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    photo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    containedInPlace: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    logo: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    geoCrosses: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    address: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    openingHoursSpecification: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    geoDisjoint: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoIntersects: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    latitude: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    maximumAttendeeCapacity: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    aggregateRating: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    map: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    branchCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    faxNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    publicAccess: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]
    geoTouches: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoCoveredBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    telephone: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasDriveThroughService: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]
    specialOpeningHoursSpecification: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    geoContains: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class LocalBusinessProperties(TypedDict):
    """A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.

    References:
        https://schema.org/LocalBusiness
    Note:
        Model Depth 3
    Attributes:
        priceRange: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The price range of the business, for example ```$$$```.
        currenciesAccepted: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency accepted.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        branchOf: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The larger organization that this local business is a branch of, if any. Not to be confused with (anatomical) [[branch]].
        paymentAccepted: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Cash, Credit Card, Cryptocurrency, Local Exchange Tradings System, etc.
        openingHours: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.* Days are specified using the following two-letter combinations: ```Mo```, ```Tu```, ```We```, ```Th```, ```Fr```, ```Sa```, ```Su```.* Times are specified using 24:00 format. For example, 3pm is specified as ```15:00```, 10am as ```10:00```. * Here is an example: <code>&lt;time itemprop="openingHours" datetime=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/time&gt;</code>.* If a business is open 7 days a week, then it can be specified as <code>&lt;time itemprop=&quot;openingHours&quot; datetime=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/time&gt;</code>.
    """

    priceRange: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    currenciesAccepted: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    branchOf: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    paymentAccepted: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    openingHours: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class LocalBusinessAllProperties(
    LocalBusinessInheritedProperties, LocalBusinessProperties, TypedDict
):
    pass


class LocalBusinessBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LocalBusiness", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"serviceArea": {"exclude": True}}
        fields = {"founder": {"exclude": True}}
        fields = {"isicV4": {"exclude": True}}
        fields = {"hasPOS": {"exclude": True}}
        fields = {"globalLocationNumber": {"exclude": True}}
        fields = {"member": {"exclude": True}}
        fields = {"knowsAbout": {"exclude": True}}
        fields = {"makesOffer": {"exclude": True}}
        fields = {"ownershipFundingInfo": {"exclude": True}}
        fields = {"founders": {"exclude": True}}
        fields = {"legalName": {"exclude": True}}
        fields = {"actionableFeedbackPolicy": {"exclude": True}}
        fields = {"areaServed": {"exclude": True}}
        fields = {"parentOrganization": {"exclude": True}}
        fields = {"slogan": {"exclude": True}}
        fields = {"department": {"exclude": True}}
        fields = {"keywords": {"exclude": True}}
        fields = {"reviews": {"exclude": True}}
        fields = {"memberOf": {"exclude": True}}
        fields = {"publishingPrinciples": {"exclude": True}}
        fields = {"employee": {"exclude": True}}
        fields = {"award": {"exclude": True}}
        fields = {"email": {"exclude": True}}
        fields = {"contactPoints": {"exclude": True}}
        fields = {"diversityStaffingReport": {"exclude": True}}
        fields = {"foundingDate": {"exclude": True}}
        fields = {"owns": {"exclude": True}}
        fields = {"awards": {"exclude": True}}
        fields = {"review": {"exclude": True}}
        fields = {"dissolutionDate": {"exclude": True}}
        fields = {"funding": {"exclude": True}}
        fields = {"interactionStatistic": {"exclude": True}}
        fields = {"events": {"exclude": True}}
        fields = {"seeks": {"exclude": True}}
        fields = {"employees": {"exclude": True}}
        fields = {"unnamedSourcesPolicy": {"exclude": True}}
        fields = {"subOrganization": {"exclude": True}}
        fields = {"foundingLocation": {"exclude": True}}
        fields = {"funder": {"exclude": True}}
        fields = {"iso6523Code": {"exclude": True}}
        fields = {"diversityPolicy": {"exclude": True}}
        fields = {"hasMerchantReturnPolicy": {"exclude": True}}
        fields = {"event": {"exclude": True}}
        fields = {"duns": {"exclude": True}}
        fields = {"alumni": {"exclude": True}}
        fields = {"ethicsPolicy": {"exclude": True}}
        fields = {"leiCode": {"exclude": True}}
        fields = {"vatID": {"exclude": True}}
        fields = {"knowsLanguage": {"exclude": True}}
        fields = {"correctionsPolicy": {"exclude": True}}
        fields = {"logo": {"exclude": True}}
        fields = {"hasCredential": {"exclude": True}}
        fields = {"address": {"exclude": True}}
        fields = {"brand": {"exclude": True}}
        fields = {"nonprofitStatus": {"exclude": True}}
        fields = {"contactPoint": {"exclude": True}}
        fields = {"hasOfferCatalog": {"exclude": True}}
        fields = {"members": {"exclude": True}}
        fields = {"aggregateRating": {"exclude": True}}
        fields = {"faxNumber": {"exclude": True}}
        fields = {"telephone": {"exclude": True}}
        fields = {"taxID": {"exclude": True}}
        fields = {"naics": {"exclude": True}}
        fields = {"location": {"exclude": True}}
        fields = {"numberOfEmployees": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}
        fields = {"geoCovers": {"exclude": True}}
        fields = {"longitude": {"exclude": True}}
        fields = {"smokingAllowed": {"exclude": True}}
        fields = {"isicV4": {"exclude": True}}
        fields = {"globalLocationNumber": {"exclude": True}}
        fields = {"amenityFeature": {"exclude": True}}
        fields = {"additionalProperty": {"exclude": True}}
        fields = {"slogan": {"exclude": True}}
        fields = {"photos": {"exclude": True}}
        fields = {"keywords": {"exclude": True}}
        fields = {"reviews": {"exclude": True}}
        fields = {"tourBookingPage": {"exclude": True}}
        fields = {"geoWithin": {"exclude": True}}
        fields = {"containsPlace": {"exclude": True}}
        fields = {"review": {"exclude": True}}
        fields = {"hasMap": {"exclude": True}}
        fields = {"containedIn": {"exclude": True}}
        fields = {"events": {"exclude": True}}
        fields = {"geoOverlaps": {"exclude": True}}
        fields = {"geoEquals": {"exclude": True}}
        fields = {"maps": {"exclude": True}}
        fields = {"isAccessibleForFree": {"exclude": True}}
        fields = {"event": {"exclude": True}}
        fields = {"photo": {"exclude": True}}
        fields = {"containedInPlace": {"exclude": True}}
        fields = {"logo": {"exclude": True}}
        fields = {"geoCrosses": {"exclude": True}}
        fields = {"address": {"exclude": True}}
        fields = {"geo": {"exclude": True}}
        fields = {"openingHoursSpecification": {"exclude": True}}
        fields = {"geoDisjoint": {"exclude": True}}
        fields = {"geoIntersects": {"exclude": True}}
        fields = {"latitude": {"exclude": True}}
        fields = {"maximumAttendeeCapacity": {"exclude": True}}
        fields = {"aggregateRating": {"exclude": True}}
        fields = {"map": {"exclude": True}}
        fields = {"branchCode": {"exclude": True}}
        fields = {"faxNumber": {"exclude": True}}
        fields = {"publicAccess": {"exclude": True}}
        fields = {"geoTouches": {"exclude": True}}
        fields = {"geoCoveredBy": {"exclude": True}}
        fields = {"telephone": {"exclude": True}}
        fields = {"hasDriveThroughService": {"exclude": True}}
        fields = {"specialOpeningHoursSpecification": {"exclude": True}}
        fields = {"geoContains": {"exclude": True}}
        fields = {"priceRange": {"exclude": True}}
        fields = {"currenciesAccepted": {"exclude": True}}
        fields = {"branchOf": {"exclude": True}}
        fields = {"paymentAccepted": {"exclude": True}}
        fields = {"openingHours": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        LocalBusinessProperties,
        LocalBusinessInheritedProperties,
        LocalBusinessAllProperties,
    ] = LocalBusinessAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LocalBusiness"
    return model


LocalBusiness = create_schema_org_model()


def create_localbusiness_model(
    model: Union[
        LocalBusinessProperties,
        LocalBusinessInheritedProperties,
        LocalBusinessAllProperties,
    ]
):
    _type = deepcopy(LocalBusinessAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LocalBusinessAllProperties):
    pydantic_type = create_localbusiness_model(model=model)
    return pydantic_type(model).schema_json()
