"""
LiveAlbum.

https://schema.org/LiveAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LiveAlbumInheritedProperties(TypedDict):
    """LiveAlbum.

    References:
        https://schema.org/LiveAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class LiveAlbumProperties(TypedDict):
    """LiveAlbum.

    References:
        https://schema.org/LiveAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class LiveAlbumAllProperties(
    LiveAlbumInheritedProperties, LiveAlbumProperties, TypedDict
):
    pass


class LiveAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LiveAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LiveAlbumProperties, LiveAlbumInheritedProperties, LiveAlbumAllProperties
    ] = LiveAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LiveAlbum"
    return model


LiveAlbum = create_schema_org_model()


def create_livealbum_model(
    model: Union[
        LiveAlbumProperties, LiveAlbumInheritedProperties, LiveAlbumAllProperties
    ]
):
    _type = deepcopy(LiveAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LiveAlbum. Please see: https://schema.org/LiveAlbum"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LiveAlbumAllProperties):
    pydantic_type = create_livealbum_model(model=model)
    return pydantic_type(model).schema_json()
