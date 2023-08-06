"""
Residence type: Apartment complex.

https://schema.org/ApartmentComplex
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ApartmentComplexInheritedProperties(TypedDict):
    """Residence type: Apartment complex.

    References:
        https://schema.org/ApartmentComplex
    Note:
        Model Depth 4
    Attributes:
        accommodationFloorPlan: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A floorplan of some [[Accommodation]].
    """

    accommodationFloorPlan: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ApartmentComplexProperties(TypedDict):
    """Residence type: Apartment complex.

    References:
        https://schema.org/ApartmentComplex
    Note:
        Model Depth 4
    Attributes:
        tourBookingPage: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A page providing information on how to book a tour of some [[Place]], such as an [[Accommodation]] or [[ApartmentComplex]] in a real estate setting, as well as other kinds of tours as appropriate.
        numberOfBedrooms: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The total integer number of bedrooms in a some [[Accommodation]], [[ApartmentComplex]] or [[FloorPlan]].
        numberOfAvailableAccommodationUnits: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the number of available accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAccommodationUnits]].
        numberOfAccommodationUnits: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the total (available plus unavailable) number of accommodation units in an [[ApartmentComplex]], or the number of accommodation units for a specific [[FloorPlan]] (within its specific [[ApartmentComplex]]). See also [[numberOfAvailableAccommodationUnits]].
        petsAllowed: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
    """

    tourBookingPage: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
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
    numberOfAvailableAccommodationUnits: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    numberOfAccommodationUnits: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    petsAllowed: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]


class ApartmentComplexAllProperties(
    ApartmentComplexInheritedProperties, ApartmentComplexProperties, TypedDict
):
    pass


class ApartmentComplexBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ApartmentComplex", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"accommodationFloorPlan": {"exclude": True}}
        fields = {"tourBookingPage": {"exclude": True}}
        fields = {"numberOfBedrooms": {"exclude": True}}
        fields = {"numberOfAvailableAccommodationUnits": {"exclude": True}}
        fields = {"numberOfAccommodationUnits": {"exclude": True}}
        fields = {"petsAllowed": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ApartmentComplexProperties,
        ApartmentComplexInheritedProperties,
        ApartmentComplexAllProperties,
    ] = ApartmentComplexAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ApartmentComplex"
    return model


ApartmentComplex = create_schema_org_model()


def create_apartmentcomplex_model(
    model: Union[
        ApartmentComplexProperties,
        ApartmentComplexInheritedProperties,
        ApartmentComplexAllProperties,
    ]
):
    _type = deepcopy(ApartmentComplexAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ApartmentComplexAllProperties):
    pydantic_type = create_apartmentcomplex_model(model=model)
    return pydantic_type(model).schema_json()
