"""
Specifies that a refund can be done as an exchange for the same product.

https://schema.org/ExchangeRefund
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ExchangeRefundInheritedProperties(TypedDict):
    """Specifies that a refund can be done as an exchange for the same product.

    References:
        https://schema.org/ExchangeRefund
    Note:
        Model Depth 5
    Attributes:
    """


class ExchangeRefundProperties(TypedDict):
    """Specifies that a refund can be done as an exchange for the same product.

    References:
        https://schema.org/ExchangeRefund
    Note:
        Model Depth 5
    Attributes:
    """


class ExchangeRefundAllProperties(
    ExchangeRefundInheritedProperties, ExchangeRefundProperties, TypedDict
):
    pass


class ExchangeRefundBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ExchangeRefund", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ExchangeRefundProperties,
        ExchangeRefundInheritedProperties,
        ExchangeRefundAllProperties,
    ] = ExchangeRefundAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ExchangeRefund"
    return model


ExchangeRefund = create_schema_org_model()


def create_exchangerefund_model(
    model: Union[
        ExchangeRefundProperties,
        ExchangeRefundInheritedProperties,
        ExchangeRefundAllProperties,
    ]
):
    _type = deepcopy(ExchangeRefundAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ExchangeRefundAllProperties):
    pydantic_type = create_exchangerefund_model(model=model)
    return pydantic_type(model).schema_json()
