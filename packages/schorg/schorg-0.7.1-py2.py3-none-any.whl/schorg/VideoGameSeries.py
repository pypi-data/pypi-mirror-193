"""
A video game series.

https://schema.org/VideoGameSeries
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VideoGameSeriesInheritedProperties(TypedDict):
    """A video game series.

    References:
        https://schema.org/VideoGameSeries
    Note:
        Model Depth 4
    Attributes:
        issn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    issn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startDate: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    endDate: NotRequired[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]
    


class VideoGameSeriesProperties(TypedDict):
    """A video game series.

    References:
        https://schema.org/VideoGameSeries
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        containsSeason: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A season that is part of the media series.
        characterAttribute: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).
        numberOfSeasons: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of seasons in this series.
        actor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        cheatCode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Cheat codes to the game.
        season: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A season in a media series.
        gameLocation: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Real or fictional location of the game (or part of game).
        trailer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The trailer of a movie or TV/radio series, season, episode, etc.
        productionCompany: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        episodes: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An episode of a TV/radio series or season.
        gamePlatform: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.
        numberOfPlayers: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicate how many people can play this game (minimum, maximum, or range).
        seasons: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A season in a media series.
        gameItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.
        episode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An episode of a TV, radio or game media within a series or season.
        director: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        numberOfEpisodes: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of episodes in this season or series.
        directors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        quest: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The task that a player-controlled character, or group of characters may complete in order to gain a reward.
        musicBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The composer of the soundtrack.
        playMode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time.
    """

    actors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    containsSeason: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    characterAttribute: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfSeasons: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    actor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cheatCode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    season: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    gameLocation: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    trailer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    productionCompany: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    episodes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gamePlatform: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    numberOfPlayers: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    seasons: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    gameItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    episode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    director: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfEpisodes: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    directors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    quest: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    musicBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    playMode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(VideoGameSeriesInheritedProperties , VideoGameSeriesProperties, TypedDict):
    pass


class VideoGameSeriesBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VideoGameSeries",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'issn': {'exclude': True}}
        fields = {'startDate': {'exclude': True}}
        fields = {'endDate': {'exclude': True}}
        fields = {'actors': {'exclude': True}}
        fields = {'containsSeason': {'exclude': True}}
        fields = {'characterAttribute': {'exclude': True}}
        fields = {'numberOfSeasons': {'exclude': True}}
        fields = {'actor': {'exclude': True}}
        fields = {'cheatCode': {'exclude': True}}
        fields = {'season': {'exclude': True}}
        fields = {'gameLocation': {'exclude': True}}
        fields = {'trailer': {'exclude': True}}
        fields = {'productionCompany': {'exclude': True}}
        fields = {'episodes': {'exclude': True}}
        fields = {'gamePlatform': {'exclude': True}}
        fields = {'numberOfPlayers': {'exclude': True}}
        fields = {'seasons': {'exclude': True}}
        fields = {'gameItem': {'exclude': True}}
        fields = {'episode': {'exclude': True}}
        fields = {'director': {'exclude': True}}
        fields = {'numberOfEpisodes': {'exclude': True}}
        fields = {'directors': {'exclude': True}}
        fields = {'quest': {'exclude': True}}
        fields = {'musicBy': {'exclude': True}}
        fields = {'playMode': {'exclude': True}}
        


def create_schema_org_model(type_: Union[VideoGameSeriesProperties, VideoGameSeriesInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VideoGameSeries"
    return model
    

VideoGameSeries = create_schema_org_model()


def create_videogameseries_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_videogameseries_model(model=model)
    return pydantic_type(model).schema_json()


