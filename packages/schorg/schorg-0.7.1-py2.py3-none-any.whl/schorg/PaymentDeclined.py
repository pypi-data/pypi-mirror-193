"""
The payee received the payment, but it was declined for some reason.

https://schema.org/PaymentDeclined
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(PaymentDeclinedInheritedProperties , PaymentDeclinedProperties, TypedDict):
    pass


class PaymentDeclinedBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PaymentDeclined",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PaymentDeclinedProperties, PaymentDeclinedInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentDeclined"
    return model
    

PaymentDeclined = create_schema_org_model()


def create_paymentdeclined_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_paymentdeclined_model(model=model)
    return pydantic_type(model).schema_json()


