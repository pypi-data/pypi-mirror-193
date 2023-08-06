"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserBlocks
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserBlocksInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserBlocks
    Note:
        Model Depth 4
    Attributes:
    """


class UserBlocksProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserBlocks
    Note:
        Model Depth 4
    Attributes:
    """


class UserBlocksAllProperties(
    UserBlocksInheritedProperties, UserBlocksProperties, TypedDict
):
    pass


class UserBlocksBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserBlocks", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UserBlocksProperties, UserBlocksInheritedProperties, UserBlocksAllProperties
    ] = UserBlocksAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserBlocks"
    return model


UserBlocks = create_schema_org_model()


def create_userblocks_model(
    model: Union[
        UserBlocksProperties, UserBlocksInheritedProperties, UserBlocksAllProperties
    ]
):
    _type = deepcopy(UserBlocksAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UserBlocksAllProperties):
    pydantic_type = create_userblocks_model(model=model)
    return pydantic_type(model).schema_json()
