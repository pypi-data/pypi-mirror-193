"""
Indicates that the item is available on back order.

https://schema.org/BackOrder
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BackOrderInheritedProperties(TypedDict):
    """Indicates that the item is available on back order.

    References:
        https://schema.org/BackOrder
    Note:
        Model Depth 5
    Attributes:
    """

    


class BackOrderProperties(TypedDict):
    """Indicates that the item is available on back order.

    References:
        https://schema.org/BackOrder
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(BackOrderInheritedProperties , BackOrderProperties, TypedDict):
    pass


class BackOrderBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BackOrder",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BackOrderProperties, BackOrderInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BackOrder"
    return model
    

BackOrder = create_schema_org_model()


def create_backorder_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_backorder_model(model=model)
    return pydantic_type(model).schema_json()


