"""
AlbumRelease.

https://schema.org/AlbumRelease
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AlbumReleaseInheritedProperties(TypedDict):
    """AlbumRelease.

    References:
        https://schema.org/AlbumRelease
    Note:
        Model Depth 5
    Attributes:
    """


class AlbumReleaseProperties(TypedDict):
    """AlbumRelease.

    References:
        https://schema.org/AlbumRelease
    Note:
        Model Depth 5
    Attributes:
    """


class AlbumReleaseAllProperties(
    AlbumReleaseInheritedProperties, AlbumReleaseProperties, TypedDict
):
    pass


class AlbumReleaseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AlbumRelease", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AlbumReleaseProperties,
        AlbumReleaseInheritedProperties,
        AlbumReleaseAllProperties,
    ] = AlbumReleaseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AlbumRelease"
    return model


AlbumRelease = create_schema_org_model()


def create_albumrelease_model(
    model: Union[
        AlbumReleaseProperties,
        AlbumReleaseInheritedProperties,
        AlbumReleaseAllProperties,
    ]
):
    _type = deepcopy(AlbumReleaseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of AlbumReleaseAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AlbumReleaseAllProperties):
    pydantic_type = create_albumrelease_model(model=model)
    return pydantic_type(model).schema_json()
