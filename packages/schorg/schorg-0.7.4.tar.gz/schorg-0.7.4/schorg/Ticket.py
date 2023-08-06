"""
Used to describe a ticket to an event, a flight, a bus ride, etc.

https://schema.org/Ticket
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TicketInheritedProperties(TypedDict):
    """Used to describe a ticket to an event, a flight, a bus ride, etc.

    References:
        https://schema.org/Ticket
    Note:
        Model Depth 3
    Attributes:
    """


class TicketProperties(TypedDict):
    """Used to describe a ticket to an event, a flight, a bus ride, etc.

    References:
        https://schema.org/Ticket
    Note:
        Model Depth 3
    Attributes:
        ticketNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The unique identifier for the ticket.
        issuedBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The organization issuing the ticket or permit.
        ticketToken: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.
        totalPrice: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The total price for the reservation or ticket, including applicable taxes, shipping, etc.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        underName: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The person or organization the reservation or ticket is for.
        ticketedSeat: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The seat associated with the ticket.
        priceCurrency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
        dateIssued: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The date the ticket was issued.
    """

    ticketNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    issuedBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    ticketToken: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    totalPrice: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    underName: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    ticketedSeat: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    priceCurrency: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    dateIssued: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]


class TicketAllProperties(TicketInheritedProperties, TicketProperties, TypedDict):
    pass


class TicketBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Ticket", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"ticketNumber": {"exclude": True}}
        fields = {"issuedBy": {"exclude": True}}
        fields = {"ticketToken": {"exclude": True}}
        fields = {"totalPrice": {"exclude": True}}
        fields = {"underName": {"exclude": True}}
        fields = {"ticketedSeat": {"exclude": True}}
        fields = {"priceCurrency": {"exclude": True}}
        fields = {"dateIssued": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TicketProperties, TicketInheritedProperties, TicketAllProperties
    ] = TicketAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Ticket"
    return model


Ticket = create_schema_org_model()


def create_ticket_model(
    model: Union[TicketProperties, TicketInheritedProperties, TicketAllProperties]
):
    _type = deepcopy(TicketAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of TicketAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TicketAllProperties):
    pydantic_type = create_ticket_model(model=model)
    return pydantic_type(model).schema_json()
