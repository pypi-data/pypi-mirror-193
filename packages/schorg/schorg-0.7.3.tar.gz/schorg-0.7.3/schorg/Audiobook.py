"""
An audiobook.

https://schema.org/Audiobook
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AudiobookInheritedProperties(TypedDict):
    """An audiobook.

    References:
        https://schema.org/Audiobook
    Note:
        Model Depth 4
    Attributes:
        caption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The caption for this object. For downloadable machine formats (closed caption, subtitles etc.) use MediaObject and indicate the [[encodingFormat]].
        embeddedTextCaption: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Represents textual captioning from a [[MediaObject]], e.g. text of a 'meme'.
        transcript: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If this MediaObject is an AudioObject or VideoObject, the transcript of that object.
        abridged: (Optional[Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]]): Indicates whether the book is an abridged edition.
        bookFormat: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The format of the book.
        illustrator: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The illustrator of the book.
        bookEdition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The edition of the book.
        numberOfPages: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of pages in the book.
        isbn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The ISBN of the book.
    """

    caption: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    embeddedTextCaption: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    transcript: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    abridged: NotRequired[
        Union[List[Union[str, StrictBool, SchemaOrgObj]], str, StrictBool, SchemaOrgObj]
    ]
    bookFormat: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    illustrator: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    bookEdition: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfPages: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    isbn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class AudiobookProperties(TypedDict):
    """An audiobook.

    References:
        https://schema.org/Audiobook
    Note:
        Model Depth 4
    Attributes:
        duration: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The duration of the item (movie, audio recording, event, etc.) in [ISO 8601 date format](http://en.wikipedia.org/wiki/ISO_8601).
        readBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A person who reads (performs) the audiobook.
    """

    duration: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    readBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class AudiobookAllProperties(
    AudiobookInheritedProperties, AudiobookProperties, TypedDict
):
    pass


class AudiobookBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Audiobook", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"caption": {"exclude": True}}
        fields = {"embeddedTextCaption": {"exclude": True}}
        fields = {"transcript": {"exclude": True}}
        fields = {"abridged": {"exclude": True}}
        fields = {"bookFormat": {"exclude": True}}
        fields = {"illustrator": {"exclude": True}}
        fields = {"bookEdition": {"exclude": True}}
        fields = {"numberOfPages": {"exclude": True}}
        fields = {"isbn": {"exclude": True}}
        fields = {"duration": {"exclude": True}}
        fields = {"readBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        AudiobookProperties, AudiobookInheritedProperties, AudiobookAllProperties
    ] = AudiobookAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Audiobook"
    return model


Audiobook = create_schema_org_model()


def create_audiobook_model(
    model: Union[
        AudiobookProperties, AudiobookInheritedProperties, AudiobookAllProperties
    ]
):
    _type = deepcopy(AudiobookAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AudiobookAllProperties):
    pydantic_type = create_audiobook_model(model=model)
    return pydantic_type(model).schema_json()
