"""
A specific payment status. For example, PaymentDue, PaymentComplete, etc.

https://schema.org/PaymentStatusType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentStatusTypeInheritedProperties(TypedDict):
    """A specific payment status. For example, PaymentDue, PaymentComplete, etc.

    References:
        https://schema.org/PaymentStatusType
    Note:
        Model Depth 5
    Attributes:
    """


class PaymentStatusTypeProperties(TypedDict):
    """A specific payment status. For example, PaymentDue, PaymentComplete, etc.

    References:
        https://schema.org/PaymentStatusType
    Note:
        Model Depth 5
    Attributes:
    """


class PaymentStatusTypeAllProperties(
    PaymentStatusTypeInheritedProperties, PaymentStatusTypeProperties, TypedDict
):
    pass


class PaymentStatusTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentStatusType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PaymentStatusTypeProperties,
        PaymentStatusTypeInheritedProperties,
        PaymentStatusTypeAllProperties,
    ] = PaymentStatusTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentStatusType"
    return model


PaymentStatusType = create_schema_org_model()


def create_paymentstatustype_model(
    model: Union[
        PaymentStatusTypeProperties,
        PaymentStatusTypeInheritedProperties,
        PaymentStatusTypeAllProperties,
    ]
):
    _type = deepcopy(PaymentStatusTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PaymentStatusType. Please see: https://schema.org/PaymentStatusType"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PaymentStatusTypeAllProperties):
    pydantic_type = create_paymentstatustype_model(model=model)
    return pydantic_type(model).schema_json()
