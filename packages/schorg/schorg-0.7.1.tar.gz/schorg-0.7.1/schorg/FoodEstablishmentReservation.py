"""
A reservation to dine at a food-related business.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

https://schema.org/FoodEstablishmentReservation
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FoodEstablishmentReservationInheritedProperties(TypedDict):
    """A reservation to dine at a food-related business.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    References:
        https://schema.org/FoodEstablishmentReservation
    Note:
        Model Depth 4
    Attributes:
        broker: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        modifiedTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The date and time the reservation was modified.
        programMembershipUsed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the reservation.
        bookingAgent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): 'bookingAgent' is an out-dated term indicating a 'broker' that serves as a booking agent.
        totalPrice: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The total price for the reservation or ticket, including applicable taxes, shipping, etc.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        reservedTicket: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A ticket associated with the reservation.
        reservationId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A unique identifier for the reservation.
        reservationFor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The thing -- flight, event, restaurant, etc. being reserved.
        underName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The person or organization the reservation or ticket is for.
        bookingTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The date and time the reservation was booked.
        reservationStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The current status of the reservation.
        priceCurrency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    """

    broker: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    modifiedTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    programMembershipUsed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bookingAgent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    totalPrice: NotRequired[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]
    reservedTicket: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reservationId: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reservationFor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    underName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bookingTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    reservationStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    priceCurrency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class FoodEstablishmentReservationProperties(TypedDict):
    """A reservation to dine at a food-related business.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations.

    References:
        https://schema.org/FoodEstablishmentReservation
    Note:
        Model Depth 4
    Attributes:
        endTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        startTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        partySize: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Number of people the reservation should accommodate.
    """

    endTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    startTime: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]
    partySize: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    


class AllProperties(FoodEstablishmentReservationInheritedProperties , FoodEstablishmentReservationProperties, TypedDict):
    pass


class FoodEstablishmentReservationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="FoodEstablishmentReservation",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'broker': {'exclude': True}}
        fields = {'provider': {'exclude': True}}
        fields = {'modifiedTime': {'exclude': True}}
        fields = {'programMembershipUsed': {'exclude': True}}
        fields = {'bookingAgent': {'exclude': True}}
        fields = {'totalPrice': {'exclude': True}}
        fields = {'reservedTicket': {'exclude': True}}
        fields = {'reservationId': {'exclude': True}}
        fields = {'reservationFor': {'exclude': True}}
        fields = {'underName': {'exclude': True}}
        fields = {'bookingTime': {'exclude': True}}
        fields = {'reservationStatus': {'exclude': True}}
        fields = {'priceCurrency': {'exclude': True}}
        fields = {'endTime': {'exclude': True}}
        fields = {'startTime': {'exclude': True}}
        fields = {'partySize': {'exclude': True}}
        


def create_schema_org_model(type_: Union[FoodEstablishmentReservationProperties, FoodEstablishmentReservationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FoodEstablishmentReservation"
    return model
    

FoodEstablishmentReservation = create_schema_org_model()


def create_foodestablishmentreservation_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_foodestablishmentreservation_model(model=model)
    return pydantic_type(model).schema_json()


