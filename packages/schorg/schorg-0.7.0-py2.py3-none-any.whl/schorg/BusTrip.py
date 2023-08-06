"""
A trip on a commercial bus line.

https://schema.org/BusTrip
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BusTripInheritedProperties(TypedDict):
    """A trip on a commercial bus line.

    References:
        https://schema.org/BusTrip
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

    departureTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    itinerary: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    provider: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    partOfTrip: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    arrivalTime: NotRequired[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]
    subTrip: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    offers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class BusTripProperties(TypedDict):
    """A trip on a commercial bus line.

    References:
        https://schema.org/BusTrip
    Note:
        Model Depth 4
    Attributes:
        busName: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The name of the bus (e.g. Bolt Express).
        busNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The unique identifier for the bus.
        departureBusStop: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The stop or station from which the bus departs.
        arrivalBusStop: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The stop or station from which the bus arrives.
    """

    busName: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    busNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    departureBusStop: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    arrivalBusStop: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(BusTripInheritedProperties , BusTripProperties, TypedDict):
    pass


class BusTripBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BusTrip",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'departureTime': {'exclude': True}}
        fields = {'itinerary': {'exclude': True}}
        fields = {'provider': {'exclude': True}}
        fields = {'partOfTrip': {'exclude': True}}
        fields = {'arrivalTime': {'exclude': True}}
        fields = {'subTrip': {'exclude': True}}
        fields = {'offers': {'exclude': True}}
        fields = {'busName': {'exclude': True}}
        fields = {'busNumber': {'exclude': True}}
        fields = {'departureBusStop': {'exclude': True}}
        fields = {'arrivalBusStop': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BusTripProperties, BusTripInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BusTrip"
    return model
    

BusTrip = create_schema_org_model()


def create_bustrip_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bustrip_model(model=model)
    return pydantic_type(model).schema_json()


