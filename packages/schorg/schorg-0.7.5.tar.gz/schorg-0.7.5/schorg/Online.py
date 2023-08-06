"""
Game server status: Online. Server is available.

https://schema.org/Online
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OnlineInheritedProperties(TypedDict):
    """Game server status: Online. Server is available.

    References:
        https://schema.org/Online
    Note:
        Model Depth 6
    Attributes:
    """


class OnlineProperties(TypedDict):
    """Game server status: Online. Server is available.

    References:
        https://schema.org/Online
    Note:
        Model Depth 6
    Attributes:
    """


class OnlineAllProperties(OnlineInheritedProperties, OnlineProperties, TypedDict):
    pass


class OnlineBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Online", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OnlineProperties, OnlineInheritedProperties, OnlineAllProperties
    ] = OnlineAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Online"
    return model


Online = create_schema_org_model()


def create_online_model(
    model: Union[OnlineProperties, OnlineInheritedProperties, OnlineAllProperties]
):
    _type = deepcopy(OnlineAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Online. Please see: https://schema.org/Online"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: OnlineAllProperties):
    pydantic_type = create_online_model(model=model)
    return pydantic_type(model).schema_json()
