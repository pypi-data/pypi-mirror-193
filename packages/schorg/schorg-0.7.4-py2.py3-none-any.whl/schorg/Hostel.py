"""
A hostel - cheap accommodation, often in shared dormitories.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

https://schema.org/Hostel
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HostelInheritedProperties(TypedDict):
    """A hostel - cheap accommodation, often in shared dormitories.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/Hostel
    Note:
        Model Depth 5
    Attributes:
        numberOfRooms: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The number of rooms (excluding bathrooms and closets) of the accommodation or lodging business.Typical unit code(s): ROM for room or C62 for no unit. The type of room can be put in the unitText property of the QuantitativeValue.
        availableLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A language someone may use with or at the item, service or place. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[inLanguage]].
        amenityFeature: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An amenity feature (e.g. a characteristic or service) of the Accommodation. This generic property does not make a statement about whether the feature is included in an offer for the main accommodation or available at extra costs.
        checkoutTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The latest someone may check out of a lodging establishment.
        starRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An official rating for a lodging business or food establishment, e.g. from national associations or standards bodies. Use the author property to indicate the rating organization, e.g. as an Organization with name such as (e.g. HOTREC, DEHOGA, WHR, or Hotelstars).
        audience: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An intended audience, i.e. a group for whom something was created.
        petsAllowed: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether pets are allowed to enter the accommodation or lodging business. More detailed information can be put in a text value.
        checkinTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The earliest someone may check into a lodging establishment.
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
    availableLanguage: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    amenityFeature: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    checkoutTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    starRating: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    audience: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    petsAllowed: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    checkinTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]


class HostelProperties(TypedDict):
    """A hostel - cheap accommodation, often in shared dormitories.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/Hostel
    Note:
        Model Depth 5
    Attributes:
    """


class HostelAllProperties(HostelInheritedProperties, HostelProperties, TypedDict):
    pass


class HostelBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Hostel", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"numberOfRooms": {"exclude": True}}
        fields = {"availableLanguage": {"exclude": True}}
        fields = {"amenityFeature": {"exclude": True}}
        fields = {"checkoutTime": {"exclude": True}}
        fields = {"starRating": {"exclude": True}}
        fields = {"audience": {"exclude": True}}
        fields = {"petsAllowed": {"exclude": True}}
        fields = {"checkinTime": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HostelProperties, HostelInheritedProperties, HostelAllProperties
    ] = HostelAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Hostel"
    return model


Hostel = create_schema_org_model()


def create_hostel_model(
    model: Union[HostelProperties, HostelInheritedProperties, HostelAllProperties]
):
    _type = deepcopy(HostelAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of HostelAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HostelAllProperties):
    pydantic_type = create_hostel_model(model=model)
    return pydantic_type(model).schema_json()
