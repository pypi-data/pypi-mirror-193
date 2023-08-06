"""
Play mode: SinglePlayer. Which is played by a lone player.

https://schema.org/SinglePlayer
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SinglePlayerInheritedProperties(TypedDict):
    """Play mode: SinglePlayer. Which is played by a lone player.

    References:
        https://schema.org/SinglePlayer
    Note:
        Model Depth 5
    Attributes:
    """


class SinglePlayerProperties(TypedDict):
    """Play mode: SinglePlayer. Which is played by a lone player.

    References:
        https://schema.org/SinglePlayer
    Note:
        Model Depth 5
    Attributes:
    """


class SinglePlayerAllProperties(
    SinglePlayerInheritedProperties, SinglePlayerProperties, TypedDict
):
    pass


class SinglePlayerBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SinglePlayer", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SinglePlayerProperties,
        SinglePlayerInheritedProperties,
        SinglePlayerAllProperties,
    ] = SinglePlayerAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SinglePlayer"
    return model


SinglePlayer = create_schema_org_model()


def create_singleplayer_model(
    model: Union[
        SinglePlayerProperties,
        SinglePlayerInheritedProperties,
        SinglePlayerAllProperties,
    ]
):
    _type = deepcopy(SinglePlayerAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SinglePlayerAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SinglePlayerAllProperties):
    pydantic_type = create_singleplayer_model(model=model)
    return pydantic_type(model).schema_json()
