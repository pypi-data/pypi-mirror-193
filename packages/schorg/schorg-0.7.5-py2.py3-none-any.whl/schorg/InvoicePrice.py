"""
Represents the invoice price of an offered product.

https://schema.org/InvoicePrice
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class InvoicePriceAllProperties(
    InvoicePriceInheritedProperties, InvoicePriceProperties, TypedDict
):
    pass


class InvoicePriceBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="InvoicePrice", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        InvoicePriceProperties,
        InvoicePriceInheritedProperties,
        InvoicePriceAllProperties,
    ] = InvoicePriceAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InvoicePrice"
    return model


InvoicePrice = create_schema_org_model()


def create_invoiceprice_model(
    model: Union[
        InvoicePriceProperties,
        InvoicePriceInheritedProperties,
        InvoicePriceAllProperties,
    ]
):
    _type = deepcopy(InvoicePriceAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of InvoicePrice. Please see: https://schema.org/InvoicePrice"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: InvoicePriceAllProperties):
    pydantic_type = create_invoiceprice_model(model=model)
    return pydantic_type(model).schema_json()
