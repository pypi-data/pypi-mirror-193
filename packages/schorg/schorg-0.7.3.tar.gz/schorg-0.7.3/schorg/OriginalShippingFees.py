"""
Specifies that the customer must pay the original shipping costs when returning a product.

https://schema.org/OriginalShippingFees
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OriginalShippingFeesInheritedProperties(TypedDict):
    """Specifies that the customer must pay the original shipping costs when returning a product.

    References:
        https://schema.org/OriginalShippingFees
    Note:
        Model Depth 5
    Attributes:
    """


class OriginalShippingFeesProperties(TypedDict):
    """Specifies that the customer must pay the original shipping costs when returning a product.

    References:
        https://schema.org/OriginalShippingFees
    Note:
        Model Depth 5
    Attributes:
    """


class OriginalShippingFeesAllProperties(
    OriginalShippingFeesInheritedProperties, OriginalShippingFeesProperties, TypedDict
):
    pass


class OriginalShippingFeesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OriginalShippingFees", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OriginalShippingFeesProperties,
        OriginalShippingFeesInheritedProperties,
        OriginalShippingFeesAllProperties,
    ] = OriginalShippingFeesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OriginalShippingFees"
    return model


OriginalShippingFees = create_schema_org_model()


def create_originalshippingfees_model(
    model: Union[
        OriginalShippingFeesProperties,
        OriginalShippingFeesInheritedProperties,
        OriginalShippingFeesAllProperties,
    ]
):
    _type = deepcopy(OriginalShippingFeesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OriginalShippingFeesAllProperties):
    pydantic_type = create_originalshippingfees_model(model=model)
    return pydantic_type(model).schema_json()
