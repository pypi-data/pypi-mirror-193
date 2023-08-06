"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserTweets
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserTweetsInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserTweets
    Note:
        Model Depth 4
    Attributes:
    """


class UserTweetsProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserTweets
    Note:
        Model Depth 4
    Attributes:
    """


class UserTweetsAllProperties(
    UserTweetsInheritedProperties, UserTweetsProperties, TypedDict
):
    pass


class UserTweetsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserTweets", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UserTweetsProperties, UserTweetsInheritedProperties, UserTweetsAllProperties
    ] = UserTweetsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserTweets"
    return model


UserTweets = create_schema_org_model()


def create_usertweets_model(
    model: Union[
        UserTweetsProperties, UserTweetsInheritedProperties, UserTweetsAllProperties
    ]
):
    _type = deepcopy(UserTweetsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of UserTweetsAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UserTweetsAllProperties):
    pydantic_type = create_usertweets_model(model=model)
    return pydantic_type(model).schema_json()
