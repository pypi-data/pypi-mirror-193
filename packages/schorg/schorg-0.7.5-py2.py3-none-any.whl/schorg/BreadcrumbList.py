"""
A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page.The [[position]] property is used to reconstruct the order of the items in a BreadcrumbList. The convention is that a breadcrumb list has an [[itemListOrder]] of [[ItemListOrderAscending]] (lower values listed first), and that the first items in this list correspond to the "top" or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific values of 'position' are not assigned meaning for a BreadcrumbList, but they should be integers, e.g. beginning with '1' for the first item in the list.      

https://schema.org/BreadcrumbList
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BreadcrumbListInheritedProperties(TypedDict):
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page.The [[position]] property is used to reconstruct the order of the items in a BreadcrumbList. The convention is that a breadcrumb list has an [[itemListOrder]] of [[ItemListOrderAscending]] (lower values listed first), and that the first items in this list correspond to the "top" or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific values of 'position' are not assigned meaning for a BreadcrumbList, but they should be integers, e.g. beginning with '1' for the first item in the list.

    References:
        https://schema.org/BreadcrumbList
    Note:
        Model Depth 4
    Attributes:
        itemListOrder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Type of ordering (e.g. Ascending, Descending, Unordered).
        numberOfItems: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list.
        itemListElement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.Note: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a 'position' property in such cases.
    """

    itemListOrder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfItems: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    itemListElement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class BreadcrumbListProperties(TypedDict):
    """A BreadcrumbList is an ItemList consisting of a chain of linked Web pages, typically described using at least their URL and their name, and typically ending with the current page.The [[position]] property is used to reconstruct the order of the items in a BreadcrumbList. The convention is that a breadcrumb list has an [[itemListOrder]] of [[ItemListOrderAscending]] (lower values listed first), and that the first items in this list correspond to the "top" or beginning of the breadcrumb trail, e.g. with a site or section homepage. The specific values of 'position' are not assigned meaning for a BreadcrumbList, but they should be integers, e.g. beginning with '1' for the first item in the list.

    References:
        https://schema.org/BreadcrumbList
    Note:
        Model Depth 4
    Attributes:
    """


class BreadcrumbListAllProperties(
    BreadcrumbListInheritedProperties, BreadcrumbListProperties, TypedDict
):
    pass


class BreadcrumbListBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BreadcrumbList", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"itemListOrder": {"exclude": True}}
        fields = {"numberOfItems": {"exclude": True}}
        fields = {"itemListElement": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BreadcrumbListProperties,
        BreadcrumbListInheritedProperties,
        BreadcrumbListAllProperties,
    ] = BreadcrumbListAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BreadcrumbList"
    return model


BreadcrumbList = create_schema_org_model()


def create_breadcrumblist_model(
    model: Union[
        BreadcrumbListProperties,
        BreadcrumbListInheritedProperties,
        BreadcrumbListAllProperties,
    ]
):
    _type = deepcopy(BreadcrumbListAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BreadcrumbList. Please see: https://schema.org/BreadcrumbList"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BreadcrumbListAllProperties):
    pydantic_type = create_breadcrumblist_model(model=model)
    return pydantic_type(model).schema_json()
