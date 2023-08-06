"""
A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Suite_(hotel)">http://en.wikipedia.org/wiki/Suite_(hotel)</a>).<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

https://schema.org/Suite
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SuiteInheritedProperties(TypedDict):
    """A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Suite_(hotel)">http://en.wikipedia.org/wiki/Suite_(hotel)</a>).<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/Suite
    Note:
        Model Depth 4
    Attributes:
        floorSize: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The size of the accommodation, e.g. in square meter or squarefoot.Typical unit code(s): MTK for square meter, FTK for square foot, or YDK for square yard
        numberOfRooms: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        floorLevel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The floor level for an [[Accommodation]] in a multi-storey building. Since counting  systems [vary internationally](https://en.wikipedia.org/wiki/Storey#Consecutive_number_floor_designations), the local system should be used where possible.
        numberOfFullBathrooms: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Number of full bathrooms - The total number of full and ¾ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsFull field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsFull+Field).
        amenityFeature: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
        tourBookingPage: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.
        numberOfBathroomsTotal: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The total integer number of bathrooms in some [[Accommodation]], following real estate conventions as [documented in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsTotalInteger+Field): "The simple sum of the number of bathrooms. For example for a property with two Full Bathrooms and one Half Bathroom, the Bathrooms Total Integer will be 3.". See also [[numberOfRooms]].
        numberOfBedrooms: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]].
        accommodationCategory: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Category of an [[Accommodation]], following real estate conventions, e.g. RESO (see [PropertySubType](https://ddwiki.reso.org/display/DDW17/PropertySubType+Field), and [PropertyType](https://ddwiki.reso.org/display/DDW17/PropertyType+Field) fields  for suggested values).
        leaseLength: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Length of the lease for some [[Accommodation]], either particular to some [[Offer]] or in some cases intrinsic to the property.
        petsAllowed: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        permittedUsage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indications regarding the permitted usage of the accommodation.
        numberOfPartialBathrooms: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): Number of partial bathrooms - The total number of half and ¼ bathrooms in an [[Accommodation]]. This corresponds to the [BathroomsPartial field in RESO](https://ddwiki.reso.org/display/DDW17/BathroomsPartial+Field).
        accommodationFloorPlan: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A floorplan of some [[Accommodation]].
        yearBuilt: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The year an [[Accommodation]] was constructed. This corresponds to the [YearBuilt field in RESO](https://ddwiki.reso.org/display/DDW17/YearBuilt+Field).
    """

    floorSize: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfRooms: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    floorLevel: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfFullBathrooms: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    amenityFeature: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    tourBookingPage: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    numberOfBathroomsTotal: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    numberOfBedrooms: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    accommodationCategory: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    leaseLength: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    petsAllowed: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    permittedUsage: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    numberOfPartialBathrooms: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    accommodationFloorPlan: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    yearBuilt: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class SuiteProperties(TypedDict):
    """A suite in a hotel or other public accommodation, denotes a class of luxury accommodations, the key feature of which is multiple rooms (source: Wikipedia, the free encyclopedia, see <a href="http://en.wikipedia.org/wiki/Suite_(hotel)">http://en.wikipedia.org/wiki/Suite_(hotel)</a>).<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/Suite
    Note:
        Model Depth 4
    Attributes:
        numberOfRooms: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        bed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of bed or beds included in the accommodation. For the single case of just one bed of a certain type, you use bed directly with a text.      If you want to indicate the quantity of a certain kind of bed, use an instance of BedDetails. For more detailed information, use the amenityFeature property.
        occupancy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).Typical unit code(s): C62 for person
    """

    numberOfRooms: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    bed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    occupancy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class SuiteAllProperties(SuiteInheritedProperties, SuiteProperties, TypedDict):
    pass


class SuiteBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Suite", alias="@id")
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
        fields = {"bed": {"exclude": True}}
        fields = {"occupancy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SuiteProperties, SuiteInheritedProperties, SuiteAllProperties
    ] = SuiteAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Suite"
    return model


Suite = create_schema_org_model()


def create_suite_model(
    model: Union[SuiteProperties, SuiteInheritedProperties, SuiteAllProperties]
):
    _type = deepcopy(SuiteAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SuiteAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SuiteAllProperties):
    pydantic_type = create_suite_model(model=model)
    return pydantic_type(model).schema_json()
