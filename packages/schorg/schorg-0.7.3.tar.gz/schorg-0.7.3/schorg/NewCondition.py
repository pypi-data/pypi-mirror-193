"""
Indicates that the item is new.

https://schema.org/NewCondition
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NewConditionInheritedProperties(TypedDict):
    """Indicates that the item is new.

    References:
        https://schema.org/NewCondition
    Note:
        Model Depth 5
    Attributes:
    """


class NewConditionProperties(TypedDict):
    """Indicates that the item is new.

    References:
        https://schema.org/NewCondition
    Note:
        Model Depth 5
    Attributes:
    """


class NewConditionAllProperties(
    NewConditionInheritedProperties, NewConditionProperties, TypedDict
):
    pass


class NewConditionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NewCondition", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        NewConditionProperties,
        NewConditionInheritedProperties,
        NewConditionAllProperties,
    ] = NewConditionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NewCondition"
    return model


NewCondition = create_schema_org_model()


def create_newcondition_model(
    model: Union[
        NewConditionProperties,
        NewConditionInheritedProperties,
        NewConditionAllProperties,
    ]
):
    _type = deepcopy(NewConditionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NewConditionAllProperties):
    pydantic_type = create_newcondition_model(model=model)
    return pydantic_type(model).schema_json()
