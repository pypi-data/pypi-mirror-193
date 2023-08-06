"""
Quiz: A test of knowledge, skills and abilities.

https://schema.org/Quiz
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class QuizInheritedProperties(TypedDict):
    """Quiz: A test of knowledge, skills and abilities.

    References:
        https://schema.org/Quiz
    Note:
        Model Depth 4
    Attributes:
        educationalLevel: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The level in terms of progression through an educational or training context. Examples of educational levels include 'beginner', 'intermediate' or 'advanced', and formal sets of level indicators.
        competencyRequired: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Knowledge, skill, ability or personal attribute that must be demonstrated by a person or other entity in order to do something such as earn an Educational Occupational Credential or understand a LearningResource.
        educationalUse: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The purpose of a work in the context of education; for example, 'assignment', 'group work'.
        educationalAlignment: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An alignment to an established educational framework.This property should not be used where the nature of the alignment can be described using a simple property, for example to express that a resource [[teaches]] or [[assesses]] a competency.
        assesses: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The item being described is intended to assess the competency or learning outcome defined by the referenced term.
        learningResourceType: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.
        teaches: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The item being described is intended to help a person learn the competency or learning outcome defined by the referenced term.
    """

    educationalLevel: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    competencyRequired: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    educationalUse: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    educationalAlignment: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    assesses: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    learningResourceType: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    teaches: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class QuizProperties(TypedDict):
    """Quiz: A test of knowledge, skills and abilities.

    References:
        https://schema.org/Quiz
    Note:
        Model Depth 4
    Attributes:
    """


class QuizAllProperties(QuizInheritedProperties, QuizProperties, TypedDict):
    pass


class QuizBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Quiz", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"educationalLevel": {"exclude": True}}
        fields = {"competencyRequired": {"exclude": True}}
        fields = {"educationalUse": {"exclude": True}}
        fields = {"educationalAlignment": {"exclude": True}}
        fields = {"assesses": {"exclude": True}}
        fields = {"learningResourceType": {"exclude": True}}
        fields = {"teaches": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        QuizProperties, QuizInheritedProperties, QuizAllProperties
    ] = QuizAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Quiz"
    return model


Quiz = create_schema_org_model()


def create_quiz_model(
    model: Union[QuizProperties, QuizInheritedProperties, QuizAllProperties]
):
    _type = deepcopy(QuizAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: QuizAllProperties):
    pydantic_type = create_quiz_model(model=model)
    return pydantic_type(model).schema_json()
