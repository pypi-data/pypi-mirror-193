"""
A specific payment status. For example, PaymentDue, PaymentComplete, etc.

https://schema.org/PaymentStatusType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(PaymentStatusTypeInheritedProperties , PaymentStatusTypeProperties, TypedDict):
    pass


class PaymentStatusTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="PaymentStatusType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[PaymentStatusTypeProperties, PaymentStatusTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PaymentStatusType"
    return model
    

PaymentStatusType = create_schema_org_model()


def create_paymentstatustype_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_paymentstatustype_model(model=model)
    return pydantic_type(model).schema_json()


