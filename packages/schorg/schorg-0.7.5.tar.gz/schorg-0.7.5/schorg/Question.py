"""
A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.

https://schema.org/Question
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class QuestionInheritedProperties(TypedDict):
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.

    References:
        https://schema.org/Question
    Note:
        Model Depth 4
    Attributes:
        parentItem: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The parent of a question, answer or item in general.
        downvoteCount: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of downvotes this question, answer or comment has received from the community.
        upvoteCount: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of upvotes this question, answer or comment has received from the community.
    """

    parentItem: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    downvoteCount: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    upvoteCount: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]


class QuestionProperties(TypedDict):
    """A specific question - e.g. from a user seeking answers online, or collected in a Frequently Asked Questions (FAQ) document.

    References:
        https://schema.org/Question
    Note:
        Model Depth 4
    Attributes:
        acceptedAnswer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The answer(s) that has been accepted as best, typically on a Question/Answer site. Sites vary in their selection mechanisms, e.g. drawing on community opinion and/or the view of the Question author.
        suggestedAnswer: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site.
        answerCount: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of answers this question has received.
        eduQuestionType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): For questions that are part of learning resources (e.g. Quiz), eduQuestionType indicates the format of question being given. Example: "Multiple choice", "Open ended", "Flashcard".
    """

    acceptedAnswer: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    suggestedAnswer: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    answerCount: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    eduQuestionType: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class QuestionAllProperties(QuestionInheritedProperties, QuestionProperties, TypedDict):
    pass


class QuestionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Question", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"parentItem": {"exclude": True}}
        fields = {"downvoteCount": {"exclude": True}}
        fields = {"upvoteCount": {"exclude": True}}
        fields = {"acceptedAnswer": {"exclude": True}}
        fields = {"suggestedAnswer": {"exclude": True}}
        fields = {"answerCount": {"exclude": True}}
        fields = {"eduQuestionType": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        QuestionProperties, QuestionInheritedProperties, QuestionAllProperties
    ] = QuestionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Question"
    return model


Question = create_schema_org_model()


def create_question_model(
    model: Union[QuestionProperties, QuestionInheritedProperties, QuestionAllProperties]
):
    _type = deepcopy(QuestionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of Question. Please see: https://schema.org/Question"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: QuestionAllProperties):
    pydantic_type = create_question_model(model=model)
    return pydantic_type(model).schema_json()
