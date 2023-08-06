"""
An enumeration of several kinds of Map.

https://schema.org/MapCategoryType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MapCategoryTypeInheritedProperties(TypedDict):
    """An enumeration of several kinds of Map.

    References:
        https://schema.org/MapCategoryType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class MapCategoryTypeProperties(TypedDict):
    """An enumeration of several kinds of Map.

    References:
        https://schema.org/MapCategoryType
    Note:
        Model Depth 4
    Attributes:
    """


class MapCategoryTypeAllProperties(
    MapCategoryTypeInheritedProperties, MapCategoryTypeProperties, TypedDict
):
    pass


class MapCategoryTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MapCategoryType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        MapCategoryTypeProperties,
        MapCategoryTypeInheritedProperties,
        MapCategoryTypeAllProperties,
    ] = MapCategoryTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MapCategoryType"
    return model


MapCategoryType = create_schema_org_model()


def create_mapcategorytype_model(
    model: Union[
        MapCategoryTypeProperties,
        MapCategoryTypeInheritedProperties,
        MapCategoryTypeAllProperties,
    ]
):
    _type = deepcopy(MapCategoryTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MapCategoryTypeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MapCategoryTypeAllProperties):
    pydantic_type = create_mapcategorytype_model(model=model)
    return pydantic_type(model).schema_json()
