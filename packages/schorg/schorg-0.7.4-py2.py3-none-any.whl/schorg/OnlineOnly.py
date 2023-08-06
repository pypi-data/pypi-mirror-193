"""
Indicates that the item is available only online.

https://schema.org/OnlineOnly
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnlineOnlyInheritedProperties(TypedDict):
    """Indicates that the item is available only online.

    References:
        https://schema.org/OnlineOnly
    Note:
        Model Depth 5
    Attributes:
    """


class OnlineOnlyProperties(TypedDict):
    """Indicates that the item is available only online.

    References:
        https://schema.org/OnlineOnly
    Note:
        Model Depth 5
    Attributes:
    """


class OnlineOnlyAllProperties(
    OnlineOnlyInheritedProperties, OnlineOnlyProperties, TypedDict
):
    pass


class OnlineOnlyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OnlineOnly", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OnlineOnlyProperties, OnlineOnlyInheritedProperties, OnlineOnlyAllProperties
    ] = OnlineOnlyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnlineOnly"
    return model


OnlineOnly = create_schema_org_model()


def create_onlineonly_model(
    model: Union[
        OnlineOnlyProperties, OnlineOnlyInheritedProperties, OnlineOnlyAllProperties
    ]
):
    _type = deepcopy(OnlineOnlyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OnlineOnlyAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OnlineOnlyAllProperties):
    pydantic_type = create_onlineonly_model(model=model)
    return pydantic_type(model).schema_json()
