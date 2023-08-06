"""
A trip on a commercial train line.

https://schema.org/TrainTrip
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TrainTripInheritedProperties(TypedDict):
    """A trip on a commercial train line.

    References:
        https://schema.org/TrainTrip
    Note:
        Model Depth 4
    Attributes:
        departureTime: (Optional[Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]]): The expected departure time.
        itinerary: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is important use [[ItemList]] to specify that order (see examples).
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        partOfTrip: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Identifies that this [[Trip]] is a subTrip of another Trip.  For example Day 1, Day 2, etc. of a multi-day trip.
        arrivalTime: (Optional[Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]]): The expected arrival time.
        subTrip: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Identifies a [[Trip]] that is a subTrip of this Trip.  For example Day 1, Day 2, etc. of a multi-day trip.
        offers: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
    """

    departureTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]
    ]
    itinerary: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    partOfTrip: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    arrivalTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]
    ]
    subTrip: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    offers: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TrainTripProperties(TypedDict):
    """A trip on a commercial train line.

    References:
        https://schema.org/TrainTrip
    Note:
        Model Depth 4
    Attributes:
        arrivalPlatform: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The platform where the train arrives.
        departurePlatform: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The platform from which the train departs.
        arrivalStation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The station where the train trip ends.
        trainName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The name of the train (e.g. The Orient Express).
        trainNumber: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The unique identifier for the train.
        departureStation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The station from which the train departs.
    """

    arrivalPlatform: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    departurePlatform: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    arrivalStation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    trainName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    trainNumber: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    departureStation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class TrainTripAllProperties(
    TrainTripInheritedProperties, TrainTripProperties, TypedDict
):
    pass


class TrainTripBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TrainTrip", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"departureTime": {"exclude": True}}
        fields = {"itinerary": {"exclude": True}}
        fields = {"provider": {"exclude": True}}
        fields = {"partOfTrip": {"exclude": True}}
        fields = {"arrivalTime": {"exclude": True}}
        fields = {"subTrip": {"exclude": True}}
        fields = {"offers": {"exclude": True}}
        fields = {"arrivalPlatform": {"exclude": True}}
        fields = {"departurePlatform": {"exclude": True}}
        fields = {"arrivalStation": {"exclude": True}}
        fields = {"trainName": {"exclude": True}}
        fields = {"trainNumber": {"exclude": True}}
        fields = {"departureStation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TrainTripProperties, TrainTripInheritedProperties, TrainTripAllProperties
    ] = TrainTripAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TrainTrip"
    return model


TrainTrip = create_schema_org_model()


def create_traintrip_model(
    model: Union[
        TrainTripProperties, TrainTripInheritedProperties, TrainTripAllProperties
    ]
):
    _type = deepcopy(TrainTripAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TrainTrip. Please see: https://schema.org/TrainTrip"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TrainTripAllProperties):
    pydantic_type = create_traintrip_model(model=model)
    return pydantic_type(model).schema_json()
