"""
A posting to a discussion forum.

https://schema.org/DiscussionForumPosting
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DiscussionForumPostingInheritedProperties(TypedDict):
    """A posting to a discussion forum.

    References:
        https://schema.org/DiscussionForumPosting
    Note:
        Model Depth 5
    Attributes:
        sharedContent: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A CreativeWork such as an image, video, or audio clip shared as part of this posting.
    """

    sharedContent: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class DiscussionForumPostingProperties(TypedDict):
    """A posting to a discussion forum.

    References:
        https://schema.org/DiscussionForumPosting
    Note:
        Model Depth 5
    Attributes:
    """


class DiscussionForumPostingAllProperties(
    DiscussionForumPostingInheritedProperties,
    DiscussionForumPostingProperties,
    TypedDict,
):
    pass


class DiscussionForumPostingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DiscussionForumPosting", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"sharedContent": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DiscussionForumPostingProperties,
        DiscussionForumPostingInheritedProperties,
        DiscussionForumPostingAllProperties,
    ] = DiscussionForumPostingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DiscussionForumPosting"
    return model


DiscussionForumPosting = create_schema_org_model()


def create_discussionforumposting_model(
    model: Union[
        DiscussionForumPostingProperties,
        DiscussionForumPostingInheritedProperties,
        DiscussionForumPostingAllProperties,
    ]
):
    _type = deepcopy(DiscussionForumPostingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DiscussionForumPostingAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DiscussionForumPostingAllProperties):
    pydantic_type = create_discussionforumposting_model(model=model)
    return pydantic_type(model).schema_json()
