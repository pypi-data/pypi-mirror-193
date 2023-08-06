"""
Indicates that the item is damaged.

https://schema.org/DamagedCondition
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DamagedConditionInheritedProperties(TypedDict):
    """Indicates that the item is damaged.

    References:
        https://schema.org/DamagedCondition
    Note:
        Model Depth 5
    Attributes:
    """


class DamagedConditionProperties(TypedDict):
    """Indicates that the item is damaged.

    References:
        https://schema.org/DamagedCondition
    Note:
        Model Depth 5
    Attributes:
    """


class DamagedConditionAllProperties(
    DamagedConditionInheritedProperties, DamagedConditionProperties, TypedDict
):
    pass


class DamagedConditionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DamagedCondition", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DamagedConditionProperties,
        DamagedConditionInheritedProperties,
        DamagedConditionAllProperties,
    ] = DamagedConditionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DamagedCondition"
    return model


DamagedCondition = create_schema_org_model()


def create_damagedcondition_model(
    model: Union[
        DamagedConditionProperties,
        DamagedConditionInheritedProperties,
        DamagedConditionAllProperties,
    ]
):
    _type = deepcopy(DamagedConditionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DamagedConditionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DamagedConditionAllProperties):
    pydantic_type = create_damagedcondition_model(model=model)
    return pydantic_type(model).schema_json()
