"""
Indicates whether this game is multi-player, co-op or single-player.

https://schema.org/GamePlayMode
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GamePlayModeInheritedProperties(TypedDict):
    """Indicates whether this game is multi-player, co-op or single-player.

    References:
        https://schema.org/GamePlayMode
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class GamePlayModeProperties(TypedDict):
    """Indicates whether this game is multi-player, co-op or single-player.

    References:
        https://schema.org/GamePlayMode
    Note:
        Model Depth 4
    Attributes:
    """


class GamePlayModeAllProperties(
    GamePlayModeInheritedProperties, GamePlayModeProperties, TypedDict
):
    pass


class GamePlayModeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GamePlayMode", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        GamePlayModeProperties,
        GamePlayModeInheritedProperties,
        GamePlayModeAllProperties,
    ] = GamePlayModeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GamePlayMode"
    return model


GamePlayMode = create_schema_org_model()


def create_gameplaymode_model(
    model: Union[
        GamePlayModeProperties,
        GamePlayModeInheritedProperties,
        GamePlayModeAllProperties,
    ]
):
    _type = deepcopy(GamePlayModeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of GamePlayModeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GamePlayModeAllProperties):
    pydantic_type = create_gameplaymode_model(model=model)
    return pydantic_type(model).schema_json()
