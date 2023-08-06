"""
A DeliveryMethod in which an item is made available via locker.

https://schema.org/LockerDelivery
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LockerDeliveryInheritedProperties(TypedDict):
    """A DeliveryMethod in which an item is made available via locker.

    References:
        https://schema.org/LockerDelivery
    Note:
        Model Depth 5
    Attributes:
    """

    


class LockerDeliveryProperties(TypedDict):
    """A DeliveryMethod in which an item is made available via locker.

    References:
        https://schema.org/LockerDelivery
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(LockerDeliveryInheritedProperties , LockerDeliveryProperties, TypedDict):
    pass


class LockerDeliveryBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LockerDelivery",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LockerDeliveryProperties, LockerDeliveryInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LockerDelivery"
    return model
    

LockerDelivery = create_schema_org_model()


def create_lockerdelivery_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_lockerdelivery_model(model=model)
    return pydantic_type(model).schema_json()


