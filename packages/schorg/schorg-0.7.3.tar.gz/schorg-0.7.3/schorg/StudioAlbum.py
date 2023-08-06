"""
StudioAlbum.

https://schema.org/StudioAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class StudioAlbumInheritedProperties(TypedDict):
    """StudioAlbum.

    References:
        https://schema.org/StudioAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class StudioAlbumProperties(TypedDict):
    """StudioAlbum.

    References:
        https://schema.org/StudioAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class StudioAlbumAllProperties(
    StudioAlbumInheritedProperties, StudioAlbumProperties, TypedDict
):
    pass


class StudioAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="StudioAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        StudioAlbumProperties, StudioAlbumInheritedProperties, StudioAlbumAllProperties
    ] = StudioAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "StudioAlbum"
    return model


StudioAlbum = create_schema_org_model()


def create_studioalbum_model(
    model: Union[
        StudioAlbumProperties, StudioAlbumInheritedProperties, StudioAlbumAllProperties
    ]
):
    _type = deepcopy(StudioAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: StudioAlbumAllProperties):
    pydantic_type = create_studioalbum_model(model=model)
    return pydantic_type(model).schema_json()
