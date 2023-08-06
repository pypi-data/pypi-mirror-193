"""
A DeliveryMethod in which an item is made available via locker.

https://schema.org/LockerDelivery
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class LockerDeliveryAllProperties(
    LockerDeliveryInheritedProperties, LockerDeliveryProperties, TypedDict
):
    pass


class LockerDeliveryBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LockerDelivery", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LockerDeliveryProperties,
        LockerDeliveryInheritedProperties,
        LockerDeliveryAllProperties,
    ] = LockerDeliveryAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LockerDelivery"
    return model


LockerDelivery = create_schema_org_model()


def create_lockerdelivery_model(
    model: Union[
        LockerDeliveryProperties,
        LockerDeliveryInheritedProperties,
        LockerDeliveryAllProperties,
    ]
):
    _type = deepcopy(LockerDeliveryAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of LockerDelivery. Please see: https://schema.org/LockerDelivery"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: LockerDeliveryAllProperties):
    pydantic_type = create_lockerdelivery_model(model=model)
    return pydantic_type(model).schema_json()
