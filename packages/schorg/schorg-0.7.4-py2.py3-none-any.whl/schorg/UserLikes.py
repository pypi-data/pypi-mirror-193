"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserLikes
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserLikesInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserLikes
    Note:
        Model Depth 4
    Attributes:
    """


class UserLikesProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserLikes
    Note:
        Model Depth 4
    Attributes:
    """


class UserLikesAllProperties(
    UserLikesInheritedProperties, UserLikesProperties, TypedDict
):
    pass


class UserLikesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserLikes", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UserLikesProperties, UserLikesInheritedProperties, UserLikesAllProperties
    ] = UserLikesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserLikes"
    return model


UserLikes = create_schema_org_model()


def create_userlikes_model(
    model: Union[
        UserLikesProperties, UserLikesInheritedProperties, UserLikesAllProperties
    ]
):
    _type = deepcopy(UserLikesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of UserLikesAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UserLikesAllProperties):
    pydantic_type = create_userlikes_model(model=model)
    return pydantic_type(model).schema_json()
