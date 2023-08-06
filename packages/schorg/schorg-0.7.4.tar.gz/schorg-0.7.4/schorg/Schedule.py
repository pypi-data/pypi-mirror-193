"""
A schedule defines a repeating time period used to describe a regularly occurring [[Event]]. At a minimum a schedule will specify [[repeatFrequency]] which describes the interval between occurrences of the event. Additional information can be provided to specify the schedule more precisely.      This includes identifying the day(s) of the week or month when the recurring event will take place, in addition to its start and end time. Schedules may also      have start and end dates to indicate when they are active, e.g. to define a limited calendar of events.

https://schema.org/Schedule
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ScheduleInheritedProperties(TypedDict):
    """A schedule defines a repeating time period used to describe a regularly occurring [[Event]]. At a minimum a schedule will specify [[repeatFrequency]] which describes the interval between occurrences of the event. Additional information can be provided to specify the schedule more precisely.      This includes identifying the day(s) of the week or month when the recurring event will take place, in addition to its start and end time. Schedules may also      have start and end dates to indicate when they are active, e.g. to define a limited calendar of events.

    References:
        https://schema.org/Schedule
    Note:
        Model Depth 3
    Attributes:
    """


class ScheduleProperties(TypedDict):
    """A schedule defines a repeating time period used to describe a regularly occurring [[Event]]. At a minimum a schedule will specify [[repeatFrequency]] which describes the interval between occurrences of the event. Additional information can be provided to specify the schedule more precisely.      This includes identifying the day(s) of the week or month when the recurring event will take place, in addition to its start and end time. Schedules may also      have start and end dates to indicate when they are active, e.g. to define a limited calendar of events.

    References:
        https://schema.org/Schedule
    Note:
        Model Depth 3
    Attributes:
        endTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. E.g. John wrote a book from January to *December*. For media, including audio and video, it's the time offset of the end of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        startTime: (Optional[Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]]): The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. E.g. John wrote a book from *January* to December. For media, including audio and video, it's the time offset of the start of a clip within a larger file.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.
        exceptDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): Defines a [[Date]] or [[DateTime]] during which a scheduled [[Event]] will not take place. The property allows exceptions to      a [[Schedule]] to be specified. If an exception is specified as a [[DateTime]] then only the event that would have started at that specific date and time      should be excluded from the schedule. If an exception is specified as a [[Date]] then any event that is scheduled for that 24 hour period should be      excluded from the schedule. This allows a whole day to be excluded from the schedule without having to itemise every scheduled event.
        repeatFrequency: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Defines the frequency at which [[Event]]s will occur according to a schedule [[Schedule]]. The intervals between      events should be defined as a [[Duration]] of time.
        scheduleTimezone: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the timezone for which the time(s) indicated in the [[Schedule]] are given. The value provided should be among those listed in the IANA Time Zone Database.
        byMonthWeek: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Defines the week(s) of the month on which a recurring Event takes place. Specified as an Integer between 1-5. For clarity, byMonthWeek is best used in conjunction with byDay to indicate concepts like the first and third Mondays of a month.
        duration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        byDay: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Defines the day(s) of the week on which a recurring [[Event]] takes place. May be specified using either [[DayOfWeek]], or alternatively [[Text]] conforming to iCal's syntax for byDay recurrence rules.
        byMonthDay: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Defines the day(s) of the month on which a recurring [[Event]] takes place. Specified as an [[Integer]] between 1-31.
        repeatCount: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Defines the number of times a recurring [[Event]] will take place.
        byMonth: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Defines the month(s) of the year on which a recurring [[Event]] takes place. Specified as an [[Integer]] between 1-12. January is 1.
        startDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    endTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    startTime: NotRequired[
        Union[List[Union[datetime, SchemaOrgObj, str]], datetime, SchemaOrgObj, str]
    ]
    exceptDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    repeatFrequency: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    scheduleTimezone: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    byMonthWeek: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    duration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    byDay: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    byMonthDay: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    repeatCount: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    byMonth: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    startDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]


class ScheduleAllProperties(ScheduleInheritedProperties, ScheduleProperties, TypedDict):
    pass


class ScheduleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Schedule", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"endTime": {"exclude": True}}
        fields = {"startTime": {"exclude": True}}
        fields = {"exceptDate": {"exclude": True}}
        fields = {"repeatFrequency": {"exclude": True}}
        fields = {"scheduleTimezone": {"exclude": True}}
        fields = {"byMonthWeek": {"exclude": True}}
        fields = {"duration": {"exclude": True}}
        fields = {"byDay": {"exclude": True}}
        fields = {"byMonthDay": {"exclude": True}}
        fields = {"repeatCount": {"exclude": True}}
        fields = {"byMonth": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ScheduleProperties, ScheduleInheritedProperties, ScheduleAllProperties
    ] = ScheduleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Schedule"
    return model


Schedule = create_schema_org_model()


def create_schedule_model(
    model: Union[ScheduleProperties, ScheduleInheritedProperties, ScheduleAllProperties]
):
    _type = deepcopy(ScheduleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ScheduleAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ScheduleAllProperties):
    pydantic_type = create_schedule_model(model=model)
    return pydantic_type(model).schema_json()
