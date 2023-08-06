"""
A series of movies. Included movies can be indicated with the hasPart property.

https://schema.org/MovieSeries
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MovieSeriesInheritedProperties(TypedDict):
    """A series of movies. Included movies can be indicated with the hasPart property.

    References:
        https://schema.org/MovieSeries
    Note:
        Model Depth 4
    Attributes:
        issn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The International Standard Serial Number (ISSN) that identifies this serial publication. You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L) for, this serial publication.
        startDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The start date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
        endDate: (Optional[Union[List[Union[datetime, str, date, SchemaOrgObj]], datetime, str, date, SchemaOrgObj]]): The end date and time of the item (in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601)).
    """

    issn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]
    endDate: NotRequired[
        Union[
            List[Union[datetime, str, date, SchemaOrgObj]],
            datetime,
            str,
            date,
            SchemaOrgObj,
        ]
    ]


class MovieSeriesProperties(TypedDict):
    """A series of movies. Included movies can be indicated with the hasPart property.

    References:
        https://schema.org/MovieSeries
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        trailer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The trailer of a movie or TV/radio series, season, episode, etc.
        productionCompany: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        director: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        directors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        musicBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The composer of the soundtrack.
    """

    actors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    trailer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    productionCompany: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    director: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    directors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    musicBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MovieSeriesAllProperties(
    MovieSeriesInheritedProperties, MovieSeriesProperties, TypedDict
):
    pass


class MovieSeriesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MovieSeries", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"issn": {"exclude": True}}
        fields = {"startDate": {"exclude": True}}
        fields = {"endDate": {"exclude": True}}
        fields = {"actors": {"exclude": True}}
        fields = {"actor": {"exclude": True}}
        fields = {"trailer": {"exclude": True}}
        fields = {"productionCompany": {"exclude": True}}
        fields = {"director": {"exclude": True}}
        fields = {"directors": {"exclude": True}}
        fields = {"musicBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MovieSeriesProperties, MovieSeriesInheritedProperties, MovieSeriesAllProperties
    ] = MovieSeriesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MovieSeries"
    return model


MovieSeries = create_schema_org_model()


def create_movieseries_model(
    model: Union[
        MovieSeriesProperties, MovieSeriesInheritedProperties, MovieSeriesAllProperties
    ]
):
    _type = deepcopy(MovieSeriesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MovieSeriesAllProperties):
    pydantic_type = create_movieseries_model(model=model)
    return pydantic_type(model).schema_json()
