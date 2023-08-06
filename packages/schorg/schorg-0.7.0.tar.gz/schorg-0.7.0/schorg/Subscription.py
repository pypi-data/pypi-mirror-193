"""
Represents the subscription pricing component of the total price for an offered product.

https://schema.org/Subscription
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SubscriptionInheritedProperties(TypedDict):
    """Represents the subscription pricing component of the total price for an offered product.

    References:
        https://schema.org/Subscription
    Note:
        Model Depth 5
    Attributes:
    """

    


class SubscriptionProperties(TypedDict):
    """Represents the subscription pricing component of the total price for an offered product.

    References:
        https://schema.org/Subscription
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SubscriptionInheritedProperties , SubscriptionProperties, TypedDict):
    pass


class SubscriptionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Subscription",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SubscriptionProperties, SubscriptionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Subscription"
    return model
    

Subscription = create_schema_org_model()


def create_subscription_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_subscription_model(model=model)
    return pydantic_type(model).schema_json()


