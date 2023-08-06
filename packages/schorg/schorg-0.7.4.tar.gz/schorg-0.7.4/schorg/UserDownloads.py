"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserDownloads
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserDownloadsInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserDownloads
    Note:
        Model Depth 4
    Attributes:
    """


class UserDownloadsProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserDownloads
    Note:
        Model Depth 4
    Attributes:
    """


class UserDownloadsAllProperties(
    UserDownloadsInheritedProperties, UserDownloadsProperties, TypedDict
):
    pass


class UserDownloadsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserDownloads", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UserDownloadsProperties,
        UserDownloadsInheritedProperties,
        UserDownloadsAllProperties,
    ] = UserDownloadsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserDownloads"
    return model


UserDownloads = create_schema_org_model()


def create_userdownloads_model(
    model: Union[
        UserDownloadsProperties,
        UserDownloadsInheritedProperties,
        UserDownloadsAllProperties,
    ]
):
    _type = deepcopy(UserDownloadsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of UserDownloadsAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UserDownloadsAllProperties):
    pydantic_type = create_userdownloads_model(model=model)
    return pydantic_type(model).schema_json()
