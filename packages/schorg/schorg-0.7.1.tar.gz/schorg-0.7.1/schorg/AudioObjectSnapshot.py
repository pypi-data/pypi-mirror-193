"""
A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

https://schema.org/AudioObjectSnapshot
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AudioObjectSnapshotInheritedProperties(TypedDict):
    """A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

    References:
        https://schema.org/AudioObjectSnapshot
    Note:
        Model Depth 5
    Attributes:
        caption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        embeddedTextCaption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
        transcript: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
    """

    caption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    embeddedTextCaption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    transcript: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AudioObjectSnapshotProperties(TypedDict):
    """A specific and exact (byte-for-byte) version of an [[AudioObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

    References:
        https://schema.org/AudioObjectSnapshot
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AudioObjectSnapshotInheritedProperties , AudioObjectSnapshotProperties, TypedDict):
    pass


class AudioObjectSnapshotBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AudioObjectSnapshot",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'caption': {'exclude': True}}
        fields = {'embeddedTextCaption': {'exclude': True}}
        fields = {'transcript': {'exclude': True}}
        


def create_schema_org_model(type_: Union[AudioObjectSnapshotProperties, AudioObjectSnapshotInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AudioObjectSnapshot"
    return model
    

AudioObjectSnapshot = create_schema_org_model()


def create_audioobjectsnapshot_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_audioobjectsnapshot_model(model=model)
    return pydantic_type(model).schema_json()


