"""
A [[comment]] that corrects [[CreativeWork]].

https://schema.org/CorrectionComment
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CorrectionCommentInheritedProperties(TypedDict):
    """A [[comment]] that corrects [[CreativeWork]].

    References:
        https://schema.org/CorrectionComment
    Note:
        Model Depth 4
    Attributes:
        parentItem: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The parent of a question, answer or item in general.
        downvoteCount: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of downvotes this question, answer or comment has received from the community.
        upvoteCount: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of upvotes this question, answer or comment has received from the community.
    """

    parentItem: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    downvoteCount: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    upvoteCount: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]


class CorrectionCommentProperties(TypedDict):
    """A [[comment]] that corrects [[CreativeWork]].

    References:
        https://schema.org/CorrectionComment
    Note:
        Model Depth 4
    Attributes:
    """


class CorrectionCommentAllProperties(
    CorrectionCommentInheritedProperties, CorrectionCommentProperties, TypedDict
):
    pass


class CorrectionCommentBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="CorrectionComment", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"parentItem": {"exclude": True}}
        fields = {"downvoteCount": {"exclude": True}}
        fields = {"upvoteCount": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        CorrectionCommentProperties,
        CorrectionCommentInheritedProperties,
        CorrectionCommentAllProperties,
    ] = CorrectionCommentAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CorrectionComment"
    return model


CorrectionComment = create_schema_org_model()


def create_correctioncomment_model(
    model: Union[
        CorrectionCommentProperties,
        CorrectionCommentInheritedProperties,
        CorrectionCommentAllProperties,
    ]
):
    _type = deepcopy(CorrectionCommentAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of CorrectionCommentAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: CorrectionCommentAllProperties):
    pydantic_type = create_correctioncomment_model(model=model)
    return pydantic_type(model).schema_json()
