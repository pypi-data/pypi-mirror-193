"""
Indicates that the item is in stock.

https://schema.org/InStock
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InStockInheritedProperties(TypedDict):
    """Indicates that the item is in stock.

    References:
        https://schema.org/InStock
    Note:
        Model Depth 5
    Attributes:
    """

    


class InStockProperties(TypedDict):
    """Indicates that the item is in stock.

    References:
        https://schema.org/InStock
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(InStockInheritedProperties , InStockProperties, TypedDict):
    pass


class InStockBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="InStock",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[InStockProperties, InStockInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InStock"
    return model
    

InStock = create_schema_org_model()


def create_instock_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_instock_model(model=model)
    return pydantic_type(model).schema_json()


