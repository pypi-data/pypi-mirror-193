"""
A radio episode which can be part of a series or season.

https://schema.org/RadioEpisode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RadioEpisodeInheritedProperties(TypedDict):
    """A radio episode which can be part of a series or season.

    References:
        https://schema.org/RadioEpisode
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        trailer: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The trailer of a movie or TV/radio series, season, episode, etc.
        duration: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        productionCompany: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        partOfSeason: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The season to which this episode belongs.
        partOfSeries: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The series to which this episode or season belongs.
        director: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        directors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        episodeNumber: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Position of the episode within an ordered group of episodes.
        musicBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The composer of the soundtrack.
    """

    actors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    trailer: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    duration: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    productionCompany: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    partOfSeason: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    partOfSeries: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    director: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    directors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    episodeNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    musicBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class RadioEpisodeProperties(TypedDict):
    """A radio episode which can be part of a series or season.

    References:
        https://schema.org/RadioEpisode
    Note:
        Model Depth 4
    Attributes:
    """


class RadioEpisodeAllProperties(
    RadioEpisodeInheritedProperties, RadioEpisodeProperties, TypedDict
):
    pass


class RadioEpisodeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RadioEpisode", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actors": {"exclude": True}}
        fields = {"actor": {"exclude": True}}
        fields = {"trailer": {"exclude": True}}
        fields = {"duration": {"exclude": True}}
        fields = {"productionCompany": {"exclude": True}}
        fields = {"partOfSeason": {"exclude": True}}
        fields = {"partOfSeries": {"exclude": True}}
        fields = {"director": {"exclude": True}}
        fields = {"directors": {"exclude": True}}
        fields = {"episodeNumber": {"exclude": True}}
        fields = {"musicBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RadioEpisodeProperties,
        RadioEpisodeInheritedProperties,
        RadioEpisodeAllProperties,
    ] = RadioEpisodeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RadioEpisode"
    return model


RadioEpisode = create_schema_org_model()


def create_radioepisode_model(
    model: Union[
        RadioEpisodeProperties,
        RadioEpisodeInheritedProperties,
        RadioEpisodeAllProperties,
    ]
):
    _type = deepcopy(RadioEpisodeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RadioEpisodeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RadioEpisodeAllProperties):
    pydantic_type = create_radioepisode_model(model=model)
    return pydantic_type(model).schema_json()
