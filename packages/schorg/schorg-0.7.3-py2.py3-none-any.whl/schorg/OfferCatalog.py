"""
An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.

https://schema.org/OfferCatalog
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfferCatalogInheritedProperties(TypedDict):
    """An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.

    References:
        https://schema.org/OfferCatalog
    Note:
        Model Depth 4
    Attributes:
        itemListOrder: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Type of ordering (e.g. Ascending, Descending, Unordered).
        numberOfItems: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list.
        itemListElement: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.Note: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a 'position' property in such cases.
    """

    itemListOrder: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    numberOfItems: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    itemListElement: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class OfferCatalogProperties(TypedDict):
    """An OfferCatalog is an ItemList that contains related Offers and/or further OfferCatalogs that are offeredBy the same provider.

    References:
        https://schema.org/OfferCatalog
    Note:
        Model Depth 4
    Attributes:
    """


class OfferCatalogAllProperties(
    OfferCatalogInheritedProperties, OfferCatalogProperties, TypedDict
):
    pass


class OfferCatalogBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OfferCatalog", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"itemListOrder": {"exclude": True}}
        fields = {"numberOfItems": {"exclude": True}}
        fields = {"itemListElement": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        OfferCatalogProperties,
        OfferCatalogInheritedProperties,
        OfferCatalogAllProperties,
    ] = OfferCatalogAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OfferCatalog"
    return model


OfferCatalog = create_schema_org_model()


def create_offercatalog_model(
    model: Union[
        OfferCatalogProperties,
        OfferCatalogInheritedProperties,
        OfferCatalogAllProperties,
    ]
):
    _type = deepcopy(OfferCatalogAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OfferCatalogAllProperties):
    pydantic_type = create_offercatalog_model(model=model)
    return pydantic_type(model).schema_json()
