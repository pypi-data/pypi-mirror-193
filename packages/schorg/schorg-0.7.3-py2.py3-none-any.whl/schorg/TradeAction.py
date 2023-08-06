"""
The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.

https://schema.org/TradeAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TradeActionInheritedProperties(TypedDict):
    """The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.

    References:
        https://schema.org/TradeAction
    Note:
        Model Depth 3
    Attributes:
        endTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        provider: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.
        startTime: (Optional[Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]]): The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        result: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The result produced in the action. E.g. John wrote *a book*.
        actionStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the current disposition of the Action.
        agent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The direct performer or driver of the action (animate or inanimate). E.g. *John* wrote a book.
        instrument: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The object that helped the agent perform the action. E.g. John wrote a book with *a pen*.
        object: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The object upon which the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). E.g. John read *a book*.
        error: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): For failed actions, more information on the cause of the failure.
        target: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates a target EntryPoint, or url, for an Action.
        location: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        participant: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Other co-agents that participated in the action indirectly. E.g. John wrote a book with *Steve*.
    """

    endTime: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    provider: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startTime: NotRequired[
        Union[List[Union[datetime, str, SchemaOrgObj]], datetime, str, SchemaOrgObj]
    ]
    result: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actionStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    agent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    instrument: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    object: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    error: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    target: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    location: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    participant: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TradeActionProperties(TypedDict):
    """The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.

    References:
        https://schema.org/TradeAction
    Note:
        Model Depth 3
    Attributes:
        price: (Optional[Union[List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]], str, StrictInt, StrictFloat, SchemaOrgObj]]): The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.Usage guidelines:* Use the [[priceCurrency]] property (with standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR") instead of including [ambiguous symbols](http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign) such as '$' in the value.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.* Note that both [RDFa](http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute) and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values alongside more human-friendly formatting.* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.
        priceSpecification: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One or more detailed price specifications, indicating the unit price and delivery or payment charges.
        priceCurrency: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The currency of the price, or a price component when attached to [[PriceSpecification]] and its subtypes.Use standard formats: [ISO 4217 currency format](http://en.wikipedia.org/wiki/ISO_4217), e.g. "USD"; [Ticker symbol](https://en.wikipedia.org/wiki/List_of_cryptocurrencies) for cryptocurrencies, e.g. "BTC"; well known names for [Local Exchange Trading Systems](https://en.wikipedia.org/wiki/Local_exchange_trading_system) (LETS) and other currency types, e.g. "Ithaca HOUR".
    """

    price: NotRequired[
        Union[
            List[Union[str, StrictInt, StrictFloat, SchemaOrgObj]],
            str,
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
        ]
    ]
    priceSpecification: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    priceCurrency: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TradeActionAllProperties(
    TradeActionInheritedProperties, TradeActionProperties, TypedDict
):
    pass


class TradeActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TradeAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"endTime": {"exclude": True}}
        fields = {"provider": {"exclude": True}}
        fields = {"startTime": {"exclude": True}}
        fields = {"result": {"exclude": True}}
        fields = {"actionStatus": {"exclude": True}}
        fields = {"agent": {"exclude": True}}
        fields = {"instrument": {"exclude": True}}
        fields = {"object": {"exclude": True}}
        fields = {"error": {"exclude": True}}
        fields = {"target": {"exclude": True}}
        fields = {"location": {"exclude": True}}
        fields = {"participant": {"exclude": True}}
        fields = {"price": {"exclude": True}}
        fields = {"priceSpecification": {"exclude": True}}
        fields = {"priceCurrency": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TradeActionProperties, TradeActionInheritedProperties, TradeActionAllProperties
    ] = TradeActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TradeAction"
    return model


TradeAction = create_schema_org_model()


def create_tradeaction_model(
    model: Union[
        TradeActionProperties, TradeActionInheritedProperties, TradeActionAllProperties
    ]
):
    _type = deepcopy(TradeActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TradeActionAllProperties):
    pydantic_type = create_tradeaction_model(model=model)
    return pydantic_type(model).schema_json()
