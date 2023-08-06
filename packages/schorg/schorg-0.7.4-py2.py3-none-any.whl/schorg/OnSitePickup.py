"""
A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.

https://schema.org/OnSitePickup
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnSitePickupInheritedProperties(TypedDict):
    """A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.

    References:
        https://schema.org/OnSitePickup
    Note:
        Model Depth 5
    Attributes:
    """


class OnSitePickupProperties(TypedDict):
    """A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.

    References:
        https://schema.org/OnSitePickup
    Note:
        Model Depth 5
    Attributes:
    """


class OnSitePickupAllProperties(
    OnSitePickupInheritedProperties, OnSitePickupProperties, TypedDict
):
    pass


class OnSitePickupBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OnSitePickup", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OnSitePickupProperties,
        OnSitePickupInheritedProperties,
        OnSitePickupAllProperties,
    ] = OnSitePickupAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnSitePickup"
    return model


OnSitePickup = create_schema_org_model()


def create_onsitepickup_model(
    model: Union[
        OnSitePickupProperties,
        OnSitePickupInheritedProperties,
        OnSitePickupAllProperties,
    ]
):
    _type = deepcopy(OnSitePickupAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OnSitePickupAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OnSitePickupAllProperties):
    pydantic_type = create_onsitepickup_model(model=model)
    return pydantic_type(model).schema_json()
