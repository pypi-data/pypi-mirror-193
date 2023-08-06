"""
The payment has been received and processed.

https://schema.org/PaymentComplete
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(PaymentCompleteInheritedProperties , PaymentCompleteProperties, TypedDict):
    pass


class PaymentCompleteBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PaymentComplete",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PaymentCompleteProperties, PaymentCompleteInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentComplete"
    return model
    

PaymentComplete = create_schema_org_model()


def create_paymentcomplete_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_paymentcomplete_model(model=model)
    return pydantic_type(model).schema_json()


