"""
RemixAlbum.

https://schema.org/RemixAlbum
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(RemixAlbumInheritedProperties , RemixAlbumProperties, TypedDict):
    pass


class RemixAlbumBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RemixAlbum",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RemixAlbumProperties, RemixAlbumInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RemixAlbum"
    return model
    

RemixAlbum = create_schema_org_model()


def create_remixalbum_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_remixalbum_model(model=model)
    return pydantic_type(model).schema_json()


