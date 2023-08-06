"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserDownloads
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(UserDownloadsInheritedProperties , UserDownloadsProperties, TypedDict):
    pass


class UserDownloadsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="UserDownloads",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[UserDownloadsProperties, UserDownloadsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserDownloads"
    return model
    

UserDownloads = create_schema_org_model()


def create_userdownloads_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_userdownloads_model(model=model)
    return pydantic_type(model).schema_json()


