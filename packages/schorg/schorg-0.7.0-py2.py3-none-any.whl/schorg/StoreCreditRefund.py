"""
Specifies that the customer receives a store credit as refund when returning a product.

https://schema.org/StoreCreditRefund
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class StoreCreditRefundInheritedProperties(TypedDict):
    """Specifies that the customer receives a store credit as refund when returning a product.

    References:
        https://schema.org/StoreCreditRefund
    Note:
        Model Depth 5
    Attributes:
    """

    


class StoreCreditRefundProperties(TypedDict):
    """Specifies that the customer receives a store credit as refund when returning a product.

    References:
        https://schema.org/StoreCreditRefund
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(StoreCreditRefundInheritedProperties , StoreCreditRefundProperties, TypedDict):
    pass


class StoreCreditRefundBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="StoreCreditRefund",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[StoreCreditRefundProperties, StoreCreditRefundInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "StoreCreditRefund"
    return model
    

StoreCreditRefund = create_schema_org_model()


def create_storecreditrefund_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_storecreditrefund_model(model=model)
    return pydantic_type(model).schema_json()


