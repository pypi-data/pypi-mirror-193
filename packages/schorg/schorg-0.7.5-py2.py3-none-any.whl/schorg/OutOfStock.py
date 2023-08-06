"""
Indicates that the item is out of stock.

https://schema.org/OutOfStock
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OutOfStockInheritedProperties(TypedDict):
    """Indicates that the item is out of stock.

    References:
        https://schema.org/OutOfStock
    Note:
        Model Depth 5
    Attributes:
    """


class OutOfStockProperties(TypedDict):
    """Indicates that the item is out of stock.

    References:
        https://schema.org/OutOfStock
    Note:
        Model Depth 5
    Attributes:
    """


class OutOfStockAllProperties(
    OutOfStockInheritedProperties, OutOfStockProperties, TypedDict
):
    pass


class OutOfStockBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OutOfStock", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OutOfStockProperties, OutOfStockInheritedProperties, OutOfStockAllProperties
    ] = OutOfStockAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OutOfStock"
    return model


OutOfStock = create_schema_org_model()


def create_outofstock_model(
    model: Union[
        OutOfStockProperties, OutOfStockInheritedProperties, OutOfStockAllProperties
    ]
):
    _type = deepcopy(OutOfStockAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of OutOfStock. Please see: https://schema.org/OutOfStock"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OutOfStockAllProperties):
    pydantic_type = create_outofstock_model(model=model)
    return pydantic_type(model).schema_json()
