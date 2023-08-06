"""
A DeliveryMethod in which an item is collected on site, e.g. in a store or at a box office.

https://schema.org/OnSitePickup
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(OnSitePickupInheritedProperties , OnSitePickupProperties, TypedDict):
    pass


class OnSitePickupBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OnSitePickup",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OnSitePickupProperties, OnSitePickupInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnSitePickup"
    return model
    

OnSitePickup = create_schema_org_model()


def create_onsitepickup_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_onsitepickup_model(model=model)
    return pydantic_type(model).schema_json()


