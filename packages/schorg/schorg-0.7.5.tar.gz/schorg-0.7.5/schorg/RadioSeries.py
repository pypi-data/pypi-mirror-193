"""
CreativeWorkSeries dedicated to radio broadcast and associated online delivery.

https://schema.org/RadioSeries
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RadioSeriesInheritedProperties(TypedDict):
    """CreativeWorkSeries dedicated to radio broadcast and associated online delivery.

    References:
        https://schema.org/RadioSeries
    Note:
        Model Depth 4
    Attributes:
        issn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        startDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, SchemaOrgObj, date]], datetime, str, SchemaOrgObj, date]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    issn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, SchemaOrgObj, date]],
            datetime,
            str,
            SchemaOrgObj,
            date,
        ]
    ]


class RadioSeriesProperties(TypedDict):
    """CreativeWorkSeries dedicated to radio broadcast and associated online delivery.

    References:
        https://schema.org/RadioSeries
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        containsSeason: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A season that is part of the media series.
        numberOfSeasons: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of seasons in this series.
        actor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        season: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A season in a media series.
        trailer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The trailer of a movie or TV/radio series, season, episode, etc.
        productionCompany: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        episodes: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An episode of a TV/radio series or season.
        seasons: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A season in a media series.
        episode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An episode of a TV, radio or game media within a series or season.
        director: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        numberOfEpisodes: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of episodes in this season or series.
        directors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        musicBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The composer of the soundtrack.
    """

    actors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    containsSeason: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    numberOfSeasons: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    actor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    season: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    trailer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    productionCompany: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    episodes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    seasons: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    episode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    director: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfEpisodes: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    directors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    musicBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class RadioSeriesAllProperties(
    RadioSeriesInheritedProperties, RadioSeriesProperties, TypedDict
):
    pass


class RadioSeriesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RadioSeries", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"issn": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}
        fields = {"actors": {"exclude": True}}
        fields = {"containsSeason": {"exclude": True}}
        fields = {"numberOfSeasons": {"exclude": True}}
        fields = {"actor": {"exclude": True}}
        fields = {"season": {"exclude": True}}
        fields = {"trailer": {"exclude": True}}
        fields = {"productionCompany": {"exclude": True}}
        fields = {"episodes": {"exclude": True}}
        fields = {"seasons": {"exclude": True}}
        fields = {"episode": {"exclude": True}}
        fields = {"director": {"exclude": True}}
        fields = {"numberOfEpisodes": {"exclude": True}}
        fields = {"directors": {"exclude": True}}
        fields = {"musicBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RadioSeriesProperties, RadioSeriesInheritedProperties, RadioSeriesAllProperties
    ] = RadioSeriesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RadioSeries"
    return model


RadioSeries = create_schema_org_model()


def create_radioseries_model(
    model: Union[
        RadioSeriesProperties, RadioSeriesInheritedProperties, RadioSeriesAllProperties
    ]
):
    _type = deepcopy(RadioSeriesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of RadioSeries. Please see: https://schema.org/RadioSeries"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: RadioSeriesAllProperties):
    pydantic_type = create_radioseries_model(model=model)
    return pydantic_type(model).schema_json()
