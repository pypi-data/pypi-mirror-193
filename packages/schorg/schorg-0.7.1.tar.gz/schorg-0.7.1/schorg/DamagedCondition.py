"""
Indicates that the item is damaged.

https://schema.org/DamagedCondition
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(DamagedConditionInheritedProperties , DamagedConditionProperties, TypedDict):
    pass


class DamagedConditionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DamagedCondition",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DamagedConditionProperties, DamagedConditionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DamagedCondition"
    return model
    

DamagedCondition = create_schema_org_model()


def create_damagedcondition_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_damagedcondition_model(model=model)
    return pydantic_type(model).schema_json()


