"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserPlusOnes
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserPlusOnesInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserPlusOnes
    Note:
        Model Depth 4
    Attributes:
    """


class UserPlusOnesProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserPlusOnes
    Note:
        Model Depth 4
    Attributes:
    """


class UserPlusOnesAllProperties(
    UserPlusOnesInheritedProperties, UserPlusOnesProperties, TypedDict
):
    pass


class UserPlusOnesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserPlusOnes", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UserPlusOnesProperties,
        UserPlusOnesInheritedProperties,
        UserPlusOnesAllProperties,
    ] = UserPlusOnesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserPlusOnes"
    return model


UserPlusOnes = create_schema_org_model()


def create_userplusones_model(
    model: Union[
        UserPlusOnesProperties,
        UserPlusOnesInheritedProperties,
        UserPlusOnesAllProperties,
    ]
):
    _type = deepcopy(UserPlusOnesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UserPlusOnesAllProperties):
    pydantic_type = create_userplusones_model(model=model)
    return pydantic_type(model).schema_json()
