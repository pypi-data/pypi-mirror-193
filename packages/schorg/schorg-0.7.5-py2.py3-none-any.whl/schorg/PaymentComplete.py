"""
The payment has been received and processed.

https://schema.org/PaymentComplete
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentCompleteInheritedProperties(TypedDict):
    """The payment has been received and processed.

    References:
        https://schema.org/PaymentComplete
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentCompleteProperties(TypedDict):
    """The payment has been received and processed.

    References:
        https://schema.org/PaymentComplete
    Note:
        Model Depth 6
    Attributes:
    """


class PaymentCompleteAllProperties(
    PaymentCompleteInheritedProperties, PaymentCompleteProperties, TypedDict
):
    pass


class PaymentCompleteBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentComplete", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PaymentCompleteProperties,
        PaymentCompleteInheritedProperties,
        PaymentCompleteAllProperties,
    ] = PaymentCompleteAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentComplete"
    return model


PaymentComplete = create_schema_org_model()


def create_paymentcomplete_model(
    model: Union[
        PaymentCompleteProperties,
        PaymentCompleteInheritedProperties,
        PaymentCompleteAllProperties,
    ]
):
    _type = deepcopy(PaymentCompleteAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PaymentComplete. Please see: https://schema.org/PaymentComplete"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PaymentCompleteAllProperties):
    pydantic_type = create_paymentcomplete_model(model=model)
    return pydantic_type(model).schema_json()
