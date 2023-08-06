"""
An art gallery.

https://schema.org/ArtGallery
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ArtGalleryInheritedProperties(TypedDict):
    """An art gallery.

    References:
        https://schema.org/ArtGallery
    Note:
        Model Depth 5
    Attributes:
    """


class ArtGalleryProperties(TypedDict):
    """An art gallery.

    References:
        https://schema.org/ArtGallery
    Note:
        Model Depth 5
    Attributes:
    """


class ArtGalleryAllProperties(
    ArtGalleryInheritedProperties, ArtGalleryProperties, TypedDict
):
    pass


class ArtGalleryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ArtGallery", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ArtGalleryProperties, ArtGalleryInheritedProperties, ArtGalleryAllProperties
    ] = ArtGalleryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ArtGallery"
    return model


ArtGallery = create_schema_org_model()


def create_artgallery_model(
    model: Union[
        ArtGalleryProperties, ArtGalleryInheritedProperties, ArtGalleryAllProperties
    ]
):
    _type = deepcopy(ArtGalleryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ArtGalleryAllProperties):
    pydantic_type = create_artgallery_model(model=model)
    return pydantic_type(model).schema_json()
