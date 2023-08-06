"""
A city hall.

https://schema.org/CityHall
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CityHallInheritedProperties(TypedDict):
    """A city hall.

    References:
        https://schema.org/CityHall
    Note:
        Model Depth 5
    Attributes:
    """


class CityHallProperties(TypedDict):
    """A city hall.

    References:
        https://schema.org/CityHall
    Note:
        Model Depth 5
    Attributes:
    """


class CityHallAllProperties(CityHallInheritedProperties, CityHallProperties, TypedDict):
    pass


class CityHallBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CityHall", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        CityHallProperties, CityHallInheritedProperties, CityHallAllProperties
    ] = CityHallAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CityHall"
    return model


CityHall = create_schema_org_model()


def create_cityhall_model(
    model: Union[CityHallProperties, CityHallInheritedProperties, CityHallAllProperties]
):
    _type = deepcopy(CityHallAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CityHallAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CityHallAllProperties):
    pydantic_type = create_cityhall_model(model=model)
    return pydantic_type(model).schema_json()
