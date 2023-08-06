"""
DJMixAlbum.

https://schema.org/DJMixAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DJMixAlbumInheritedProperties(TypedDict):
    """DJMixAlbum.

    References:
        https://schema.org/DJMixAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class DJMixAlbumProperties(TypedDict):
    """DJMixAlbum.

    References:
        https://schema.org/DJMixAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class DJMixAlbumAllProperties(
    DJMixAlbumInheritedProperties, DJMixAlbumProperties, TypedDict
):
    pass


class DJMixAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DJMixAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DJMixAlbumProperties, DJMixAlbumInheritedProperties, DJMixAlbumAllProperties
    ] = DJMixAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DJMixAlbum"
    return model


DJMixAlbum = create_schema_org_model()


def create_djmixalbum_model(
    model: Union[
        DJMixAlbumProperties, DJMixAlbumInheritedProperties, DJMixAlbumAllProperties
    ]
):
    _type = deepcopy(DJMixAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DJMixAlbumAllProperties):
    pydantic_type = create_djmixalbum_model(model=model)
    return pydantic_type(model).schema_json()
