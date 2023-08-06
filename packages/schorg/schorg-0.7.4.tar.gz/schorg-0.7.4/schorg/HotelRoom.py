"""
A hotel room is a single room in a hotel.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

https://schema.org/HotelRoom
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HotelRoomInheritedProperties(TypedDict):
    """A hotel room is a single room in a hotel.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/HotelRoom
    Note:
        Model Depth 5
    Attributes:
    """


class HotelRoomProperties(TypedDict):
    """A hotel room is a single room in a hotel.<br /><br />See also the <a href="/docs/hotels.html">dedicated document on the use of schema.org for marking up hotels and other forms of accommodations</a>.

    References:
        https://schema.org/HotelRoom
    Note:
        Model Depth 5
    Attributes:
        bed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of bed or beds included in the accommodation. For the single case of just one bed of a certain type, you use bed directly with a text.      If you want to indicate the quantity of a certain kind of bed, use an instance of BedDetails. For more detailed information, use the amenityFeature property.
        occupancy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The allowed total occupancy for the accommodation in persons (including infants etc). For individual accommodations, this is not necessarily the legal maximum but defines the permitted usage as per the contractual agreement (e.g. a double room used by a single person).Typical unit code(s): C62 for person
    """

    bed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    occupancy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class HotelRoomAllProperties(
    HotelRoomInheritedProperties, HotelRoomProperties, TypedDict
):
    pass


class HotelRoomBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HotelRoom", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"bed": {"exclude": True}}
        fields = {"occupancy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        HotelRoomProperties, HotelRoomInheritedProperties, HotelRoomAllProperties
    ] = HotelRoomAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HotelRoom"
    return model


HotelRoom = create_schema_org_model()


def create_hotelroom_model(
    model: Union[
        HotelRoomProperties, HotelRoomInheritedProperties, HotelRoomAllProperties
    ]
):
    _type = deepcopy(HotelRoomAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of HotelRoomAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HotelRoomAllProperties):
    pydantic_type = create_hotelroom_model(model=model)
    return pydantic_type(model).schema_json()
