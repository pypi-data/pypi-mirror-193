"""
Content coded 'transformed content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'transformed content':  or all of the video has been manipulated to transform the footage itself. This category includes using tools like the Adobe Suite to change the speed of the video, add or remove visual elements or dub audio. Deepfakes are also a subset of transformation.For an [[ImageObject]] to be 'transformed content': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.For an [[ImageObject]] with embedded text to be 'transformed content': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.For an [[AudioObject]] to be 'transformed content': Part or all of the audio has been manipulated to alter the words or sounds, or the audio has been synthetically generated, such as to create a sound-alike voice.

https://schema.org/TransformedContent
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TransformedContentInheritedProperties(TypedDict):
    """Content coded 'transformed content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'transformed content':  or all of the video has been manipulated to transform the footage itself. This category includes using tools like the Adobe Suite to change the speed of the video, add or remove visual elements or dub audio. Deepfakes are also a subset of transformation.For an [[ImageObject]] to be 'transformed content': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.For an [[ImageObject]] with embedded text to be 'transformed content': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.For an [[AudioObject]] to be 'transformed content': Part or all of the audio has been manipulated to alter the words or sounds, or the audio has been synthetically generated, such as to create a sound-alike voice.

    References:
        https://schema.org/TransformedContent
    Note:
        Model Depth 5
    Attributes:
    """


class TransformedContentProperties(TypedDict):
    """Content coded 'transformed content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'transformed content':  or all of the video has been manipulated to transform the footage itself. This category includes using tools like the Adobe Suite to change the speed of the video, add or remove visual elements or dub audio. Deepfakes are also a subset of transformation.For an [[ImageObject]] to be 'transformed content': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.For an [[ImageObject]] with embedded text to be 'transformed content': Adding or deleting visual elements to give the image a different meaning with the intention to mislead.For an [[AudioObject]] to be 'transformed content': Part or all of the audio has been manipulated to alter the words or sounds, or the audio has been synthetically generated, such as to create a sound-alike voice.

    References:
        https://schema.org/TransformedContent
    Note:
        Model Depth 5
    Attributes:
    """


class TransformedContentAllProperties(
    TransformedContentInheritedProperties, TransformedContentProperties, TypedDict
):
    pass


class TransformedContentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="TransformedContent", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        TransformedContentProperties,
        TransformedContentInheritedProperties,
        TransformedContentAllProperties,
    ] = TransformedContentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TransformedContent"
    return model


TransformedContent = create_schema_org_model()


def create_transformedcontent_model(
    model: Union[
        TransformedContentProperties,
        TransformedContentInheritedProperties,
        TransformedContentAllProperties,
    ]
):
    _type = deepcopy(TransformedContentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of TransformedContent. Please see: https://schema.org/TransformedContent"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: TransformedContentAllProperties):
    pydantic_type = create_transformedcontent_model(model=model)
    return pydantic_type(model).schema_json()
