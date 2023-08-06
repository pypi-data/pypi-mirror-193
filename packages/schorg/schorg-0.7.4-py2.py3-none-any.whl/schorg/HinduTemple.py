"""
A Hindu temple.

https://schema.org/HinduTemple
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HinduTempleInheritedProperties(TypedDict):
    """A Hindu temple.

    References:
        https://schema.org/HinduTemple
    Note:
        Model Depth 5
    Attributes:
    """


class HinduTempleProperties(TypedDict):
    """A Hindu temple.

    References:
        https://schema.org/HinduTemple
    Note:
        Model Depth 5
    Attributes:
    """


class HinduTempleAllProperties(
    HinduTempleInheritedProperties, HinduTempleProperties, TypedDict
):
    pass


class HinduTempleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HinduTemple", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HinduTempleProperties, HinduTempleInheritedProperties, HinduTempleAllProperties
    ] = HinduTempleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HinduTemple"
    return model


HinduTemple = create_schema_org_model()


def create_hindutemple_model(
    model: Union[
        HinduTempleProperties, HinduTempleInheritedProperties, HinduTempleAllProperties
    ]
):
    _type = deepcopy(HinduTempleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of HinduTempleAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HinduTempleAllProperties):
    pydantic_type = create_hindutemple_model(model=model)
    return pydantic_type(model).schema_json()
