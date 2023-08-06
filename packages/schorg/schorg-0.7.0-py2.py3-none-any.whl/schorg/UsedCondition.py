"""
Indicates that the item is used.

https://schema.org/UsedCondition
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(UsedConditionInheritedProperties , UsedConditionProperties, TypedDict):
    pass


class UsedConditionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="UsedCondition",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[UsedConditionProperties, UsedConditionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UsedCondition"
    return model
    

UsedCondition = create_schema_org_model()


def create_usedcondition_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_usedcondition_model(model=model)
    return pydantic_type(model).schema_json()


