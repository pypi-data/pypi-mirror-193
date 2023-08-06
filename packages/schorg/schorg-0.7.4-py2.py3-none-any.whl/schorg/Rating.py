"""
A rating is an evaluation on a numeric scale, such as 1 to 5 stars.

https://schema.org/Rating
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RatingInheritedProperties(TypedDict):
    """A rating is an evaluation on a numeric scale, such as 1 to 5 stars.

    References:
        https://schema.org/Rating
    Note:
        Model Depth 3
    Attributes:
    """


class RatingProperties(TypedDict):
    """A rating is an evaluation on a numeric scale, such as 1 to 5 stars.

    References:
        https://schema.org/Rating
    Note:
        Model Depth 3
    Attributes:
        reviewAspect: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): This Review or Rating is relevant to this part or facet of the itemReviewed.
        author: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.
        ratingExplanation: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A short explanation (e.g. one to two sentences) providing background context and other information that led to the conclusion expressed in the rating. This is particularly applicable to ratings associated with "fact check" markup using [[ClaimReview]].
        bestRating: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.
        ratingValue: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The rating for the content.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        worstRating: (Optional[Union[List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]], StrictInt, StrictFloat, SchemaOrgObj, str]]): The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.
    """

    reviewAspect: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    author: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    ratingExplanation: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    bestRating: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    ratingValue: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]
    worstRating: NotRequired[
        Union[
            List[Union[StrictInt, StrictFloat, SchemaOrgObj, str]],
            StrictInt,
            StrictFloat,
            SchemaOrgObj,
            str,
        ]
    ]


class RatingAllProperties(RatingInheritedProperties, RatingProperties, TypedDict):
    pass


class RatingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Rating", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"reviewAspect": {"exclude": True}}
        fields = {"author": {"exclude": True}}
        fields = {"ratingExplanation": {"exclude": True}}
        fields = {"bestRating": {"exclude": True}}
        fields = {"ratingValue": {"exclude": True}}
        fields = {"worstRating": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RatingProperties, RatingInheritedProperties, RatingAllProperties
    ] = RatingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Rating"
    return model


Rating = create_schema_org_model()


def create_rating_model(
    model: Union[RatingProperties, RatingInheritedProperties, RatingAllProperties]
):
    _type = deepcopy(RatingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RatingAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RatingAllProperties):
    pydantic_type = create_rating_model(model=model)
    return pydantic_type(model).schema_json()
