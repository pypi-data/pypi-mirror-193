"""
Represents the invoice price of an offered product.

https://schema.org/InvoicePrice
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InvoicePriceInheritedProperties(TypedDict):
    """Represents the invoice price of an offered product.

    References:
        https://schema.org/InvoicePrice
    Note:
        Model Depth 5
    Attributes:
    """

    


class InvoicePriceProperties(TypedDict):
    """Represents the invoice price of an offered product.

    References:
        https://schema.org/InvoicePrice
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(InvoicePriceInheritedProperties , InvoicePriceProperties, TypedDict):
    pass


class InvoicePriceBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="InvoicePrice",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[InvoicePriceProperties, InvoicePriceInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InvoicePrice"
    return model
    

InvoicePrice = create_schema_org_model()


def create_invoiceprice_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_invoiceprice_model(model=model)
    return pydantic_type(model).schema_json()


