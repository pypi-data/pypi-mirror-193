"""
A video game series.

https://schema.org/VideoGameSeries
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VideoGameSeriesInheritedProperties(TypedDict):
    """A video game series.

    References:
        https://schema.org/VideoGameSeries
    Note:
        Model Depth 4
    Attributes:
        issn: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        startDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    issn: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
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


class VideoGameSeriesProperties(TypedDict):
    """A video game series.

    References:
        https://schema.org/VideoGameSeries
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        containsSeason: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A season that is part of the media series.
        characterAttribute: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).
        numberOfSeasons: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of seasons in this series.
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        cheatCode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Cheat codes to the game.
        season: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A season in a media series.
        gameLocation: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): Real or fictional location of the game (or part of game).
        trailer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The trailer of a movie or TV/radio series, season, episode, etc.
        productionCompany: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        episodes: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An episode of a TV/radio series or season.
        gamePlatform: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.
        numberOfPlayers: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicate how many people can play this game (minimum, maximum, or range).
        seasons: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A season in a media series.
        gameItem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.
        episode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An episode of a TV, radio or game media within a series or season.
        director: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        numberOfEpisodes: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of episodes in this season or series.
        directors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        quest: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The task that a player-controlled character, or group of characters may complete in order to gain a reward.
        musicBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The composer of the soundtrack.
        playMode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time.
    """

    actors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    containsSeason: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    characterAttribute: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    numberOfSeasons: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cheatCode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    season: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    gameLocation: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    trailer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    productionCompany: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    episodes: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gamePlatform: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    numberOfPlayers: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    seasons: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    gameItem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    episode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    director: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfEpisodes: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    directors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    quest: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    musicBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    playMode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class VideoGameSeriesAllProperties(
    VideoGameSeriesInheritedProperties, VideoGameSeriesProperties, TypedDict
):
    pass


class VideoGameSeriesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="VideoGameSeries", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"issn": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}
        fields = {"actors": {"exclude": True}}
        fields = {"containsSeason": {"exclude": True}}
        fields = {"characterAttribute": {"exclude": True}}
        fields = {"numberOfSeasons": {"exclude": True}}
        fields = {"actor": {"exclude": True}}
        fields = {"cheatCode": {"exclude": True}}
        fields = {"season": {"exclude": True}}
        fields = {"gameLocation": {"exclude": True}}
        fields = {"trailer": {"exclude": True}}
        fields = {"productionCompany": {"exclude": True}}
        fields = {"episodes": {"exclude": True}}
        fields = {"gamePlatform": {"exclude": True}}
        fields = {"numberOfPlayers": {"exclude": True}}
        fields = {"seasons": {"exclude": True}}
        fields = {"gameItem": {"exclude": True}}
        fields = {"episode": {"exclude": True}}
        fields = {"director": {"exclude": True}}
        fields = {"numberOfEpisodes": {"exclude": True}}
        fields = {"directors": {"exclude": True}}
        fields = {"quest": {"exclude": True}}
        fields = {"musicBy": {"exclude": True}}
        fields = {"playMode": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        VideoGameSeriesProperties,
        VideoGameSeriesInheritedProperties,
        VideoGameSeriesAllProperties,
    ] = VideoGameSeriesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VideoGameSeries"
    return model


VideoGameSeries = create_schema_org_model()


def create_videogameseries_model(
    model: Union[
        VideoGameSeriesProperties,
        VideoGameSeriesInheritedProperties,
        VideoGameSeriesAllProperties,
    ]
):
    _type = deepcopy(VideoGameSeriesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of VideoGameSeriesAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: VideoGameSeriesAllProperties):
    pydantic_type = create_videogameseries_model(model=model)
    return pydantic_type(model).schema_json()
