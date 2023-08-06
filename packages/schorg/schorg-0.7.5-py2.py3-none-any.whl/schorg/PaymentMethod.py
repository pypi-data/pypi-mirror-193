"""
A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction.Commonly used values:* http://purl.org/goodrelations/v1#ByBankTransferInAdvance* http://purl.org/goodrelations/v1#ByInvoice* http://purl.org/goodrelations/v1#Cash* http://purl.org/goodrelations/v1#CheckInAdvance* http://purl.org/goodrelations/v1#COD* http://purl.org/goodrelations/v1#DirectDebit* http://purl.org/goodrelations/v1#GoogleCheckout* http://purl.org/goodrelations/v1#PayPal* http://purl.org/goodrelations/v1#PaySwarm        

https://schema.org/PaymentMethod
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PaymentMethodInheritedProperties(TypedDict):
    """A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction.Commonly used values:* http://purl.org/goodrelations/v1#ByBankTransferInAdvance* http://purl.org/goodrelations/v1#ByInvoice* http://purl.org/goodrelations/v1#Cash* http://purl.org/goodrelations/v1#CheckInAdvance* http://purl.org/goodrelations/v1#COD* http://purl.org/goodrelations/v1#DirectDebit* http://purl.org/goodrelations/v1#GoogleCheckout* http://purl.org/goodrelations/v1#PayPal* http://purl.org/goodrelations/v1#PaySwarm

    References:
        https://schema.org/PaymentMethod
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class PaymentMethodProperties(TypedDict):
    """A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction.Commonly used values:* http://purl.org/goodrelations/v1#ByBankTransferInAdvance* http://purl.org/goodrelations/v1#ByInvoice* http://purl.org/goodrelations/v1#Cash* http://purl.org/goodrelations/v1#CheckInAdvance* http://purl.org/goodrelations/v1#COD* http://purl.org/goodrelations/v1#DirectDebit* http://purl.org/goodrelations/v1#GoogleCheckout* http://purl.org/goodrelations/v1#PayPal* http://purl.org/goodrelations/v1#PaySwarm

    References:
        https://schema.org/PaymentMethod
    Note:
        Model Depth 4
    Attributes:
    """


class PaymentMethodAllProperties(
    PaymentMethodInheritedProperties, PaymentMethodProperties, TypedDict
):
    pass


class PaymentMethodBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PaymentMethod", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        PaymentMethodProperties,
        PaymentMethodInheritedProperties,
        PaymentMethodAllProperties,
    ] = PaymentMethodAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentMethod"
    return model


PaymentMethod = create_schema_org_model()


def create_paymentmethod_model(
    model: Union[
        PaymentMethodProperties,
        PaymentMethodInheritedProperties,
        PaymentMethodAllProperties,
    ]
):
    _type = deepcopy(PaymentMethodAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of PaymentMethod. Please see: https://schema.org/PaymentMethod"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: PaymentMethodAllProperties):
    pydantic_type = create_paymentmethod_model(model=model)
    return pydantic_type(model).schema_json()
