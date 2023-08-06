"""
A trip or journey. An itinerary of visits to one or more places.

https://schema.org/Trip
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TripInheritedProperties(TypedDict):
    """A trip or journey. An itinerary of visits to one or more places.

    References:
        https://schema.org/Trip
    Note:
        Model Depth 3
    Attributes:
    """

    


class TripProperties(TypedDict):
    """A trip or journey. An itinerary of visits to one or more places.

    References:
        https://schema.org/Trip
    Note:
        Model Depth 3
    Attributes:
        departureTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The expected departure time.
        itinerary: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Destination(s) ( [[Place]] ) that make up a trip. For a trip where destination order is important use [[ItemList]] to specify that order (see examples).
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        partOfTrip: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Identifies that this [[Trip]] is a subTrip of another Trip.  For example Day 1, Day 2, etc. of a multi-day trip.
        arrivalTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The expected arrival time.
        subTrip: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Identifies a [[Trip]] that is a subTrip of this Trip.  For example Day 1, Day 2, etc. of a multi-day trip.
        offers: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.      
    """

    departureTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    itinerary: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    partOfTrip: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    arrivalTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    subTrip: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    offers: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(TripInheritedProperties , TripProperties, TypedDict):
    pass


class TripBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Trip",alias='@id')
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
        


def create_schema_org_model(type_: Union[TripProperties, TripInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Trip"
    return model
    

Trip = create_schema_org_model()


def create_trip_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_trip_model(model=model)
    return pydantic_type(model).schema_json()


