"""
Indicates that the item is refurbished.

https://schema.org/RefurbishedCondition
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(RefurbishedConditionInheritedProperties , RefurbishedConditionProperties, TypedDict):
    pass


class RefurbishedConditionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RefurbishedCondition",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RefurbishedConditionProperties, RefurbishedConditionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RefurbishedCondition"
    return model
    

RefurbishedCondition = create_schema_org_model()


def create_refurbishedcondition_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_refurbishedcondition_model(model=model)
    return pydantic_type(model).schema_json()


