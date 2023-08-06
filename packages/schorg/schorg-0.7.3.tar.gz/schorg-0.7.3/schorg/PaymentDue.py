"""
The payment is due, but still within an acceptable time to be received.

https://schema.org/PaymentDue
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentDueInheritedProperties(TypedDict):
    """The payment is due, but still within an acceptable time to be received.

    References:
        https://schema.org/PaymentDue
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentDueProperties(TypedDict):
    """The payment is due, but still within an acceptable time to be received.

    References:
        https://schema.org/PaymentDue
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentDueAllProperties(
    PaymentDueInheritedProperties, PaymentDueProperties, TypedDict
):
    pass


class PaymentDueBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentDue", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PaymentDueProperties, PaymentDueInheritedProperties, PaymentDueAllProperties
    ] = PaymentDueAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentDue"
    return model


PaymentDue = create_schema_org_model()


def create_paymentdue_model(
    model: Union[
        PaymentDueProperties, PaymentDueInheritedProperties, PaymentDueAllProperties
    ]
):
    _type = deepcopy(PaymentDueAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PaymentDueAllProperties):
    pydantic_type = create_paymentdue_model(model=model)
    return pydantic_type(model).schema_json()
