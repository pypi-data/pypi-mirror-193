"""
Classification of the album by its type of content: soundtrack, live album, studio album, etc.

https://schema.org/MusicAlbumProductionType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MusicAlbumProductionTypeInheritedProperties(TypedDict):
    """Classification of the album by its type of content: soundtrack, live album, studio album, etc.

    References:
        https://schema.org/MusicAlbumProductionType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class MusicAlbumProductionTypeProperties(TypedDict):
    """Classification of the album by its type of content: soundtrack, live album, studio album, etc.

    References:
        https://schema.org/MusicAlbumProductionType
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MusicAlbumProductionTypeInheritedProperties , MusicAlbumProductionTypeProperties, TypedDict):
    pass


class MusicAlbumProductionTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MusicAlbumProductionType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MusicAlbumProductionTypeProperties, MusicAlbumProductionTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MusicAlbumProductionType"
    return model
    

MusicAlbumProductionType = create_schema_org_model()


def create_musicalbumproductiontype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_musicalbumproductiontype_model(model=model)
    return pydantic_type(model).schema_json()


