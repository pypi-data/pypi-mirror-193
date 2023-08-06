"""
Content coded 'staged content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'staged content': A video that has been created using actors or similarly contrived.For an [[ImageObject]] to be 'staged content': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.For an [[ImageObject]] with embedded text to be 'staged content': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.For an [[AudioObject]] to be 'staged content': Audio that has been created using actors or similarly contrived.

https://schema.org/StagedContent
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class StagedContentInheritedProperties(TypedDict):
    """Content coded 'staged content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'staged content': A video that has been created using actors or similarly contrived.For an [[ImageObject]] to be 'staged content': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.For an [[ImageObject]] with embedded text to be 'staged content': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.For an [[AudioObject]] to be 'staged content': Audio that has been created using actors or similarly contrived.

    References:
        https://schema.org/StagedContent
    Note:
        Model Depth 5
    Attributes:
    """


class StagedContentProperties(TypedDict):
    """Content coded 'staged content' in a [[MediaReview]], considered in the context of how it was published or shared.For a [[VideoObject]] to be 'staged content': A video that has been created using actors or similarly contrived.For an [[ImageObject]] to be 'staged content': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.For an [[ImageObject]] with embedded text to be 'staged content': An image that was created using actors or similarly contrived, such as a screenshot of a fake tweet.For an [[AudioObject]] to be 'staged content': Audio that has been created using actors or similarly contrived.

    References:
        https://schema.org/StagedContent
    Note:
        Model Depth 5
    Attributes:
    """


class StagedContentAllProperties(
    StagedContentInheritedProperties, StagedContentProperties, TypedDict
):
    pass


class StagedContentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="StagedContent", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        StagedContentProperties,
        StagedContentInheritedProperties,
        StagedContentAllProperties,
    ] = StagedContentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "StagedContent"
    return model


StagedContent = create_schema_org_model()


def create_stagedcontent_model(
    model: Union[
        StagedContentProperties,
        StagedContentInheritedProperties,
        StagedContentAllProperties,
    ]
):
    _type = deepcopy(StagedContentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: StagedContentAllProperties):
    pydantic_type = create_stagedcontent_model(model=model)
    return pydantic_type(model).schema_json()
