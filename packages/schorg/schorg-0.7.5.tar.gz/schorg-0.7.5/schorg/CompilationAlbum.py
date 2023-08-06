"""
CompilationAlbum.

https://schema.org/CompilationAlbum
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CompilationAlbumInheritedProperties(TypedDict):
    """CompilationAlbum.

    References:
        https://schema.org/CompilationAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class CompilationAlbumProperties(TypedDict):
    """CompilationAlbum.

    References:
        https://schema.org/CompilationAlbum
    Note:
        Model Depth 5
    Attributes:
    """


class CompilationAlbumAllProperties(
    CompilationAlbumInheritedProperties, CompilationAlbumProperties, TypedDict
):
    pass


class CompilationAlbumBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CompilationAlbum", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CompilationAlbumProperties,
        CompilationAlbumInheritedProperties,
        CompilationAlbumAllProperties,
    ] = CompilationAlbumAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CompilationAlbum"
    return model


CompilationAlbum = create_schema_org_model()


def create_compilationalbum_model(
    model: Union[
        CompilationAlbumProperties,
        CompilationAlbumInheritedProperties,
        CompilationAlbumAllProperties,
    ]
):
    _type = deepcopy(CompilationAlbumAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of CompilationAlbum. Please see: https://schema.org/CompilationAlbum"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CompilationAlbumAllProperties):
    pydantic_type = create_compilationalbum_model(model=model)
    return pydantic_type(model).schema_json()
