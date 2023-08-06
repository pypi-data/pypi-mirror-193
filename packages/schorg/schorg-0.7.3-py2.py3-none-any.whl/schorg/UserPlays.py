"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserPlays
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserPlaysInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserPlays
    Note:
        Model Depth 4
    Attributes:
    """


class UserPlaysProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserPlays
    Note:
        Model Depth 4
    Attributes:
    """


class UserPlaysAllProperties(
    UserPlaysInheritedProperties, UserPlaysProperties, TypedDict
):
    pass


class UserPlaysBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserPlays", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UserPlaysProperties, UserPlaysInheritedProperties, UserPlaysAllProperties
    ] = UserPlaysAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserPlays"
    return model


UserPlays = create_schema_org_model()


def create_userplays_model(
    model: Union[
        UserPlaysProperties, UserPlaysInheritedProperties, UserPlaysAllProperties
    ]
):
    _type = deepcopy(UserPlaysAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UserPlaysAllProperties):
    pydantic_type = create_userplays_model(model=model)
    return pydantic_type(model).schema_json()
