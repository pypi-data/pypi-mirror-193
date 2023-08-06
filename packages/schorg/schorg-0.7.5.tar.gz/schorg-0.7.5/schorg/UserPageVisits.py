"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserPageVisits
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserPageVisitsInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserPageVisits
    Note:
        Model Depth 4
    Attributes:
    """


class UserPageVisitsProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserPageVisits
    Note:
        Model Depth 4
    Attributes:
    """


class UserPageVisitsAllProperties(
    UserPageVisitsInheritedProperties, UserPageVisitsProperties, TypedDict
):
    pass


class UserPageVisitsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserPageVisits", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UserPageVisitsProperties,
        UserPageVisitsInheritedProperties,
        UserPageVisitsAllProperties,
    ] = UserPageVisitsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserPageVisits"
    return model


UserPageVisits = create_schema_org_model()


def create_userpagevisits_model(
    model: Union[
        UserPageVisitsProperties,
        UserPageVisitsInheritedProperties,
        UserPageVisitsAllProperties,
    ]
):
    _type = deepcopy(UserPageVisitsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of UserPageVisits. Please see: https://schema.org/UserPageVisits"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: UserPageVisitsAllProperties):
    pydantic_type = create_userpagevisits_model(model=model)
    return pydantic_type(model).schema_json()
