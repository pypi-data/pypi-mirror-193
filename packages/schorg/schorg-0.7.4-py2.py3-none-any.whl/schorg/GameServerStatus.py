"""
Status of a game server.

https://schema.org/GameServerStatus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GameServerStatusInheritedProperties(TypedDict):
    """Status of a game server.

    References:
        https://schema.org/GameServerStatus
    Note:
        Model Depth 5
    Attributes:
    """


class GameServerStatusProperties(TypedDict):
    """Status of a game server.

    References:
        https://schema.org/GameServerStatus
    Note:
        Model Depth 5
    Attributes:
    """


class GameServerStatusAllProperties(
    GameServerStatusInheritedProperties, GameServerStatusProperties, TypedDict
):
    pass


class GameServerStatusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GameServerStatus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GameServerStatusProperties,
        GameServerStatusInheritedProperties,
        GameServerStatusAllProperties,
    ] = GameServerStatusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GameServerStatus"
    return model


GameServerStatus = create_schema_org_model()


def create_gameserverstatus_model(
    model: Union[
        GameServerStatusProperties,
        GameServerStatusInheritedProperties,
        GameServerStatusAllProperties,
    ]
):
    _type = deepcopy(GameServerStatusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of GameServerStatusAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GameServerStatusAllProperties):
    pydantic_type = create_gameserverstatus_model(model=model)
    return pydantic_type(model).schema_json()
