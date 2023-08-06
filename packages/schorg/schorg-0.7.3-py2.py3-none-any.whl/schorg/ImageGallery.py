"""
Web page type: Image gallery page.

https://schema.org/ImageGallery
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ImageGalleryInheritedProperties(TypedDict):
    """Web page type: Image gallery page.

    References:
        https://schema.org/ImageGallery
    Note:
        Model Depth 6
    Attributes:
    """


class ImageGalleryProperties(TypedDict):
    """Web page type: Image gallery page.

    References:
        https://schema.org/ImageGallery
    Note:
        Model Depth 6
    Attributes:
    """


class ImageGalleryAllProperties(
    ImageGalleryInheritedProperties, ImageGalleryProperties, TypedDict
):
    pass


class ImageGalleryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ImageGallery", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ImageGalleryProperties,
        ImageGalleryInheritedProperties,
        ImageGalleryAllProperties,
    ] = ImageGalleryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ImageGallery"
    return model


ImageGallery = create_schema_org_model()


def create_imagegallery_model(
    model: Union[
        ImageGalleryProperties,
        ImageGalleryInheritedProperties,
        ImageGalleryAllProperties,
    ]
):
    _type = deepcopy(ImageGalleryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ImageGalleryAllProperties):
    pydantic_type = create_imagegallery_model(model=model)
    return pydantic_type(model).schema_json()
