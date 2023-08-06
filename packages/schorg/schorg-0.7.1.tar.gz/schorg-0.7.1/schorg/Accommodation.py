"""
An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.For more specific types of accommodations not defined in schema.org, one can use additionalType with external vocabularies.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

https://schema.org/Accommodation
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AccommodationInheritedProperties(TypedDict):
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.For more specific types of accommodations not defined in schema.org, one can use additionalType with external vocabularies.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/Accommodation
    Note:
        Model Depth 3
    Attributes:
        geoCovers: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a covering geometry to a covered geometry. "Every point of b is a point of (the interior or boundary of) a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        longitude: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The longitude of a location. For example ```-122.08585``` ([WGS 84](https://en.wikipedia.org/wiki/World_Geodetic_System)).
        smokingAllowed: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Indicates whether it is allowed to smoke in the place, e.g. in the restaurant, hotel or hotel room.
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
        isAccessibleForFree: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): A flag to signal that the item, event, or place is accessible for free.
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
        publicAccess: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): A flag to signal that the [[Place]] is open to public visitors.  If this property is omitted there is no assumed default boolean value
        geoTouches: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents spatial relations in which two geometries (or the places they represent) touch: "they have at least one boundary point in common, but no interior points." (A symmetric relationship, as defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).)
        geoCoveredBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a geometry to another that covers it. As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
        telephone: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The telephone number.
        hasDriveThroughService: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Indicates whether some facility (e.g. [[FoodEstablishment]], [[CovidTestingFacility]]) offers a service that can be used by driving through in a car. In the case of [[CovidTestingFacility]] such facilities could potentially help with social distancing from other potentially-infected users.
        specialOpeningHoursSpecification: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The special opening hours of a certain place.Use this to explicitly override general opening hours brought in scope by [[openingHoursSpecification]] or [[openingHours]].      
        geoContains: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents a relationship between two geometries (or the places they represent), relating a containing geometry to a contained geometry. "a contains b iff no points of b lie in the exterior of a, and at least one point of the interior of b lies in the interior of a". As defined in [DE-9IM](https://en.wikipedia.org/wiki/DE-9IM).
    """

    geoCovers: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    longitude: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    smokingAllowed: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    isicV4: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    globalLocationNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    amenityFeature: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    additionalProperty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    slogan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    photos: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    keywords: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    reviews: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    tourBookingPage: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    geoWithin: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    containsPlace: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    review: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasMap: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    containedIn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    events: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoOverlaps: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoEquals: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    maps: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    isAccessibleForFree: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    event: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    photo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    containedInPlace: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    logo: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    geoCrosses: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    address: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geo: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    openingHoursSpecification: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoDisjoint: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoIntersects: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    latitude: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    maximumAttendeeCapacity: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    aggregateRating: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    map: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    branchCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    faxNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    publicAccess: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    geoTouches: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoCoveredBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    telephone: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    hasDriveThroughService: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    specialOpeningHoursSpecification: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    geoContains: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AccommodationProperties(TypedDict):
    """An accommodation is a place that can accommodate human beings, e.g. a hotel room, a camping pitch, or a meeting room. Many accommodations are for overnight stays, but this is not a mandatory requirement.For more specific types of accommodations not defined in schema.org, one can use additionalType with external vocabularies.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/Accommodation
    Note:
        Model Depth 3
    Attributes:
        floorSize: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The size of the accommodation, e.g. in square meter or squarefoot.Typical unit code(s): MTK for square meter, FTK for square foot, or YDK for square yard 
        numberOfRooms: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        floorLevel: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The floor level for an [[Accommodation]] in a multi-storey building. Since counting  systems [vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations), the local system should be used where possible.
        numberOfFullBathrooms: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).
        amenityFeature: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
        tourBookingPage: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.
        numberOfBathroomsTotal: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The total integer number of bathrooms in some [[Accommodation]], following real estate conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field): "The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms and one Half Bathroom, the Bathrooms Total Integer will be 3.". See also [[numberOfRooms]].
        numberOfBedrooms: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]].
        accommodationCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Category of an [[Accommodation]], following real estate conventions, e.g. RESO (see [PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field), and [PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field) fields  for suggested values).
        leaseLength: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.
        petsAllowed: (Optional[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]): Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        permittedUsage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indications regarding the permitted usage of the accommodation.
        numberOfPartialBathrooms: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field). 
        accommodationFloorPlan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A floorplan of some [[Accommodation]].
        yearBuilt: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field). 
    """

    floorSize: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfRooms: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    floorLevel: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfFullBathrooms: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    amenityFeature: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    tourBookingPage: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    numberOfBathroomsTotal: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    numberOfBedrooms: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    accommodationCategory: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    leaseLength: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    petsAllowed: NotRequired[Union[List[Union[str, SchemaOrgObj, StrictBool]], str, SchemaOrgObj, StrictBool]]
    permittedUsage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfPartialBathrooms: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    accommodationFloorPlan: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    yearBuilt: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    


class AllProperties(AccommodationInheritedProperties , AccommodationProperties, TypedDict):
    pass


class AccommodationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Accommodation",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'geoCovers': {'exclude': True}}
        fields = {'longitude': {'exclude': True}}
        fields = {'smokingAllowed': {'exclude': True}}
        fields = {'isicV4': {'exclude': True}}
        fields = {'globalLocationNumber': {'exclude': True}}
        fields = {'amenityFeature': {'exclude': True}}
        fields = {'additionalProperty': {'exclude': True}}
        fields = {'slogan': {'exclude': True}}
        fields = {'photos': {'exclude': True}}
        fields = {'keywords': {'exclude': True}}
        fields = {'reviews': {'exclude': True}}
        fields = {'tourBookingPage': {'exclude': True}}
        fields = {'geoWithin': {'exclude': True}}
        fields = {'containsPlace': {'exclude': True}}
        fields = {'review': {'exclude': True}}
        fields = {'hasMap': {'exclude': True}}
        fields = {'containedIn': {'exclude': True}}
        fields = {'events': {'exclude': True}}
        fields = {'geoOverlaps': {'exclude': True}}
        fields = {'geoEquals': {'exclude': True}}
        fields = {'maps': {'exclude': True}}
        fields = {'isAccessibleForFree': {'exclude': True}}
        fields = {'event': {'exclude': True}}
        fields = {'photo': {'exclude': True}}
        fields = {'containedInPlace': {'exclude': True}}
        fields = {'logo': {'exclude': True}}
        fields = {'geoCrosses': {'exclude': True}}
        fields = {'address': {'exclude': True}}
        fields = {'geo': {'exclude': True}}
        fields = {'openingHoursSpecification': {'exclude': True}}
        fields = {'geoDisjoint': {'exclude': True}}
        fields = {'geoIntersects': {'exclude': True}}
        fields = {'latitude': {'exclude': True}}
        fields = {'maximumAttendeeCapacity': {'exclude': True}}
        fields = {'aggregateRating': {'exclude': True}}
        fields = {'map': {'exclude': True}}
        fields = {'branchCode': {'exclude': True}}
        fields = {'faxNumber': {'exclude': True}}
        fields = {'publicAccess': {'exclude': True}}
        fields = {'geoTouches': {'exclude': True}}
        fields = {'geoCoveredBy': {'exclude': True}}
        fields = {'telephone': {'exclude': True}}
        fields = {'hasDriveThroughService': {'exclude': True}}
        fields = {'specialOpeningHoursSpecification': {'exclude': True}}
        fields = {'geoContains': {'exclude': True}}
        fields = {'floorSize': {'exclude': True}}
        fields = {'numberOfRooms': {'exclude': True}}
        fields = {'floorLevel': {'exclude': True}}
        fields = {'numberOfFullBathrooms': {'exclude': True}}
        fields = {'amenityFeature': {'exclude': True}}
        fields = {'tourBookingPage': {'exclude': True}}
        fields = {'numberOfBathroomsTotal': {'exclude': True}}
        fields = {'numberOfBedrooms': {'exclude': True}}
        fields = {'accommodationCategory': {'exclude': True}}
        fields = {'leaseLength': {'exclude': True}}
        fields = {'petsAllowed': {'exclude': True}}
        fields = {'permittedUsage': {'exclude': True}}
        fields = {'numberOfPartialBathrooms': {'exclude': True}}
        fields = {'accommodationFloorPlan': {'exclude': True}}
        fields = {'yearBuilt': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AccommodationProperties, AccommodationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Accommodation"
    return model
    

Accommodation = create_schema_org_model()


def create_accommodation_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_accommodation_model(model=model)
    return pydantic_type(model).schema_json()


