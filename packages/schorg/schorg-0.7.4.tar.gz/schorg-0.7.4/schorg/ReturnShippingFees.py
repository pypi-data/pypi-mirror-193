"""
Specifies that the customer must pay the return shipping costs when returning a product.

https://schema.org/ReturnShippingFees
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReturnShippingFeesInheritedProperties(TypedDict):
    """Specifies that the customer must pay the return shipping costs when returning a product.

    References:
        https://schema.org/ReturnShippingFees
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnShippingFeesProperties(TypedDict):
    """Specifies that the customer must pay the return shipping costs when returning a product.

    References:
        https://schema.org/ReturnShippingFees
    Note:
        Model Depth 5
    Attributes:
    """


class ReturnShippingFeesAllProperties(
    ReturnShippingFeesInheritedProperties, ReturnShippingFeesProperties, TypedDict
):
    pass


class ReturnShippingFeesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReturnShippingFees", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReturnShippingFeesProperties,
        ReturnShippingFeesInheritedProperties,
        ReturnShippingFeesAllProperties,
    ] = ReturnShippingFeesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReturnShippingFees"
    return model


ReturnShippingFees = create_schema_org_model()


def create_returnshippingfees_model(
    model: Union[
        ReturnShippingFeesProperties,
        ReturnShippingFeesInheritedProperties,
        ReturnShippingFeesAllProperties,
    ]
):
    _type = deepcopy(ReturnShippingFeesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ReturnShippingFeesAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReturnShippingFeesAllProperties):
    pydantic_type = create_returnshippingfees_model(model=model)
    return pydantic_type(model).schema_json()
