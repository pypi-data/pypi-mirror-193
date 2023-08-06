"""
An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>).

https://schema.org/Apartment
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ApartmentInheritedProperties(TypedDict):
    """An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>).

    References:
        https://schema.org/Apartment
    Note:
        Model Depth 4
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
        petsAllowed: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        permittedUsage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indications regarding the permitted usage of the accommodation.
        numberOfPartialBathrooms: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field).
        accommodationFloorPlan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A floorplan of some [[Accommodation]].
        yearBuilt: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field).
    """

    floorSize: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfRooms: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    floorLevel: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfFullBathrooms: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    amenityFeature: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    tourBookingPage: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    numberOfBathroomsTotal: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    numberOfBedrooms: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    accommodationCategory: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    leaseLength: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    petsAllowed: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]
    permittedUsage: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    numberOfPartialBathrooms: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    accommodationFloorPlan: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    yearBuilt: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]


class ApartmentProperties(TypedDict):
    """An apartment (in American English) or flat (in British English) is a self-contained housing unit (a type of residential real estate) that occupies only part of a building (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Apartment">http://en.wikipedia.org/wiki/Apartment</a>).

    References:
        https://schema.org/Apartment
    Note:
        Model Depth 4
    Attributes:
        numberOfRooms: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        occupancy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).Typical unit code(s): C62 for person
    """

    numberOfRooms: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    occupancy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ApartmentAllProperties(
    ApartmentInheritedProperties, ApartmentProperties, TypedDict
):
    pass


class ApartmentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Apartment", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"floorSize": {"exclude": True}}
        fields = {"numberOfRooms": {"exclude": True}}
        fields = {"floorLevel": {"exclude": True}}
        fields = {"numberOfFullBathrooms": {"exclude": True}}
        fields = {"amenityFeature": {"exclude": True}}
        fields = {"tourBookingPage": {"exclude": True}}
        fields = {"numberOfBathroomsTotal": {"exclude": True}}
        fields = {"numberOfBedrooms": {"exclude": True}}
        fields = {"accommodationCategory": {"exclude": True}}
        fields = {"leaseLength": {"exclude": True}}
        fields = {"petsAllowed": {"exclude": True}}
        fields = {"permittedUsage": {"exclude": True}}
        fields = {"numberOfPartialBathrooms": {"exclude": True}}
        fields = {"accommodationFloorPlan": {"exclude": True}}
        fields = {"yearBuilt": {"exclude": True}}
        fields = {"numberOfRooms": {"exclude": True}}
        fields = {"occupancy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ApartmentProperties, ApartmentInheritedProperties, ApartmentAllProperties
    ] = ApartmentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Apartment"
    return model


Apartment = create_schema_org_model()


def create_apartment_model(
    model: Union[
        ApartmentProperties, ApartmentInheritedProperties, ApartmentAllProperties
    ]
):
    _type = deepcopy(ApartmentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ApartmentAllProperties):
    pydantic_type = create_apartment_model(model=model)
    return pydantic_type(model).schema_json()
