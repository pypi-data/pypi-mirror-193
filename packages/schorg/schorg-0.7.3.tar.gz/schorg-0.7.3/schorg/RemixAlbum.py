"""
RemixAlbum.

https://schema.org/RemixAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RemixAlbumInheritedProperties(TypedDict):
    """RemixAlbum.

    References:
        https://schema.org/RemixAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class RemixAlbumProperties(TypedDict):
    """RemixAlbum.

    References:
        https://schema.org/RemixAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class RemixAlbumAllProperties(
    RemixAlbumInheritedProperties, RemixAlbumProperties, TypedDict
):
    pass


class RemixAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RemixAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RemixAlbumProperties, RemixAlbumInheritedProperties, RemixAlbumAllProperties
    ] = RemixAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RemixAlbum"
    return model


RemixAlbum = create_schema_org_model()


def create_remixalbum_model(
    model: Union[
        RemixAlbumProperties, RemixAlbumInheritedProperties, RemixAlbumAllProperties
    ]
):
    _type = deepcopy(RemixAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RemixAlbumAllProperties):
    pydantic_type = create_remixalbum_model(model=model)
    return pydantic_type(model).schema_json()
