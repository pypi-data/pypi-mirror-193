"""
A short TV program or a segment/part of a TV program.

https://schema.org/TVClip
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TVClipInheritedProperties(TypedDict):
    """A short TV program or a segment/part of a TV program.

    References:
        https://schema.org/TVClip
    Note:
        Model Depth 4
    Attributes:
        actors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        clipNumber: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): Position of the clip within an ordered group of clips.
        partOfEpisode: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The episode to which this clip belongs.
        partOfSeason: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The season to which this episode belongs.
        startOffset: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The start time of the clip expressed as the number of seconds from the beginning of the work.
        partOfSeries: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The series to which this episode or season belongs.
        endOffset: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The end time of the clip expressed as the number of seconds from the beginning of the work.
        director: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        directors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        musicBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The composer of the soundtrack.
    """

    actors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    clipNumber: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    partOfEpisode: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    partOfSeason: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    startOffset: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    partOfSeries: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    endOffset: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    director: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    directors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    musicBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class TVClipProperties(TypedDict):
    """A short TV program or a segment/part of a TV program.

    References:
        https://schema.org/TVClip
    Note:
        Model Depth 4
    Attributes:
        partOfTVSeries: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The TV series to which this episode or season belongs.
    """

    partOfTVSeries: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class TVClipAllProperties(TVClipInheritedProperties, TVClipProperties, TypedDict):
    pass


class TVClipBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TVClip", alias="@id")
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
        fields = {"partOfTVSeries": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TVClipProperties, TVClipInheritedProperties, TVClipAllProperties
    ] = TVClipAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TVClip"
    return model


TVClip = create_schema_org_model()


def create_tvclip_model(
    model: Union[TVClipProperties, TVClipInheritedProperties, TVClipAllProperties]
):
    _type = deepcopy(TVClipAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of TVClipAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TVClipAllProperties):
    pydantic_type = create_tvclip_model(model=model)
    return pydantic_type(model).schema_json()
