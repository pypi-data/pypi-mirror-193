"""
Indicates that the item is refurbished.

https://schema.org/RefurbishedCondition
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RefurbishedConditionInheritedProperties(TypedDict):
    """Indicates that the item is refurbished.

    References:
        https://schema.org/RefurbishedCondition
    Note:
        Model Depth 5
    Attributes:
    """


class RefurbishedConditionProperties(TypedDict):
    """Indicates that the item is refurbished.

    References:
        https://schema.org/RefurbishedCondition
    Note:
        Model Depth 5
    Attributes:
    """


class RefurbishedConditionAllProperties(
    RefurbishedConditionInheritedProperties, RefurbishedConditionProperties, TypedDict
):
    pass


class RefurbishedConditionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RefurbishedCondition", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RefurbishedConditionProperties,
        RefurbishedConditionInheritedProperties,
        RefurbishedConditionAllProperties,
    ] = RefurbishedConditionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RefurbishedCondition"
    return model


RefurbishedCondition = create_schema_org_model()


def create_refurbishedcondition_model(
    model: Union[
        RefurbishedConditionProperties,
        RefurbishedConditionInheritedProperties,
        RefurbishedConditionAllProperties,
    ]
):
    _type = deepcopy(RefurbishedConditionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RefurbishedConditionAllProperties):
    pydantic_type = create_refurbishedcondition_model(model=model)
    return pydantic_type(model).schema_json()
