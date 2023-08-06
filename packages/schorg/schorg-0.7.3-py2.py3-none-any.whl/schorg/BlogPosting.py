"""
A blog post.

https://schema.org/BlogPosting
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BlogPostingInheritedProperties(TypedDict):
    """A blog post.

    References:
        https://schema.org/BlogPosting
    Note:
        Model Depth 5
    Attributes:
        sharedContent: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A CreativeWork such as an image, video, or audio clip shared as part of this posting.
    """

    sharedContent: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class BlogPostingProperties(TypedDict):
    """A blog post.

    References:
        https://schema.org/BlogPosting
    Note:
        Model Depth 5
    Attributes:
    """


class BlogPostingAllProperties(
    BlogPostingInheritedProperties, BlogPostingProperties, TypedDict
):
    pass


class BlogPostingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BlogPosting", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"sharedContent": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        BlogPostingProperties, BlogPostingInheritedProperties, BlogPostingAllProperties
    ] = BlogPostingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BlogPosting"
    return model


BlogPosting = create_schema_org_model()


def create_blogposting_model(
    model: Union[
        BlogPostingProperties, BlogPostingInheritedProperties, BlogPostingAllProperties
    ]
):
    _type = deepcopy(BlogPostingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BlogPostingAllProperties):
    pydantic_type = create_blogposting_model(model=model)
    return pydantic_type(model).schema_json()
