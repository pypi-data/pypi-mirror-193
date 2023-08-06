"""
Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.

https://schema.org/MultiPlayer
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MultiPlayerInheritedProperties(TypedDict):
    """Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.

    References:
        https://schema.org/MultiPlayer
    Note:
        Model Depth 5
    Attributes:
    """

    


class MultiPlayerProperties(TypedDict):
    """Play mode: MultiPlayer. Requiring or allowing multiple human players to play simultaneously.

    References:
        https://schema.org/MultiPlayer
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MultiPlayerInheritedProperties , MultiPlayerProperties, TypedDict):
    pass


class MultiPlayerBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MultiPlayer",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MultiPlayerProperties, MultiPlayerInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MultiPlayer"
    return model
    

MultiPlayer = create_schema_org_model()


def create_multiplayer_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_multiplayer_model(model=model)
    return pydantic_type(model).schema_json()


