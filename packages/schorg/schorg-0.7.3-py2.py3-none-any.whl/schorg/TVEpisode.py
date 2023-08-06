"""
A TV episode which can be part of a series or season.

https://schema.org/TVEpisode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TVEpisodeInheritedProperties(TypedDict):
    """A TV episode which can be part of a series or season.

    References:
        https://schema.org/TVEpisode
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        trailer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The trailer of a movie or TV/radio series, season, episode, etc.
        duration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        productionCompany: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The production company or studio responsible for the item, e.g. series, video game, episode etc.
        partOfSeason: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The season to which this episode belongs.
        partOfSeries: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The series to which this episode or season belongs.
        director: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        directors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        episodeNumber: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Position of the episode within an ordered group of episodes.
        musicBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The composer of the soundtrack.
    """

    actors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    trailer: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    duration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    productionCompany: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    partOfSeason: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    partOfSeries: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    director: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    directors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    episodeNumber: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    musicBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TVEpisodeProperties(TypedDict):
    """A TV episode which can be part of a series or season.

    References:
        https://schema.org/TVEpisode
    Note:
        Model Depth 4
    Attributes:
        partOfTVSeries: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The TV series to which this episode or season belongs.
        titleEIDR: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): An [EIDR](https://eidr.org/) (Entertainment Identifier Registry) [[identifier]] representing at the most general/abstract level, a work of film or television.For example, the motion picture known as "Ghostbusters" has a titleEIDR of  "10.5240/7EC7-228A-510A-053E-CBB8-J". This title (or work) may have several variants, which EIDR calls "edits". See [[editEIDR]].Since schema.org types like [[Movie]] and [[TVEpisode]] can be used for both works and their multiple expressions, it is possible to use [[titleEIDR]] alone (for a general description), or alongside [[editEIDR]] for a more edit-specific description.
        subtitleLanguage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Languages in which subtitles/captions are available, in [IETF BCP 47 standard format](http://tools.ietf.org/html/bcp47).
        countryOfOrigin: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The country of origin of something, including products as well as creative  works such as movie and TV content.In the case of TV and movie, this would be the country of the principle offices of the production company or individual responsible for the movie. For other kinds of [[CreativeWork]] it is difficult to provide fully general guidance, and properties such as [[contentLocation]] and [[locationCreated]] may be more applicable.In the case of products, the country of origin of the product. The exact interpretation of this may vary by context and product type, and cannot be fully enumerated here.
    """

    partOfTVSeries: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    titleEIDR: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    subtitleLanguage: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    countryOfOrigin: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class TVEpisodeAllProperties(
    TVEpisodeInheritedProperties, TVEpisodeProperties, TypedDict
):
    pass


class TVEpisodeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TVEpisode", alias="@id")
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
        fields = {"partOfTVSeries": {"exclude": True}}
        fields = {"titleEIDR": {"exclude": True}}
        fields = {"subtitleLanguage": {"exclude": True}}
        fields = {"countryOfOrigin": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TVEpisodeProperties, TVEpisodeInheritedProperties, TVEpisodeAllProperties
    ] = TVEpisodeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TVEpisode"
    return model


TVEpisode = create_schema_org_model()


def create_tvepisode_model(
    model: Union[
        TVEpisodeProperties, TVEpisodeInheritedProperties, TVEpisodeAllProperties
    ]
):
    _type = deepcopy(TVEpisodeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TVEpisodeAllProperties):
    pydantic_type = create_tvepisode_model(model=model)
    return pydantic_type(model).schema_json()
