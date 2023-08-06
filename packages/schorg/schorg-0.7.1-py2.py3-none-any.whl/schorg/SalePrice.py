"""
Represents a sale price (usually active for a limited period) of an offered product.

https://schema.org/SalePrice
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SalePriceInheritedProperties(TypedDict):
    """Represents a sale price (usually active for a limited period) of an offered product.

    References:
        https://schema.org/SalePrice
    Note:
        Model Depth 5
    Attributes:
    """

    


class SalePriceProperties(TypedDict):
    """Represents a sale price (usually active for a limited period) of an offered product.

    References:
        https://schema.org/SalePrice
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SalePriceInheritedProperties , SalePriceProperties, TypedDict):
    pass


class SalePriceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SalePrice",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SalePriceProperties, SalePriceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SalePrice"
    return model
    

SalePrice = create_schema_org_model()


def create_saleprice_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_saleprice_model(model=model)
    return pydantic_type(model).schema_json()


