"""
The payment is due and considered late.

https://schema.org/PaymentPastDue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentPastDueInheritedProperties(TypedDict):
    """The payment is due and considered late.

    References:
        https://schema.org/PaymentPastDue
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentPastDueProperties(TypedDict):
    """The payment is due and considered late.

    References:
        https://schema.org/PaymentPastDue
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentPastDueAllProperties(
    PaymentPastDueInheritedProperties, PaymentPastDueProperties, TypedDict
):
    pass


class PaymentPastDueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentPastDue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PaymentPastDueProperties,
        PaymentPastDueInheritedProperties,
        PaymentPastDueAllProperties,
    ] = PaymentPastDueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentPastDue"
    return model


PaymentPastDue = create_schema_org_model()


def create_paymentpastdue_model(
    model: Union[
        PaymentPastDueProperties,
        PaymentPastDueInheritedProperties,
        PaymentPastDueAllProperties,
    ]
):
    _type = deepcopy(PaymentPastDueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PaymentPastDueAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PaymentPastDueAllProperties):
    pydantic_type = create_paymentpastdue_model(model=model)
    return pydantic_type(model).schema_json()
