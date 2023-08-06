"""
The kind of release which this album is: single, EP or album.

https://schema.org/MusicAlbumReleaseType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MusicAlbumReleaseTypeInheritedProperties(TypedDict):
    """The kind of release which this album is: single, EP or album.

    References:
        https://schema.org/MusicAlbumReleaseType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class MusicAlbumReleaseTypeProperties(TypedDict):
    """The kind of release which this album is: single, EP or album.

    References:
        https://schema.org/MusicAlbumReleaseType
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MusicAlbumReleaseTypeInheritedProperties , MusicAlbumReleaseTypeProperties, TypedDict):
    pass


class MusicAlbumReleaseTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MusicAlbumReleaseType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MusicAlbumReleaseTypeProperties, MusicAlbumReleaseTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MusicAlbumReleaseType"
    return model
    

MusicAlbumReleaseType = create_schema_org_model()


def create_musicalbumreleasetype_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_musicalbumreleasetype_model(model=model)
    return pydantic_type(model).schema_json()


