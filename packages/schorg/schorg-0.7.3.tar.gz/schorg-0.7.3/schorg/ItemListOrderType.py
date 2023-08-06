"""
Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.

https://schema.org/ItemListOrderType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ItemListOrderTypeInheritedProperties(TypedDict):
    """Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.

    References:
        https://schema.org/ItemListOrderType
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ItemListOrderTypeProperties(TypedDict):
    """Enumerated for values for itemListOrder for indicating how an ordered ItemList is organized.

    References:
        https://schema.org/ItemListOrderType
    Note:
        Model Depth 4
    Attributes:
    """


class ItemListOrderTypeAllProperties(
    ItemListOrderTypeInheritedProperties, ItemListOrderTypeProperties, TypedDict
):
    pass


class ItemListOrderTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ItemListOrderType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ItemListOrderTypeProperties,
        ItemListOrderTypeInheritedProperties,
        ItemListOrderTypeAllProperties,
    ] = ItemListOrderTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ItemListOrderType"
    return model


ItemListOrderType = create_schema_org_model()


def create_itemlistordertype_model(
    model: Union[
        ItemListOrderTypeProperties,
        ItemListOrderTypeInheritedProperties,
        ItemListOrderTypeAllProperties,
    ]
):
    _type = deepcopy(ItemListOrderTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ItemListOrderTypeAllProperties):
    pydantic_type = create_itemlistordertype_model(model=model)
    return pydantic_type(model).schema_json()
