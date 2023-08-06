"""
UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

https://schema.org/UserComments
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UserCommentsInheritedProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserComments
    Note:
        Model Depth 4
    Attributes:
    """


class UserCommentsProperties(TypedDict):
    """UserInteraction and its subtypes is an old way of talking about users interacting with pages. It is generally better to use [[Action]]-based vocabulary, alongside types such as [[Comment]].

    References:
        https://schema.org/UserComments
    Note:
        Model Depth 4
    Attributes:
        commentText: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The text of the UserComment.
        replyToUrl: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): The URL at which a reply may be posted to the specified UserComment.
        creator: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.
        commentTime: (Optional[Union[List[Union[date, datetime, SchemaOrgObj, str]], date, datetime, SchemaOrgObj, str]]): The time at which the UserComment was made.
        discusses: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Specifies the CreativeWork associated with the UserComment.
    """

    commentText: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    replyToUrl: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]
    creator: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    commentTime: NotRequired[
        Union[
            List[Union[date, datetime, SchemaOrgObj, str]],
            date,
            datetime,
            SchemaOrgObj,
            str,
        ]
    ]
    discusses: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class UserCommentsAllProperties(
    UserCommentsInheritedProperties, UserCommentsProperties, TypedDict
):
    pass


class UserCommentsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="UserComments", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"commentText": {"exclude": True}}
        fields = {"replyToUrl": {"exclude": True}}
        fields = {"creator": {"exclude": True}}
        fields = {"commentTime": {"exclude": True}}
        fields = {"discusses": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        UserCommentsProperties,
        UserCommentsInheritedProperties,
        UserCommentsAllProperties,
    ] = UserCommentsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "UserComments"
    return model


UserComments = create_schema_org_model()


def create_usercomments_model(
    model: Union[
        UserCommentsProperties,
        UserCommentsInheritedProperties,
        UserCommentsAllProperties,
    ]
):
    _type = deepcopy(UserCommentsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of UserCommentsAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UserCommentsAllProperties):
    pydantic_type = create_usercomments_model(model=model)
    return pydantic_type(model).schema_json()
