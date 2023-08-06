"""
An eCommerce site.

https://schema.org/OnlineStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnlineStoreInheritedProperties(TypedDict):
    """An eCommerce site.

    References:
        https://schema.org/OnlineStore
    Note:
        Model Depth 4
    Attributes:
    """


class OnlineStoreProperties(TypedDict):
    """An eCommerce site.

    References:
        https://schema.org/OnlineStore
    Note:
        Model Depth 4
    Attributes:
    """


class OnlineStoreAllProperties(
    OnlineStoreInheritedProperties, OnlineStoreProperties, TypedDict
):
    pass


class OnlineStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OnlineStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OnlineStoreProperties, OnlineStoreInheritedProperties, OnlineStoreAllProperties
    ] = OnlineStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnlineStore"
    return model


OnlineStore = create_schema_org_model()


def create_onlinestore_model(
    model: Union[
        OnlineStoreProperties, OnlineStoreInheritedProperties, OnlineStoreAllProperties
    ]
):
    _type = deepcopy(OnlineStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OnlineStoreAllProperties):
    pydantic_type = create_onlinestore_model(model=model)
    return pydantic_type(model).schema_json()
