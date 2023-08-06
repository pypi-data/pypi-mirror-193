"""
The payee received the payment, but it was declined for some reason.

https://schema.org/PaymentDeclined
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentDeclinedInheritedProperties(TypedDict):
    """The payee received the payment, but it was declined for some reason.

    References:
        https://schema.org/PaymentDeclined
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentDeclinedProperties(TypedDict):
    """The payee received the payment, but it was declined for some reason.

    References:
        https://schema.org/PaymentDeclined
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentDeclinedAllProperties(
    PaymentDeclinedInheritedProperties, PaymentDeclinedProperties, TypedDict
):
    pass


class PaymentDeclinedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentDeclined", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PaymentDeclinedProperties,
        PaymentDeclinedInheritedProperties,
        PaymentDeclinedAllProperties,
    ] = PaymentDeclinedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentDeclined"
    return model


PaymentDeclined = create_schema_org_model()


def create_paymentdeclined_model(
    model: Union[
        PaymentDeclinedProperties,
        PaymentDeclinedInheritedProperties,
        PaymentDeclinedAllProperties,
    ]
):
    _type = deepcopy(PaymentDeclinedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PaymentDeclinedAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PaymentDeclinedAllProperties):
    pydantic_type = create_paymentdeclined_model(model=model)
    return pydantic_type(model).schema_json()
