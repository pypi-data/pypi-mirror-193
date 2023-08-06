"""
Indicates that the item is used.

https://schema.org/UsedCondition
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UsedConditionInheritedProperties(TypedDict):
    """Indicates that the item is used.

    References:
        https://schema.org/UsedCondition
    Note:
        Model Depth 5
    Attributes:
    """


class UsedConditionProperties(TypedDict):
    """Indicates that the item is used.

    References:
        https://schema.org/UsedCondition
    Note:
        Model Depth 5
    Attributes:
    """


class UsedConditionAllProperties(
    UsedConditionInheritedProperties, UsedConditionProperties, TypedDict
):
    pass


class UsedConditionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UsedCondition", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UsedConditionProperties,
        UsedConditionInheritedProperties,
        UsedConditionAllProperties,
    ] = UsedConditionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UsedCondition"
    return model


UsedCondition = create_schema_org_model()


def create_usedcondition_model(
    model: Union[
        UsedConditionProperties,
        UsedConditionInheritedProperties,
        UsedConditionAllProperties,
    ]
):
    _type = deepcopy(UsedConditionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UsedConditionAllProperties):
    pydantic_type = create_usedcondition_model(model=model)
    return pydantic_type(model).schema_json()
