"""
An airline flight.

https://schema.org/Flight
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FlightInheritedProperties(TypedDict):
    """An airline flight.

    References:
        https://schema.org/Flight
    Note:
        Model Depth 4
    Attributes:
        departureTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The expected departure time.
        itinerary: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is important use [[ItemList]] to specify that order (see examples).
        provider: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        partOfTrip: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Identifies that this [[Trip]] is a subTrip of another Trip.  For example Day 1, Day 2, etc. of a multi-day trip.
        arrivalTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The expected arrival time.
        subTrip: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Identifies a [[Trip]] that is a subTrip of this Trip.  For example Day 1, Day 2, etc. of a multi-day trip.
        offers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
    """

    departureTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    itinerary: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    provider: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    partOfTrip: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    arrivalTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    subTrip: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    offers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class FlightProperties(TypedDict):
    """An airline flight.

    References:
        https://schema.org/Flight
    Note:
        Model Depth 4
    Attributes:
        seller: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.
        boardingPolicy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type of boarding policy used by the airline (e.g. zone-based or group-based).
        webCheckinTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The time when a passenger can check into the flight online.
        arrivalAirport: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The airport where the flight terminates.
        estimatedFlightDuration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The estimated time the flight will take.
        carrier: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): 'carrier' is an out-dated term indicating the 'provider' for parcel delivery and flights.
        departureAirport: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The airport where the flight originates.
        mealService: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Description of the meals that will be provided or available for purchase.
        flightDistance: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The distance of the flight.
        departureGate: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Identifier of the flight's departure gate.
        departureTerminal: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Identifier of the flight's departure terminal.
        arrivalTerminal: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Identifier of the flight's arrival terminal.
        flightNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The unique identifier for a flight including the airline IATA code. For example, if describing United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'.
        arrivalGate: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Identifier of the flight's arrival gate.
        aircraft: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The kind of aircraft (e.g., "Boeing 747").
    """

    seller: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    boardingPolicy: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    webCheckinTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    arrivalAirport: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    estimatedFlightDuration: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    carrier: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    departureAirport: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    mealService: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    flightDistance: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    departureGate: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    departureTerminal: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    arrivalTerminal: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    flightNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    arrivalGate: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    aircraft: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class FlightAllProperties(FlightInheritedProperties, FlightProperties, TypedDict):
    pass


class FlightBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Flight", alias="@id")
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
        fields = {"seller": {"exclude": True}}
        fields = {"boardingPolicy": {"exclude": True}}
        fields = {"webCheckinTime": {"exclude": True}}
        fields = {"arrivalAirport": {"exclude": True}}
        fields = {"estimatedFlightDuration": {"exclude": True}}
        fields = {"carrier": {"exclude": True}}
        fields = {"departureAirport": {"exclude": True}}
        fields = {"mealService": {"exclude": True}}
        fields = {"flightDistance": {"exclude": True}}
        fields = {"departureGate": {"exclude": True}}
        fields = {"departureTerminal": {"exclude": True}}
        fields = {"arrivalTerminal": {"exclude": True}}
        fields = {"flightNumber": {"exclude": True}}
        fields = {"arrivalGate": {"exclude": True}}
        fields = {"aircraft": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        FlightProperties, FlightInheritedProperties, FlightAllProperties
    ] = FlightAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Flight"
    return model


Flight = create_schema_org_model()


def create_flight_model(
    model: Union[FlightProperties, FlightInheritedProperties, FlightAllProperties]
):
    _type = deepcopy(FlightAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of FlightAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FlightAllProperties):
    pydantic_type = create_flight_model(model=model)
    return pydantic_type(model).schema_json()
