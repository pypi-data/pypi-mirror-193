"""
SoundtrackAlbum.

https://schema.org/SoundtrackAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SoundtrackAlbumInheritedProperties(TypedDict):
    """SoundtrackAlbum.

    References:
        https://schema.org/SoundtrackAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class SoundtrackAlbumProperties(TypedDict):
    """SoundtrackAlbum.

    References:
        https://schema.org/SoundtrackAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class SoundtrackAlbumAllProperties(
    SoundtrackAlbumInheritedProperties, SoundtrackAlbumProperties, TypedDict
):
    pass


class SoundtrackAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SoundtrackAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SoundtrackAlbumProperties,
        SoundtrackAlbumInheritedProperties,
        SoundtrackAlbumAllProperties,
    ] = SoundtrackAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SoundtrackAlbum"
    return model


SoundtrackAlbum = create_schema_org_model()


def create_soundtrackalbum_model(
    model: Union[
        SoundtrackAlbumProperties,
        SoundtrackAlbumInheritedProperties,
        SoundtrackAlbumAllProperties,
    ]
):
    _type = deepcopy(SoundtrackAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SoundtrackAlbum. Please see: https://schema.org/SoundtrackAlbum"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SoundtrackAlbumAllProperties):
    pydantic_type = create_soundtrackalbum_model(model=model)
    return pydantic_type(model).schema_json()
