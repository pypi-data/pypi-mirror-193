"""
Content coded 'edited or cropped content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'edited or cropped content': The video has been edited or rearranged. This category applies to time edits, including editing multiple videos together to alter the story being told or editing out large portions from a video.For an [[ImageObject]] to be 'edited or cropped content': Presenting a part of an image from a larger whole to mislead the viewer.For an [[ImageObject]] with embedded text to be 'edited or cropped content': Presenting a part of an image from a larger whole to mislead the viewer.For an [[AudioObject]] to be 'edited or cropped content': The audio has been edited or rearranged. This category applies to time edits, including editing multiple audio clips together to alter the story being told or editing out large portions from the recording.

https://schema.org/EditedOrCroppedContent
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EditedOrCroppedContentInheritedProperties(TypedDict):
    """Content coded 'edited or cropped content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'edited or cropped content': The video has been edited or rearranged. This category applies to time edits, including editing multiple videos together to alter the story being told or editing out large portions from a video.For an [[ImageObject]] to be 'edited or cropped content': Presenting a part of an image from a larger whole to mislead the viewer.For an [[ImageObject]] with embedded text to be 'edited or cropped content': Presenting a part of an image from a larger whole to mislead the viewer.For an [[AudioObject]] to be 'edited or cropped content': The audio has been edited or rearranged. This category applies to time edits, including editing multiple audio clips together to alter the story being told or editing out large portions from the recording.

    References:
        https://schema.org/EditedOrCroppedContent
    Note:
        Model Depth 5
    Attributes:
    """


class EditedOrCroppedContentProperties(TypedDict):
    """Content coded 'edited or cropped content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'edited or cropped content': The video has been edited or rearranged. This category applies to time edits, including editing multiple videos together to alter the story being told or editing out large portions from a video.For an [[ImageObject]] to be 'edited or cropped content': Presenting a part of an image from a larger whole to mislead the viewer.For an [[ImageObject]] with embedded text to be 'edited or cropped content': Presenting a part of an image from a larger whole to mislead the viewer.For an [[AudioObject]] to be 'edited or cropped content': The audio has been edited or rearranged. This category applies to time edits, including editing multiple audio clips together to alter the story being told or editing out large portions from the recording.

    References:
        https://schema.org/EditedOrCroppedContent
    Note:
        Model Depth 5
    Attributes:
    """


class EditedOrCroppedContentAllProperties(
    EditedOrCroppedContentInheritedProperties,
    EditedOrCroppedContentProperties,
    TypedDict,
):
    pass


class EditedOrCroppedContentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EditedOrCroppedContent", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EditedOrCroppedContentProperties,
        EditedOrCroppedContentInheritedProperties,
        EditedOrCroppedContentAllProperties,
    ] = EditedOrCroppedContentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EditedOrCroppedContent"
    return model


EditedOrCroppedContent = create_schema_org_model()


def create_editedorcroppedcontent_model(
    model: Union[
        EditedOrCroppedContentProperties,
        EditedOrCroppedContentInheritedProperties,
        EditedOrCroppedContentAllProperties,
    ]
):
    _type = deepcopy(EditedOrCroppedContentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EditedOrCroppedContent. Please see: https://schema.org/EditedOrCroppedContent"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EditedOrCroppedContentAllProperties):
    pydantic_type = create_editedorcroppedcontent_model(model=model)
    return pydantic_type(model).schema_json()
