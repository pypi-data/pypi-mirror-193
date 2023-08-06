"""
A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

https://schema.org/VideoObjectSnapshot
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VideoObjectSnapshotInheritedProperties(TypedDict):
    """A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

    References:
        https://schema.org/VideoObjectSnapshot
    Note:
        Model Depth 5
    Attributes:
        actors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        caption: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        thumbnail: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Thumbnail image for an image or video.
        embeddedTextCaption: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
        director: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        videoFrameSize: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The frame size of the video.
        directors: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        transcript: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
        musicBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The composer of the soundtrack.
        videoQuality: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The quality of the video.
    """

    actors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    actor: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    caption: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    thumbnail: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    embeddedTextCaption: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    director: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    videoFrameSize: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    directors: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    transcript: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    musicBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    videoQuality: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class VideoObjectSnapshotProperties(TypedDict):
    """A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

    References:
        https://schema.org/VideoObjectSnapshot
    Note:
        Model Depth 5
    Attributes:
    """


class VideoObjectSnapshotAllProperties(
    VideoObjectSnapshotInheritedProperties, VideoObjectSnapshotProperties, TypedDict
):
    pass


class VideoObjectSnapshotBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="VideoObjectSnapshot", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"actors": {"exclude": True}}
        fields = {"actor": {"exclude": True}}
        fields = {"caption": {"exclude": True}}
        fields = {"thumbnail": {"exclude": True}}
        fields = {"embeddedTextCaption": {"exclude": True}}
        fields = {"director": {"exclude": True}}
        fields = {"videoFrameSize": {"exclude": True}}
        fields = {"directors": {"exclude": True}}
        fields = {"transcript": {"exclude": True}}
        fields = {"musicBy": {"exclude": True}}
        fields = {"videoQuality": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        VideoObjectSnapshotProperties,
        VideoObjectSnapshotInheritedProperties,
        VideoObjectSnapshotAllProperties,
    ] = VideoObjectSnapshotAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VideoObjectSnapshot"
    return model


VideoObjectSnapshot = create_schema_org_model()


def create_videoobjectsnapshot_model(
    model: Union[
        VideoObjectSnapshotProperties,
        VideoObjectSnapshotInheritedProperties,
        VideoObjectSnapshotAllProperties,
    ]
):
    _type = deepcopy(VideoObjectSnapshotAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of VideoObjectSnapshotAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: VideoObjectSnapshotAllProperties):
    pydantic_type = create_videoobjectsnapshot_model(model=model)
    return pydantic_type(model).schema_json()
