"""
DemoAlbum.

https://schema.org/DemoAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DemoAlbumInheritedProperties(TypedDict):
    """DemoAlbum.

    References:
        https://schema.org/DemoAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class DemoAlbumProperties(TypedDict):
    """DemoAlbum.

    References:
        https://schema.org/DemoAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class DemoAlbumAllProperties(
    DemoAlbumInheritedProperties, DemoAlbumProperties, TypedDict
):
    pass


class DemoAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DemoAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DemoAlbumProperties, DemoAlbumInheritedProperties, DemoAlbumAllProperties
    ] = DemoAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DemoAlbum"
    return model


DemoAlbum = create_schema_org_model()


def create_demoalbum_model(
    model: Union[
        DemoAlbumProperties, DemoAlbumInheritedProperties, DemoAlbumAllProperties
    ]
):
    _type = deepcopy(DemoAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DemoAlbumAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DemoAlbumAllProperties):
    pydantic_type = create_demoalbum_model(model=model)
    return pydantic_type(model).schema_json()
