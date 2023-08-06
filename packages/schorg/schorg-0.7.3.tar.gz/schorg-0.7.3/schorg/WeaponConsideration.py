"""
The item is intended to induce bodily harm, for example guns, mace, combat knives, brass knuckles, nail or other bombs, and spears.

https://schema.org/WeaponConsideration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WeaponConsiderationInheritedProperties(TypedDict):
    """The item is intended to induce bodily harm, for example guns, mace, combat knives, brass knuckles, nail or other bombs, and spears.

    References:
        https://schema.org/WeaponConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class WeaponConsiderationProperties(TypedDict):
    """The item is intended to induce bodily harm, for example guns, mace, combat knives, brass knuckles, nail or other bombs, and spears.

    References:
        https://schema.org/WeaponConsideration
    Note:
        Model Depth 5
    Attributes:
    """


class WeaponConsiderationAllProperties(
    WeaponConsiderationInheritedProperties, WeaponConsiderationProperties, TypedDict
):
    pass


class WeaponConsiderationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WeaponConsideration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WeaponConsiderationProperties,
        WeaponConsiderationInheritedProperties,
        WeaponConsiderationAllProperties,
    ] = WeaponConsiderationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WeaponConsideration"
    return model


WeaponConsideration = create_schema_org_model()


def create_weaponconsideration_model(
    model: Union[
        WeaponConsiderationProperties,
        WeaponConsiderationInheritedProperties,
        WeaponConsiderationAllProperties,
    ]
):
    _type = deepcopy(WeaponConsiderationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WeaponConsiderationAllProperties):
    pydantic_type = create_weaponconsideration_model(model=model)
    return pydantic_type(model).schema_json()
