"""
An image of a visual machine-readable code such as a barcode or QR code.

https://schema.org/Barcode
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BarcodeInheritedProperties(TypedDict):
    """An image of a visual machine-readable code such as a barcode or QR code.

    References:
        https://schema.org/Barcode
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
    embeddedTextCaption: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    representativeOfPage: NotRequired[Union[List[Union[SchemaOrgObj, str, StrictBool]], SchemaOrgObj, str, StrictBool]]
    


class BarcodeProperties(TypedDict):
    """An image of a visual machine-readable code such as a barcode or QR code.

    References:
        https://schema.org/Barcode
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(BarcodeInheritedProperties , BarcodeProperties, TypedDict):
    pass


class BarcodeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Barcode",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'caption': {'exclude': True}}
        fields = {'thumbnail': {'exclude': True}}
        fields = {'exifData': {'exclude': True}}
        fields = {'embeddedTextCaption': {'exclude': True}}
        fields = {'representativeOfPage': {'exclude': True}}
        


def create_schema_org_model(type_: Union[BarcodeProperties, BarcodeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Barcode"
    return model
    

Barcode = create_schema_org_model()


def create_barcode_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_barcode_model(model=model)
    return pydantic_type(model).schema_json()


