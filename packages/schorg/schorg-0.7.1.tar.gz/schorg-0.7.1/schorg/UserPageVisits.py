"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserPageVisits
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(UserPageVisitsInheritedProperties , UserPageVisitsProperties, TypedDict):
    pass


class UserPageVisitsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="UserPageVisits",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[UserPageVisitsProperties, UserPageVisitsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserPageVisits"
    return model
    

UserPageVisits = create_schema_org_model()


def create_userpagevisits_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_userpagevisits_model(model=model)
    return pydantic_type(model).schema_json()


