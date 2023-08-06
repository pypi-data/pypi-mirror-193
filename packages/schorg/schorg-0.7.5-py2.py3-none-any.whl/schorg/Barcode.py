"""
An image of a visual machine-readable code such as a barcode or QR code.

https://schema.org/Barcode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BarcodeInheritedProperties(TypedDict):
    """An image of a visual machine-readable code such as a barcode or QR code.

    References:
        https://schema.org/Barcode
    Note:
        Model Depth 5
    Attributes:
        caption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        thumbnail: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Thumbnail image for an image or video.
        exifData: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): exif data for this object.
        embeddedTextCaption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
        representativeOfPage: (Optional[Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]]): Indicates whether this image is representative of the content of the page.
    """

    caption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    thumbnail: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    exifData: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    embeddedTextCaption: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    representativeOfPage: NotRequired[
        Union[List[Union[StrictBool, SchemaOrgObj, str]], StrictBool, SchemaOrgObj, str]
    ]


class BarcodeProperties(TypedDict):
    """An image of a visual machine-readable code such as a barcode or QR code.

    References:
        https://schema.org/Barcode
    Note:
        Model Depth 5
    Attributes:
    """


class BarcodeAllProperties(BarcodeInheritedProperties, BarcodeProperties, TypedDict):
    pass


class BarcodeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Barcode", alias="@id")
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
        BarcodeProperties, BarcodeInheritedProperties, BarcodeAllProperties
    ] = BarcodeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Barcode"
    return model


Barcode = create_schema_org_model()


def create_barcode_model(
    model: Union[BarcodeProperties, BarcodeInheritedProperties, BarcodeAllProperties]
):
    _type = deepcopy(BarcodeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Barcode. Please see: https://schema.org/Barcode"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BarcodeAllProperties):
    pydantic_type = create_barcode_model(model=model)
    return pydantic_type(model).schema_json()
