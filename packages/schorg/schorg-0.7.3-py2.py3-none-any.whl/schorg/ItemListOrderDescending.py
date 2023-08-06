"""
An ItemList ordered with higher values listed first.

https://schema.org/ItemListOrderDescending
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class ItemListOrderDescendingAllProperties(
    ItemListOrderDescendingInheritedProperties,
    ItemListOrderDescendingProperties,
    TypedDict,
):
    pass


class ItemListOrderDescendingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ItemListOrderDescending", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ItemListOrderDescendingProperties,
        ItemListOrderDescendingInheritedProperties,
        ItemListOrderDescendingAllProperties,
    ] = ItemListOrderDescendingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ItemListOrderDescending"
    return model


ItemListOrderDescending = create_schema_org_model()


def create_itemlistorderdescending_model(
    model: Union[
        ItemListOrderDescendingProperties,
        ItemListOrderDescendingInheritedProperties,
        ItemListOrderDescendingAllProperties,
    ]
):
    _type = deepcopy(ItemListOrderDescendingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ItemListOrderDescendingAllProperties):
    pydantic_type = create_itemlistorderdescending_model(model=model)
    return pydantic_type(model).schema_json()
