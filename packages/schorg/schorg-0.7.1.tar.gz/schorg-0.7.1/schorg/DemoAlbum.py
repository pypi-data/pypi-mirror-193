"""
DemoAlbum.

https://schema.org/DemoAlbum
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(DemoAlbumInheritedProperties , DemoAlbumProperties, TypedDict):
    pass


class DemoAlbumBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DemoAlbum",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DemoAlbumProperties, DemoAlbumInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DemoAlbum"
    return model
    

DemoAlbum = create_schema_org_model()


def create_demoalbum_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_demoalbum_model(model=model)
    return pydantic_type(model).schema_json()


