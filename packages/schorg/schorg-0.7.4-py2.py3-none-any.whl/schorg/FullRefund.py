"""
Specifies that a refund can be done in the full amount the customer paid for the product.

https://schema.org/FullRefund
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FullRefundInheritedProperties(TypedDict):
    """Specifies that a refund can be done in the full amount the customer paid for the product.

    References:
        https://schema.org/FullRefund
    Note:
        Model Depth 5
    Attributes:
    """


class FullRefundProperties(TypedDict):
    """Specifies that a refund can be done in the full amount the customer paid for the product.

    References:
        https://schema.org/FullRefund
    Note:
        Model Depth 5
    Attributes:
    """


class FullRefundAllProperties(
    FullRefundInheritedProperties, FullRefundProperties, TypedDict
):
    pass


class FullRefundBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FullRefund", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FullRefundProperties, FullRefundInheritedProperties, FullRefundAllProperties
    ] = FullRefundAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FullRefund"
    return model


FullRefund = create_schema_org_model()


def create_fullrefund_model(
    model: Union[
        FullRefundProperties, FullRefundInheritedProperties, FullRefundAllProperties
    ]
):
    _type = deepcopy(FullRefundAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of FullRefundAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FullRefundAllProperties):
    pydantic_type = create_fullrefund_model(model=model)
    return pydantic_type(model).schema_json()
