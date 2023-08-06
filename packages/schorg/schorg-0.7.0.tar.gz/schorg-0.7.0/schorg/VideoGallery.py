"""
Web page type: Video gallery page.

https://schema.org/VideoGallery
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VideoGalleryInheritedProperties(TypedDict):
    """Web page type: Video gallery page.

    References:
        https://schema.org/VideoGallery
    Note:
        Model Depth 6
    Attributes:
    """

    


class VideoGalleryProperties(TypedDict):
    """Web page type: Video gallery page.

    References:
        https://schema.org/VideoGallery
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(VideoGalleryInheritedProperties , VideoGalleryProperties, TypedDict):
    pass


class VideoGalleryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="VideoGallery",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[VideoGalleryProperties, VideoGalleryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VideoGallery"
    return model
    

VideoGallery = create_schema_org_model()


def create_videogallery_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_videogallery_model(model=model)
    return pydantic_type(model).schema_json()


