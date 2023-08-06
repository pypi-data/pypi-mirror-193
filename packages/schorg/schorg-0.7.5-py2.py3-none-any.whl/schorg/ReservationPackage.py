"""
A group of multiple reservations with common values for all sub-reservations.

https://schema.org/ReservationPackage
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReservationPackageInheritedProperties(TypedDict):
    """A group of multiple reservations with common values for all sub-reservations.

    References:
        https://schema.org/ReservationPackage
    Note:
        Model Depth 4
    Attributes:
        broker: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        modifiedTime: (Optional[Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]]): The date and time the reservation was modified.
        programMembershipUsed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the reservation.
        bookingAgent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): 'bookingAgent' is an out-dated term indicating a 'broker' that serves as a booking agent.
        totalPrice: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The total price for the reservation or ticket, including applicable taxes, shipping, etc.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        reservedTicket: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A ticket associated with the reservation.
        reservationId: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A unique identifier for the reservation.
        reservationFor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The thing -- flight, event, restaurant, etc. being reserved.
        underName: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The person or organization the reservation or ticket is for.
        bookingTime: (Optional[Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]]): The date and time the reservation was booked.
        reservationStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The current status of the reservation.
        priceCurrency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    """

    broker: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    modifiedTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]
    ]
    programMembershipUsed: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    bookingAgent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    totalPrice: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    reservedTicket: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    reservationId: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reservationFor: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    underName: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bookingTime: NotRequired[
        Union[List[Union[str, SchemaOrgObj, datetime]], str, SchemaOrgObj, datetime]
    ]
    reservationStatus: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    priceCurrency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ReservationPackageProperties(TypedDict):
    """A group of multiple reservations with common values for all sub-reservations.

    References:
        https://schema.org/ReservationPackage
    Note:
        Model Depth 4
    Attributes:
        subReservation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The individual reservations included in the package. Typically a repeated property.
    """

    subReservation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ReservationPackageAllProperties(
    ReservationPackageInheritedProperties, ReservationPackageProperties, TypedDict
):
    pass


class ReservationPackageBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReservationPackage", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"broker": {"exclude": True}}
        fields = {"provider": {"exclude": True}}
        fields = {"modifiedTime": {"exclude": True}}
        fields = {"programMembershipUsed": {"exclude": True}}
        fields = {"bookingAgent": {"exclude": True}}
        fields = {"totalPrice": {"exclude": True}}
        fields = {"reservedTicket": {"exclude": True}}
        fields = {"reservationId": {"exclude": True}}
        fields = {"reservationFor": {"exclude": True}}
        fields = {"underName": {"exclude": True}}
        fields = {"bookingTime": {"exclude": True}}
        fields = {"reservationStatus": {"exclude": True}}
        fields = {"priceCurrency": {"exclude": True}}
        fields = {"subReservation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReservationPackageProperties,
        ReservationPackageInheritedProperties,
        ReservationPackageAllProperties,
    ] = ReservationPackageAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationPackage"
    return model


ReservationPackage = create_schema_org_model()


def create_reservationpackage_model(
    model: Union[
        ReservationPackageProperties,
        ReservationPackageInheritedProperties,
        ReservationPackageAllProperties,
    ]
):
    _type = deepcopy(ReservationPackageAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReservationPackage. Please see: https://schema.org/ReservationPackage"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReservationPackageAllProperties):
    pydantic_type = create_reservationpackage_model(model=model)
    return pydantic_type(model).schema_json()
