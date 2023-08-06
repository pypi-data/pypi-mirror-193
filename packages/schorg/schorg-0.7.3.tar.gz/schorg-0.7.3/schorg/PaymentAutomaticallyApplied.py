"""
An automatic payment system is in place and will be used.

https://schema.org/PaymentAutomaticallyApplied
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentAutomaticallyAppliedInheritedProperties(TypedDict):
    """An automatic payment system is in place and will be used.

    References:
        https://schema.org/PaymentAutomaticallyApplied
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentAutomaticallyAppliedProperties(TypedDict):
    """An automatic payment system is in place and will be used.

    References:
        https://schema.org/PaymentAutomaticallyApplied
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentAutomaticallyAppliedAllProperties(
    PaymentAutomaticallyAppliedInheritedProperties,
    PaymentAutomaticallyAppliedProperties,
    TypedDict,
):
    pass


class PaymentAutomaticallyAppliedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentAutomaticallyApplied", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PaymentAutomaticallyAppliedProperties,
        PaymentAutomaticallyAppliedInheritedProperties,
        PaymentAutomaticallyAppliedAllProperties,
    ] = PaymentAutomaticallyAppliedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentAutomaticallyApplied"
    return model


PaymentAutomaticallyApplied = create_schema_org_model()


def create_paymentautomaticallyapplied_model(
    model: Union[
        PaymentAutomaticallyAppliedProperties,
        PaymentAutomaticallyAppliedInheritedProperties,
        PaymentAutomaticallyAppliedAllProperties,
    ]
):
    _type = deepcopy(PaymentAutomaticallyAppliedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PaymentAutomaticallyAppliedAllProperties):
    pydantic_type = create_paymentautomaticallyapplied_model(model=model)
    return pydantic_type(model).schema_json()
