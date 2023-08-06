"""
An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

https://schema.org/Answer
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AnswerInheritedProperties(TypedDict):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    References:
        https://schema.org/Answer
    Note:
        Model Depth 4
    Attributes:
        parentItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The parent of a question, answer or item in general.
        downvoteCount: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of downvotes this question, answer or comment has received from the community.
        upvoteCount: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of upvotes this question, answer or comment has received from the community.
    """

    parentItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    downvoteCount: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    upvoteCount: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]


class AnswerProperties(TypedDict):
    """An answer offered to a question; perhaps correct, perhaps opinionated or wrong.

    References:
        https://schema.org/Answer
    Note:
        Model Depth 4
    Attributes:
        answerExplanation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A step-by-step or full explanation about Answer. Can outline how this Answer was achieved or contain more broad clarification or statement about it.
    """

    answerExplanation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class AnswerAllProperties(AnswerInheritedProperties, AnswerProperties, TypedDict):
    pass


class AnswerBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Answer", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"parentItem": {"exclude": True}}
        fields = {"downvoteCount": {"exclude": True}}
        fields = {"upvoteCount": {"exclude": True}}
        fields = {"answerExplanation": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        AnswerProperties, AnswerInheritedProperties, AnswerAllProperties
    ] = AnswerAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Answer"
    return model


Answer = create_schema_org_model()


def create_answer_model(
    model: Union[AnswerProperties, AnswerInheritedProperties, AnswerAllProperties]
):
    _type = deepcopy(AnswerAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AnswerAllProperties):
    pydantic_type = create_answer_model(model=model)
    return pydantic_type(model).schema_json()
