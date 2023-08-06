"""
SpokenWordAlbum.

https://schema.org/SpokenWordAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SpokenWordAlbumInheritedProperties(TypedDict):
    """SpokenWordAlbum.

    References:
        https://schema.org/SpokenWordAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class SpokenWordAlbumProperties(TypedDict):
    """SpokenWordAlbum.

    References:
        https://schema.org/SpokenWordAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class SpokenWordAlbumAllProperties(
    SpokenWordAlbumInheritedProperties, SpokenWordAlbumProperties, TypedDict
):
    pass


class SpokenWordAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SpokenWordAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SpokenWordAlbumProperties,
        SpokenWordAlbumInheritedProperties,
        SpokenWordAlbumAllProperties,
    ] = SpokenWordAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SpokenWordAlbum"
    return model


SpokenWordAlbum = create_schema_org_model()


def create_spokenwordalbum_model(
    model: Union[
        SpokenWordAlbumProperties,
        SpokenWordAlbumInheritedProperties,
        SpokenWordAlbumAllProperties,
    ]
):
    _type = deepcopy(SpokenWordAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SpokenWordAlbum. Please see: https://schema.org/SpokenWordAlbum"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SpokenWordAlbumAllProperties):
    pydantic_type = create_spokenwordalbum_model(model=model)
    return pydantic_type(model).schema_json()
