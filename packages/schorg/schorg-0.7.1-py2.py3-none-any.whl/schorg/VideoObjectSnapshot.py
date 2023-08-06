"""
A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

https://schema.org/VideoObjectSnapshot
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VideoObjectSnapshotInheritedProperties(TypedDict):
    """A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

    References:
        https://schema.org/VideoObjectSnapshot
    Note:
        Model Depth 5
    Attributes:
        actors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip.
        actor: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An actor, e.g. in TV, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.
        caption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        thumbnail: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Thumbnail image for an image or video.
        embeddedTextCaption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
        director: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.
        videoFrameSize: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The frame size of the video.
        directors: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A director of e.g. TV, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip.
        transcript: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
        musicBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The composer of the soundtrack.
        videoQuality: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The quality of the video.
    """

    actors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    actor: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    caption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    thumbnail: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    embeddedTextCaption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    director: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    videoFrameSize: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    directors: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    transcript: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    musicBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    videoQuality: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class VideoObjectSnapshotProperties(TypedDict):
    """A specific and exact (byte-for-byte) version of a [[VideoObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

    References:
        https://schema.org/VideoObjectSnapshot
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(VideoObjectSnapshotInheritedProperties , VideoObjectSnapshotProperties, TypedDict):
    pass


class VideoObjectSnapshotBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VideoObjectSnapshot",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'actors': {'exclude': True}}
        fields = {'actor': {'exclude': True}}
        fields = {'caption': {'exclude': True}}
        fields = {'thumbnail': {'exclude': True}}
        fields = {'embeddedTextCaption': {'exclude': True}}
        fields = {'director': {'exclude': True}}
        fields = {'videoFrameSize': {'exclude': True}}
        fields = {'directors': {'exclude': True}}
        fields = {'transcript': {'exclude': True}}
        fields = {'musicBy': {'exclude': True}}
        fields = {'videoQuality': {'exclude': True}}
        


def create_schema_org_model(type_: Union[VideoObjectSnapshotProperties, VideoObjectSnapshotInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VideoObjectSnapshot"
    return model
    

VideoObjectSnapshot = create_schema_org_model()


def create_videoobjectsnapshot_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_videoobjectsnapshot_model(model=model)
    return pydantic_type(model).schema_json()


