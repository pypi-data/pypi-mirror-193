"""
A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.

https://schema.org/ItemList
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ItemListInheritedProperties(TypedDict):
    """A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.

    References:
        https://schema.org/ItemList
    Note:
        Model Depth 3
    Attributes:
    """


class ItemListProperties(TypedDict):
    """A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.

    References:
        https://schema.org/ItemList
    Note:
        Model Depth 3
    Attributes:
        itemListOrder: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Type of ordering (e.g. Ascending, Descending, Unordered).
        numberOfItems: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list.
        itemListElement: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.Note: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a 'position' property in such cases.
    """

    itemListOrder: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    numberOfItems: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    itemListElement: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class ItemListAllProperties(ItemListInheritedProperties, ItemListProperties, TypedDict):
    pass


class ItemListBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ItemList", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"itemListOrder": {"exclude": True}}
        fields = {"numberOfItems": {"exclude": True}}
        fields = {"itemListElement": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ItemListProperties, ItemListInheritedProperties, ItemListAllProperties
    ] = ItemListAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ItemList"
    return model


ItemList = create_schema_org_model()


def create_itemlist_model(
    model: Union[ItemListProperties, ItemListInheritedProperties, ItemListAllProperties]
):
    _type = deepcopy(ItemListAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ItemListAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ItemListAllProperties):
    pydantic_type = create_itemlist_model(model=model)
    return pydantic_type(model).schema_json()
