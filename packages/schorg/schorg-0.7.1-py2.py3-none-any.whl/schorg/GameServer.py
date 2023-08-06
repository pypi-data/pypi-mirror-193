"""
Server that provides game interaction in a multiplayer game.

https://schema.org/GameServer
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GameServerInheritedProperties(TypedDict):
    """Server that provides game interaction in a multiplayer game.

    References:
        https://schema.org/GameServer
    Note:
        Model Depth 3
    Attributes:
    """

    


class GameServerProperties(TypedDict):
    """Server that provides game interaction in a multiplayer game.

    References:
        https://schema.org/GameServer
    Note:
        Model Depth 3
    Attributes:
        playersOnline: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): Number of players on the server.
        game: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Video game which is played on this server.
        serverStatus: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Status of a game server.
    """

    playersOnline: NotRequired[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]
    game: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    serverStatus: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(GameServerInheritedProperties , GameServerProperties, TypedDict):
    pass


class GameServerBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GameServer",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'playersOnline': {'exclude': True}}
        fields = {'game': {'exclude': True}}
        fields = {'serverStatus': {'exclude': True}}
        


def create_schema_org_model(type_: Union[GameServerProperties, GameServerInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GameServer"
    return model
    

GameServer = create_schema_org_model()


def create_gameserver_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_gameserver_model(model=model)
    return pydantic_type(model).schema_json()


