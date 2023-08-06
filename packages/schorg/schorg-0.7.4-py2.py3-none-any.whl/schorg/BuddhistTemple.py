"""
A Buddhist temple.

https://schema.org/BuddhistTemple
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BuddhistTempleInheritedProperties(TypedDict):
    """A Buddhist temple.

    References:
        https://schema.org/BuddhistTemple
    Note:
        Model Depth 5
    Attributes:
    """


class BuddhistTempleProperties(TypedDict):
    """A Buddhist temple.

    References:
        https://schema.org/BuddhistTemple
    Note:
        Model Depth 5
    Attributes:
    """


class BuddhistTempleAllProperties(
    BuddhistTempleInheritedProperties, BuddhistTempleProperties, TypedDict
):
    pass


class BuddhistTempleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BuddhistTemple", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BuddhistTempleProperties,
        BuddhistTempleInheritedProperties,
        BuddhistTempleAllProperties,
    ] = BuddhistTempleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BuddhistTemple"
    return model


BuddhistTemple = create_schema_org_model()


def create_buddhisttemple_model(
    model: Union[
        BuddhistTempleProperties,
        BuddhistTempleInheritedProperties,
        BuddhistTempleAllProperties,
    ]
):
    _type = deepcopy(BuddhistTempleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of BuddhistTempleAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BuddhistTempleAllProperties):
    pydantic_type = create_buddhisttemple_model(model=model)
    return pydantic_type(model).schema_json()
