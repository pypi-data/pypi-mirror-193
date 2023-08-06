"""
An ItemList ordered with no explicit order.

https://schema.org/ItemListUnordered
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ItemListUnorderedInheritedProperties(TypedDict):
    """An ItemList ordered with no explicit order.

    References:
        https://schema.org/ItemListUnordered
    Note:
        Model Depth 5
    Attributes:
    """


class ItemListUnorderedProperties(TypedDict):
    """An ItemList ordered with no explicit order.

    References:
        https://schema.org/ItemListUnordered
    Note:
        Model Depth 5
    Attributes:
    """


class ItemListUnorderedAllProperties(
    ItemListUnorderedInheritedProperties, ItemListUnorderedProperties, TypedDict
):
    pass


class ItemListUnorderedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ItemListUnordered", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ItemListUnorderedProperties,
        ItemListUnorderedInheritedProperties,
        ItemListUnorderedAllProperties,
    ] = ItemListUnorderedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ItemListUnordered"
    return model


ItemListUnordered = create_schema_org_model()


def create_itemlistunordered_model(
    model: Union[
        ItemListUnorderedProperties,
        ItemListUnorderedInheritedProperties,
        ItemListUnorderedAllProperties,
    ]
):
    _type = deepcopy(ItemListUnorderedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ItemListUnorderedAllProperties):
    pydantic_type = create_itemlistunordered_model(model=model)
    return pydantic_type(model).schema_json()
