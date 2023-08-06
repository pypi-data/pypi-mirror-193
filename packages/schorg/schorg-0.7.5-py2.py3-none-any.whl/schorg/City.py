"""
A city or town.

https://schema.org/City
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CityInheritedProperties(TypedDict):
    """A city or town.

    References:
        https://schema.org/City
    Note:
        Model Depth 4
    Attributes:
    """


class CityProperties(TypedDict):
    """A city or town.

    References:
        https://schema.org/City
    Note:
        Model Depth 4
    Attributes:
    """


class CityAllProperties(CityInheritedProperties, CityProperties, TypedDict):
    pass


class CityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="City", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CityProperties, CityInheritedProperties, CityAllProperties
    ] = CityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "City"
    return model


City = create_schema_org_model()


def create_city_model(
    model: Union[CityProperties, CityInheritedProperties, CityAllProperties]
):
    _type = deepcopy(CityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of City. Please see: https://schema.org/City"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: CityAllProperties):
    pydantic_type = create_city_model(model=model)
    return pydantic_type(model).schema_json()
