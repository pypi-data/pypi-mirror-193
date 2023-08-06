"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserCheckins
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserCheckinsInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserCheckins
    Note:
        Model Depth 4
    Attributes:
    """


class UserCheckinsProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserCheckins
    Note:
        Model Depth 4
    Attributes:
    """


class UserCheckinsAllProperties(
    UserCheckinsInheritedProperties, UserCheckinsProperties, TypedDict
):
    pass


class UserCheckinsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserCheckins", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UserCheckinsProperties,
        UserCheckinsInheritedProperties,
        UserCheckinsAllProperties,
    ] = UserCheckinsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserCheckins"
    return model


UserCheckins = create_schema_org_model()


def create_usercheckins_model(
    model: Union[
        UserCheckinsProperties,
        UserCheckinsInheritedProperties,
        UserCheckinsAllProperties,
    ]
):
    _type = deepcopy(UserCheckinsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UserCheckinsAllProperties):
    pydantic_type = create_usercheckins_model(model=model)
    return pydantic_type(model).schema_json()
