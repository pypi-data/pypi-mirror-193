"""
Event type: A social dance.

https://schema.org/DanceEvent
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DanceEventInheritedProperties(TypedDict):
    """Event type: A social dance.

    References:
        https://schema.org/DanceEvent
    Note:
        Model Depth 3
    Attributes:
        performer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A performer at the event&#x2014;for example, a presenter, musician, musical group or actor.
        eventAttendanceMode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The eventAttendanceMode of an event indicates whether it occurs online, offline, or a mix.
        workFeatured: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A work featured in some event, e.g. exhibited in an ExhibitionEvent.       Specific subproperties are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).
        remainingAttendeeCapacity: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of attendee places for an event that remain unallocated.
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        doorTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The time admission will commence.
        previousStartDate: (Optional[Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]]): Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated.
        recordedIn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The CreativeWork that captured all or part of this Event.
        keywords: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Keywords or tags used to describe some item. Multiple textual entries in a keywords list are typically delimited by commas, or by repeating the property.
        contributor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A secondary contributor to the CreativeWork or Event.
        superEvent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.
        eventSchedule: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Associates an [[Event]] with a [[Schedule]]. There are circumstances where it is preferable to share a schedule for a series of      repeating events rather than data on the individual events themselves. For example, a website or application might prefer to publish a schedule for a weekly      gym class rather than provide data on every event. A schedule could be processed by applications to add forthcoming events to a calendar. An [[Event]] that      is associated with a [[Schedule]] using this property should not have [[startDate]] or [[endDate]] properties. These are instead defined within the associated      [[Schedule]], this avoids any ambiguity for clients using the data. The property might have repeated values to specify different schedules, e.g. for different months      or seasons.
        maximumVirtualAttendeeCapacity: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]] is [[OnlineEventAttendanceMode]] (or the online aspects, in the case of a [[MixedEventAttendanceMode]]).
        attendees: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person attending the event.
        review: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A review of the item.
        eventStatus: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled.
        funding: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A [[Grant]] that directly or indirectly provide funding or sponsorship for this item. See also [[ownershipFundingInfo]].
        workPerformed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A work performed in some event, for example a play performed in a TheaterEvent.
        duration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        about: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The subject matter of the content.
        composer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The person or organization who wrote a composition, or who is the composer of a work performed at some event.
        funder: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization that supports (sponsors) something through some kind of financial contribution.
        isAccessibleForFree: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): A flag to signal that the item, event, or place is accessible for free.
        subEvent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference.
        typicalAgeRange: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The typical expected age range, e.g. '7-9', '11-'.
        audience: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An intended audience, i.e. a group for whom something was created.
        attendee: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization attending the event.
        subEvents: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Events that are a part of this event. For example, a conference event includes many presentations, each subEvents of the conference.
        performers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The main performer or performers of the event&#x2014;for example, a presenter, musician, or actor.
        maximumAttendeeCapacity: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The total number of individuals that may attend an event or venue.
        translator: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.
        aggregateRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The overall rating, based on a collection of reviews or ratings, of the item.
        maximumPhysicalAttendeeCapacity: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The maximum physical attendee capacity of an [[Event]] whose [[eventAttendanceMode]] is [[OfflineEventAttendanceMode]] (or the offline aspects, in the case of a [[MixedEventAttendanceMode]]).
        director: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        inLanguage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The language of the content or performance or used in an action. Please use one of the language codes from the [IETF BCP 47 standard](http://tools.ietf.org/html/bcp47). See also [[availableLanguage]].
        startDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        offers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event. Use [[businessFunction]] to indicate the kind of transaction offered, i.e. sell, lease, etc. This property can also be used to describe a [[Demand]]. While this property is listed as expected on a number of common types, it can be used in others. In that case, using a second type, such as Product or a subtype of Product, can clarify the nature of the offer.
        endDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        location: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location of, for example, where an event is happening, where an organization is located, or where an action takes place.
        sponsor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A person or organization that supports a thing through a pledge, promise, or financial contribution. E.g. a sponsor of a Medical Study or a corporate sponsor of an event.
        organizer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An organizer of an Event.
    """

    performer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    eventAttendanceMode: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    workFeatured: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    remainingAttendeeCapacity: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    doorTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    previousStartDate: NotRequired[
        Union[List[Union[date, SchemaOrgObj, str]], date, SchemaOrgObj, str]
    ]
    recordedIn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    keywords: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    contributor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    superEvent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    eventSchedule: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    maximumVirtualAttendeeCapacity: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    attendees: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    review: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    eventStatus: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    funding: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    workPerformed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    duration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    about: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    composer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    funder: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    isAccessibleForFree: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]
    subEvent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    typicalAgeRange: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    audience: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    attendee: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    subEvents: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    performers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    maximumAttendeeCapacity: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    translator: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    aggregateRating: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    maximumPhysicalAttendeeCapacity: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    director: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    inLanguage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    startDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    offers: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    endDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    location: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    sponsor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    organizer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class DanceEventProperties(TypedDict):
    """Event type: A social dance.

    References:
        https://schema.org/DanceEvent
    Note:
        Model Depth 3
    Attributes:
    """


class DanceEventAllProperties(
    DanceEventInheritedProperties, DanceEventProperties, TypedDict
):
    pass


class DanceEventBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DanceEvent", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"performer": {"exclude": True}}
        fields = {"eventAttendanceMode": {"exclude": True}}
        fields = {"workFeatured": {"exclude": True}}
        fields = {"remainingAttendeeCapacity": {"exclude": True}}
        fields = {"actor": {"exclude": True}}
        fields = {"doorTime": {"exclude": True}}
        fields = {"previousStartDate": {"exclude": True}}
        fields = {"recordedIn": {"exclude": True}}
        fields = {"keywords": {"exclude": True}}
        fields = {"contributor": {"exclude": True}}
        fields = {"superEvent": {"exclude": True}}
        fields = {"eventSchedule": {"exclude": True}}
        fields = {"maximumVirtualAttendeeCapacity": {"exclude": True}}
        fields = {"attendees": {"exclude": True}}
        fields = {"review": {"exclude": True}}
        fields = {"eventStatus": {"exclude": True}}
        fields = {"funding": {"exclude": True}}
        fields = {"workPerformed": {"exclude": True}}
        fields = {"duration": {"exclude": True}}
        fields = {"about": {"exclude": True}}
        fields = {"composer": {"exclude": True}}
        fields = {"funder": {"exclude": True}}
        fields = {"isAccessibleForFree": {"exclude": True}}
        fields = {"subEvent": {"exclude": True}}
        fields = {"typicalAgeRange": {"exclude": True}}
        fields = {"audience": {"exclude": True}}
        fields = {"attendee": {"exclude": True}}
        fields = {"subEvents": {"exclude": True}}
        fields = {"performers": {"exclude": True}}
        fields = {"maximumAttendeeCapacity": {"exclude": True}}
        fields = {"translator": {"exclude": True}}
        fields = {"aggregateRating": {"exclude": True}}
        fields = {"maximumPhysicalAttendeeCapacity": {"exclude": True}}
        fields = {"director": {"exclude": True}}
        fields = {"inLanguage": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"offers": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}
        fields = {"location": {"exclude": True}}
        fields = {"sponsor": {"exclude": True}}
        fields = {"organizer": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DanceEventProperties, DanceEventInheritedProperties, DanceEventAllProperties
    ] = DanceEventAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DanceEvent"
    return model


DanceEvent = create_schema_org_model()


def create_danceevent_model(
    model: Union[
        DanceEventProperties, DanceEventInheritedProperties, DanceEventAllProperties
    ]
):
    _type = deepcopy(DanceEventAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DanceEventAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DanceEventAllProperties):
    pydantic_type = create_danceevent_model(model=model)
    return pydantic_type(model).schema_json()
