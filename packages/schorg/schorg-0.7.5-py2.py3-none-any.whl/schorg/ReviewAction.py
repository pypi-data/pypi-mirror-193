"""
The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.

https://schema.org/ReviewAction
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReviewActionInheritedProperties(TypedDict):
    """The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.

    References:
        https://schema.org/ReviewAction
    Note:
        Model Depth 4
    Attributes:
    """


class ReviewActionProperties(TypedDict):
    """The act of producing a balanced opinion about the object for an audience. An agent reviews an object with participants resulting in a review.

    References:
        https://schema.org/ReviewAction
    Note:
        Model Depth 4
    Attributes:
        resultReview: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A sub property of result. The review that resulted in the performing of the action.
    """

    resultReview: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ReviewActionAllProperties(
    ReviewActionInheritedProperties, ReviewActionProperties, TypedDict
):
    pass


class ReviewActionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReviewAction", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"resultReview": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReviewActionProperties,
        ReviewActionInheritedProperties,
        ReviewActionAllProperties,
    ] = ReviewActionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReviewAction"
    return model


ReviewAction = create_schema_org_model()


def create_reviewaction_model(
    model: Union[
        ReviewActionProperties,
        ReviewActionInheritedProperties,
        ReviewActionAllProperties,
    ]
):
    _type = deepcopy(ReviewActionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReviewAction. Please see: https://schema.org/ReviewAction"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReviewActionAllProperties):
    pydantic_type = create_reviewaction_model(model=model)
    return pydantic_type(model).schema_json()
