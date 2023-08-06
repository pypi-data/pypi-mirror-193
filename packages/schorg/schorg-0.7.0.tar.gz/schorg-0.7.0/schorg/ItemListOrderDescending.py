"""
An ItemList ordered with higher values listed first.

https://schema.org/ItemListOrderDescending
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ItemListOrderDescendingInheritedProperties(TypedDict):
    """An ItemList ordered with higher values listed first.

    References:
        https://schema.org/ItemListOrderDescending
    Note:
        Model Depth 5
    Attributes:
    """

    


class ItemListOrderDescendingProperties(TypedDict):
    """An ItemList ordered with higher values listed first.

    References:
        https://schema.org/ItemListOrderDescending
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ItemListOrderDescendingInheritedProperties , ItemListOrderDescendingProperties, TypedDict):
    pass


class ItemListOrderDescendingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ItemListOrderDescending",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ItemListOrderDescendingProperties, ItemListOrderDescendingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ItemListOrderDescending"
    return model
    

ItemListOrderDescending = create_schema_org_model()


def create_itemlistorderdescending_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_itemlistorderdescending_model(model=model)
    return pydantic_type(model).schema_json()


