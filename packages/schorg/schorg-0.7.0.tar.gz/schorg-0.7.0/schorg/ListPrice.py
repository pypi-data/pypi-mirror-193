"""
Represents the list price (the price a product is actually advertised for) of an offered product.

https://schema.org/ListPrice
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ListPriceInheritedProperties , ListPriceProperties, TypedDict):
    pass


class ListPriceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ListPrice",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ListPriceProperties, ListPriceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ListPrice"
    return model
    

ListPrice = create_schema_org_model()


def create_listprice_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_listprice_model(model=model)
    return pydantic_type(model).schema_json()


