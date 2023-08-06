"""
An enumeration of several kinds of Map.

https://schema.org/MapCategoryType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MapCategoryTypeInheritedProperties(TypedDict):
    """An enumeration of several kinds of Map.

    References:
        https://schema.org/MapCategoryType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class MapCategoryTypeProperties(TypedDict):
    """An enumeration of several kinds of Map.

    References:
        https://schema.org/MapCategoryType
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MapCategoryTypeInheritedProperties , MapCategoryTypeProperties, TypedDict):
    pass


class MapCategoryTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MapCategoryType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MapCategoryTypeProperties, MapCategoryTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MapCategoryType"
    return model
    

MapCategoryType = create_schema_org_model()


def create_mapcategorytype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mapcategorytype_model(model=model)
    return pydantic_type(model).schema_json()


