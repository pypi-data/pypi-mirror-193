"""
Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.

https://schema.org/OnlineFull
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnlineFullInheritedProperties(TypedDict):
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.

    References:
        https://schema.org/OnlineFull
    Note:
        Model Depth 6
    Attributes:
    """


class OnlineFullProperties(TypedDict):
    """Game server status: OnlineFull. Server is online but unavailable. The maximum number of players has reached.

    References:
        https://schema.org/OnlineFull
    Note:
        Model Depth 6
    Attributes:
    """


class OnlineFullAllProperties(
    OnlineFullInheritedProperties, OnlineFullProperties, TypedDict
):
    pass


class OnlineFullBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OnlineFull", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OnlineFullProperties, OnlineFullInheritedProperties, OnlineFullAllProperties
    ] = OnlineFullAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OnlineFull"
    return model


OnlineFull = create_schema_org_model()


def create_onlinefull_model(
    model: Union[
        OnlineFullProperties, OnlineFullInheritedProperties, OnlineFullAllProperties
    ]
):
    _type = deepcopy(OnlineFullAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of OnlineFullAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OnlineFullAllProperties):
    pydantic_type = create_onlinefull_model(model=model)
    return pydantic_type(model).schema_json()
