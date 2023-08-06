"""
A short segment/part of a movie.

https://schema.org/MovieClip
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MovieClipInheritedProperties(TypedDict):
    """A short segment/part of a movie.

    References:
        https://schema.org/MovieClip
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        clipNumber: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Position of the clip within an ordered group of clips.
        partOfEpisode: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The episode to which this clip belongs.
        partOfSeason: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The season to which this episode belongs.
        startOffset: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The start time of the clip expressed as the number of seconds from the beginning of the work.
        partOfSeries: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The series to which this episode or season belongs.
        endOffset: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The end time of the clip expressed as the number of seconds from the beginning of the work.
        director: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        directors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        musicBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The composer of the soundtrack.
    """

    actors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    clipNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    partOfEpisode: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    partOfSeason: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    startOffset: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    partOfSeries: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    endOffset: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    director: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    directors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    musicBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class MovieClipProperties(TypedDict):
    """A short segment/part of a movie.

    References:
        https://schema.org/MovieClip
    Note:
        Model Depth 4
    Attributes:
    """


class MovieClipAllProperties(
    MovieClipInheritedProperties, MovieClipProperties, TypedDict
):
    pass


class MovieClipBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MovieClip", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actors": {"exclude": True}}
        fields = {"actor": {"exclude": True}}
        fields = {"clipNumber": {"exclude": True}}
        fields = {"partOfEpisode": {"exclude": True}}
        fields = {"partOfSeason": {"exclude": True}}
        fields = {"startOffset": {"exclude": True}}
        fields = {"partOfSeries": {"exclude": True}}
        fields = {"endOffset": {"exclude": True}}
        fields = {"director": {"exclude": True}}
        fields = {"directors": {"exclude": True}}
        fields = {"musicBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MovieClipProperties, MovieClipInheritedProperties, MovieClipAllProperties
    ] = MovieClipAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MovieClip"
    return model


MovieClip = create_schema_org_model()


def create_movieclip_model(
    model: Union[
        MovieClipProperties, MovieClipInheritedProperties, MovieClipAllProperties
    ]
):
    _type = deepcopy(MovieClipAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MovieClip. Please see: https://schema.org/MovieClip"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MovieClipAllProperties):
    pydantic_type = create_movieclip_model(model=model)
    return pydantic_type(model).schema_json()
