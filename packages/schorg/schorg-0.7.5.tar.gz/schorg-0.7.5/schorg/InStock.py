"""
Indicates that the item is in stock.

https://schema.org/InStock
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class InStockInheritedProperties(TypedDict):
    """Indicates that the item is in stock.

    References:
        https://schema.org/InStock
    Note:
        Model Depth 5
    Attributes:
    """


class InStockProperties(TypedDict):
    """Indicates that the item is in stock.

    References:
        https://schema.org/InStock
    Note:
        Model Depth 5
    Attributes:
    """


class InStockAllProperties(InStockInheritedProperties, InStockProperties, TypedDict):
    pass


class InStockBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="InStock", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        InStockProperties, InStockInheritedProperties, InStockAllProperties
    ] = InStockAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "InStock"
    return model


InStock = create_schema_org_model()


def create_instock_model(
    model: Union[InStockProperties, InStockInheritedProperties, InStockAllProperties]
):
    _type = deepcopy(InStockAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of InStock. Please see: https://schema.org/InStock"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: InStockAllProperties):
    pydantic_type = create_instock_model(model=model)
    return pydantic_type(model).schema_json()
