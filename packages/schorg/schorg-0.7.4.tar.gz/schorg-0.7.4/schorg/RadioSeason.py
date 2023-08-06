"""
Season dedicated to radio broadcast and associated online delivery.

https://schema.org/RadioSeason
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RadioSeasonInheritedProperties(TypedDict):
    """Season dedicated to radio broadcast and associated online delivery.

    References:
        https://schema.org/RadioSeason
    Note:
        Model Depth 4
    Attributes:
        seasonNumber: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Position of the season within an ordered group of seasons.
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        trailer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The trailer of a movie or TV/radio series, season, episode, etc.
        productionCompany: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        episodes: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An episode of a TV/radio series or season.
        partOfSeries: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The series to which this episode or season belongs.
        episode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An episode of a TV, radio or game media within a series or season.
        director: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        startDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        numberOfEpisodes: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of episodes in this season or series.
        endDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    seasonNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    trailer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    productionCompany: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    episodes: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    partOfSeries: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    episode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    director: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    startDate: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    numberOfEpisodes: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
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


class RadioSeasonProperties(TypedDict):
    """Season dedicated to radio broadcast and associated online delivery.

    References:
        https://schema.org/RadioSeason
    Note:
        Model Depth 4
    Attributes:
    """


class RadioSeasonAllProperties(
    RadioSeasonInheritedProperties, RadioSeasonProperties, TypedDict
):
    pass


class RadioSeasonBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RadioSeason", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"seasonNumber": {"exclude": True}}
        fields = {"actor": {"exclude": True}}
        fields = {"trailer": {"exclude": True}}
        fields = {"productionCompany": {"exclude": True}}
        fields = {"episodes": {"exclude": True}}
        fields = {"partOfSeries": {"exclude": True}}
        fields = {"episode": {"exclude": True}}
        fields = {"director": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"numberOfEpisodes": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RadioSeasonProperties, RadioSeasonInheritedProperties, RadioSeasonAllProperties
    ] = RadioSeasonAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RadioSeason"
    return model


RadioSeason = create_schema_org_model()


def create_radioseason_model(
    model: Union[
        RadioSeasonProperties, RadioSeasonInheritedProperties, RadioSeasonAllProperties
    ]
):
    _type = deepcopy(RadioSeasonAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RadioSeasonAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RadioSeasonAllProperties):
    pydantic_type = create_radioseason_model(model=model)
    return pydantic_type(model).schema_json()
