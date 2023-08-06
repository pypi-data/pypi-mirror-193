"""
Play mode: SinglePlayer. Which is played by a lone player.

https://schema.org/SinglePlayer
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(SinglePlayerInheritedProperties , SinglePlayerProperties, TypedDict):
    pass


class SinglePlayerBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SinglePlayer",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SinglePlayerProperties, SinglePlayerInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SinglePlayer"
    return model
    

SinglePlayer = create_schema_org_model()


def create_singleplayer_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_singleplayer_model(model=model)
    return pydantic_type(model).schema_json()


