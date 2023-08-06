"""
An ItemList ordered with lower values listed first.

https://schema.org/ItemListOrderAscending
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ItemListOrderAscendingInheritedProperties(TypedDict):
    """An ItemList ordered with lower values listed first.

    References:
        https://schema.org/ItemListOrderAscending
    Note:
        Model Depth 5
    Attributes:
    """


class ItemListOrderAscendingProperties(TypedDict):
    """An ItemList ordered with lower values listed first.

    References:
        https://schema.org/ItemListOrderAscending
    Note:
        Model Depth 5
    Attributes:
    """


class ItemListOrderAscendingAllProperties(
    ItemListOrderAscendingInheritedProperties,
    ItemListOrderAscendingProperties,
    TypedDict,
):
    pass


class ItemListOrderAscendingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ItemListOrderAscending", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ItemListOrderAscendingProperties,
        ItemListOrderAscendingInheritedProperties,
        ItemListOrderAscendingAllProperties,
    ] = ItemListOrderAscendingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ItemListOrderAscending"
    return model


ItemListOrderAscending = create_schema_org_model()


def create_itemlistorderascending_model(
    model: Union[
        ItemListOrderAscendingProperties,
        ItemListOrderAscendingInheritedProperties,
        ItemListOrderAscendingAllProperties,
    ]
):
    _type = deepcopy(ItemListOrderAscendingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ItemListOrderAscending. Please see: https://schema.org/ItemListOrderAscending"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ItemListOrderAscendingAllProperties):
    pydantic_type = create_itemlistorderascending_model(model=model)
    return pydantic_type(model).schema_json()
