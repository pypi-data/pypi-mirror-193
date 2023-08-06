"""
A music store.

https://schema.org/MusicStore
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MusicStoreInheritedProperties(TypedDict):
    """A music store.

    References:
        https://schema.org/MusicStore
    Note:
        Model Depth 5
    Attributes:
    """


class MusicStoreProperties(TypedDict):
    """A music store.

    References:
        https://schema.org/MusicStore
    Note:
        Model Depth 5
    Attributes:
    """


class MusicStoreAllProperties(
    MusicStoreInheritedProperties, MusicStoreProperties, TypedDict
):
    pass


class MusicStoreBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MusicStore", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MusicStoreProperties, MusicStoreInheritedProperties, MusicStoreAllProperties
    ] = MusicStoreAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MusicStore"
    return model


MusicStore = create_schema_org_model()


def create_musicstore_model(
    model: Union[
        MusicStoreProperties, MusicStoreInheritedProperties, MusicStoreAllProperties
    ]
):
    _type = deepcopy(MusicStoreAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MusicStoreAllProperties):
    pydantic_type = create_musicstore_model(model=model)
    return pydantic_type(model).schema_json()
