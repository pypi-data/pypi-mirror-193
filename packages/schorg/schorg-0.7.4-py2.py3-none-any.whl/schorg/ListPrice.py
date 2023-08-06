"""
Represents the list price (the price a product is actually advertised for) of an offered product.

https://schema.org/ListPrice
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ListPriceInheritedProperties(TypedDict):
    """Represents the list price (the price a product is actually advertised for) of an offered product.

    References:
        https://schema.org/ListPrice
    Note:
        Model Depth 5
    Attributes:
    """


class ListPriceProperties(TypedDict):
    """Represents the list price (the price a product is actually advertised for) of an offered product.

    References:
        https://schema.org/ListPrice
    Note:
        Model Depth 5
    Attributes:
    """


class ListPriceAllProperties(
    ListPriceInheritedProperties, ListPriceProperties, TypedDict
):
    pass


class ListPriceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ListPrice", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ListPriceProperties, ListPriceInheritedProperties, ListPriceAllProperties
    ] = ListPriceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ListPrice"
    return model


ListPrice = create_schema_org_model()


def create_listprice_model(
    model: Union[
        ListPriceProperties, ListPriceInheritedProperties, ListPriceAllProperties
    ]
):
    _type = deepcopy(ListPriceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ListPriceAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ListPriceAllProperties):
    pydantic_type = create_listprice_model(model=model)
    return pydantic_type(model).schema_json()
