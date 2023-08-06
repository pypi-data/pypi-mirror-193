"""
Content coded 'as original media content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'original': No evidence the footage has been misleadingly altered or manipulated, though it may contain false or misleading claims.For an [[ImageObject]] to be 'original': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.For an [[ImageObject]] with embedded text to be 'original': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.For an [[AudioObject]] to be 'original': No evidence the audio has been misleadingly altered or manipulated, though it may contain false or misleading claims.

https://schema.org/OriginalMediaContent
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OriginalMediaContentInheritedProperties(TypedDict):
    """Content coded 'as original media content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'original': No evidence the footage has been misleadingly altered or manipulated, though it may contain false or misleading claims.For an [[ImageObject]] to be 'original': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.For an [[ImageObject]] with embedded text to be 'original': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.For an [[AudioObject]] to be 'original': No evidence the audio has been misleadingly altered or manipulated, though it may contain false or misleading claims.

    References:
        https://schema.org/OriginalMediaContent
    Note:
        Model Depth 5
    Attributes:
    """


class OriginalMediaContentProperties(TypedDict):
    """Content coded 'as original media content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'original': No evidence the footage has been misleadingly altered or manipulated, though it may contain false or misleading claims.For an [[ImageObject]] to be 'original': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.For an [[ImageObject]] with embedded text to be 'original': No evidence the image has been misleadingly altered or manipulated, though it may still contain false or misleading claims.For an [[AudioObject]] to be 'original': No evidence the audio has been misleadingly altered or manipulated, though it may contain false or misleading claims.

    References:
        https://schema.org/OriginalMediaContent
    Note:
        Model Depth 5
    Attributes:
    """


class OriginalMediaContentAllProperties(
    OriginalMediaContentInheritedProperties, OriginalMediaContentProperties, TypedDict
):
    pass


class OriginalMediaContentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OriginalMediaContent", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OriginalMediaContentProperties,
        OriginalMediaContentInheritedProperties,
        OriginalMediaContentAllProperties,
    ] = OriginalMediaContentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OriginalMediaContent"
    return model


OriginalMediaContent = create_schema_org_model()


def create_originalmediacontent_model(
    model: Union[
        OriginalMediaContentProperties,
        OriginalMediaContentInheritedProperties,
        OriginalMediaContentAllProperties,
    ]
):
    _type = deepcopy(OriginalMediaContentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OriginalMediaContentAllProperties):
    pydantic_type = create_originalmediacontent_model(model=model)
    return pydantic_type(model).schema_json()
