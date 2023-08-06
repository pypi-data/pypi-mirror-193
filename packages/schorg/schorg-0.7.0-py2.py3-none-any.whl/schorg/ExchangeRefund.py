"""
Specifies that a refund can be done as an exchange for the same product.

https://schema.org/ExchangeRefund
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ExchangeRefundInheritedProperties , ExchangeRefundProperties, TypedDict):
    pass


class ExchangeRefundBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ExchangeRefund",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ExchangeRefundProperties, ExchangeRefundInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ExchangeRefund"
    return model
    

ExchangeRefund = create_schema_org_model()


def create_exchangerefund_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_exchangerefund_model(model=model)
    return pydantic_type(model).schema_json()


