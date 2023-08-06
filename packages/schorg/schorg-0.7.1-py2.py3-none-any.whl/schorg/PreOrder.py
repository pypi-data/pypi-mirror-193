"""
Indicates that the item is available for pre-order.

https://schema.org/PreOrder
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PreOrderInheritedProperties(TypedDict):
    """Indicates that the item is available for pre-order.

    References:
        https://schema.org/PreOrder
    Note:
        Model Depth 5
    Attributes:
    """

    


class PreOrderProperties(TypedDict):
    """Indicates that the item is available for pre-order.

    References:
        https://schema.org/PreOrder
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(PreOrderInheritedProperties , PreOrderProperties, TypedDict):
    pass


class PreOrderBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PreOrder",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PreOrderProperties, PreOrderInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PreOrder"
    return model
    

PreOrder = create_schema_org_model()


def create_preorder_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_preorder_model(model=model)
    return pydantic_type(model).schema_json()


