"""
A specific and exact (byte-for-byte) version of an [[ImageObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata (e.g. XMP, EXIF) the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

https://schema.org/ImageObjectSnapshot
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ImageObjectSnapshotInheritedProperties(TypedDict):
    """A specific and exact (byte-for-byte) version of an [[ImageObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata (e.g. XMP, EXIF) the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

    References:
        https://schema.org/ImageObjectSnapshot
    Note:
        Model Depth 5
    Attributes:
        caption: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        thumbnail: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Thumbnail image for an image or video.
        exifData: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): exif data for this object.
        embeddedTextCaption: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
        representativeOfPage: (Optional[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]): Indicates whether this image is representative of the content of the page.
    """

    caption: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    thumbnail: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    exifData: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    embeddedTextCaption: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    representativeOfPage: NotRequired[
        Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]
    ]


class ImageObjectSnapshotProperties(TypedDict):
    """A specific and exact (byte-for-byte) version of an [[ImageObject]]. Two byte-for-byte identical files, for the purposes of this type, considered identical. If they have different embedded metadata (e.g. XMP, EXIF) the files will differ. Different external facts about the files, e.g. creator or dateCreated that aren't represented in their actual content, do not affect this notion of identity.

    References:
        https://schema.org/ImageObjectSnapshot
    Note:
        Model Depth 5
    Attributes:
    """


class ImageObjectSnapshotAllProperties(
    ImageObjectSnapshotInheritedProperties, ImageObjectSnapshotProperties, TypedDict
):
    pass


class ImageObjectSnapshotBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ImageObjectSnapshot", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"caption": {"exclude": True}}
        fields = {"thumbnail": {"exclude": True}}
        fields = {"exifData": {"exclude": True}}
        fields = {"embeddedTextCaption": {"exclude": True}}
        fields = {"representativeOfPage": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ImageObjectSnapshotProperties,
        ImageObjectSnapshotInheritedProperties,
        ImageObjectSnapshotAllProperties,
    ] = ImageObjectSnapshotAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ImageObjectSnapshot"
    return model


ImageObjectSnapshot = create_schema_org_model()


def create_imageobjectsnapshot_model(
    model: Union[
        ImageObjectSnapshotProperties,
        ImageObjectSnapshotInheritedProperties,
        ImageObjectSnapshotAllProperties,
    ]
):
    _type = deepcopy(ImageObjectSnapshotAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ImageObjectSnapshotAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ImageObjectSnapshotAllProperties):
    pydantic_type = create_imageobjectsnapshot_model(model=model)
    return pydantic_type(model).schema_json()
