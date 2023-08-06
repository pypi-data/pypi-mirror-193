"""
An EndorsementRating is a rating that expresses some level of endorsement, for example inclusion in a "critic's pick" blog, a"Like" or "+1" on a social network. It can be considered the [[result]] of an [[EndorseAction]] in which the [[object]] of the action is rated positively bysome [[agent]]. As is common elsewhere in schema.org, it is sometimes more useful to describe the results of such an action without explicitly describing the [[Action]].An [[EndorsementRating]] may be part of a numeric scale or organized system, but this is not required: having an explicit type for indicating a positive,endorsement rating is particularly useful in the absence of numeric scales as it helps consumers understand that the rating is broadly positive.

https://schema.org/EndorsementRating
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EndorsementRatingInheritedProperties(TypedDict):
    """An EndorsementRating is a rating that expresses some level of endorsement, for example inclusion in a "critic's pick" blog, a"Like" or "+1" on a social network. It can be considered the [[result]] of an [[EndorseAction]] in which the [[object]] of the action is rated positively bysome [[agent]]. As is common elsewhere in schema.org, it is sometimes more useful to describe the results of such an action without explicitly describing the [[Action]].An [[EndorsementRating]] may be part of a numeric scale or organized system, but this is not required: having an explicit type for indicating a positive,endorsement rating is particularly useful in the absence of numeric scales as it helps consumers understand that the rating is broadly positive.

    References:
        https://schema.org/EndorsementRating
    Note:
        Model Depth 4
    Attributes:
        reviewAspect: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This Review or Rating is relevant to this part or facet of the itemReviewed.
        author: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The author of this content or rating. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.
        ratingExplanation: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A short explanation (e.g. one to two sentences) providing background context and other information that led to the conclusion expressed in the rating. This is particularly applicable to ratings associated with "fact check" markup using [[ClaimReview]].
        bestRating: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.
        ratingValue: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The rating for the content.Usage guidelines:* Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similar Unicode symbols.* Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
        worstRating: (Optional[Union[List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]], str, SchemaOrgObj, StrictInt, StrictFloat]]): The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.
    """

    reviewAspect: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    author: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    ratingExplanation: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    bestRating: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    ratingValue: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]
    worstRating: NotRequired[
        Union[
            List[Union[str, SchemaOrgObj, StrictInt, StrictFloat]],
            str,
            SchemaOrgObj,
            StrictInt,
            StrictFloat,
        ]
    ]


class EndorsementRatingProperties(TypedDict):
    """An EndorsementRating is a rating that expresses some level of endorsement, for example inclusion in a "critic's pick" blog, a"Like" or "+1" on a social network. It can be considered the [[result]] of an [[EndorseAction]] in which the [[object]] of the action is rated positively bysome [[agent]]. As is common elsewhere in schema.org, it is sometimes more useful to describe the results of such an action without explicitly describing the [[Action]].An [[EndorsementRating]] may be part of a numeric scale or organized system, but this is not required: having an explicit type for indicating a positive,endorsement rating is particularly useful in the absence of numeric scales as it helps consumers understand that the rating is broadly positive.

    References:
        https://schema.org/EndorsementRating
    Note:
        Model Depth 4
    Attributes:
    """


class EndorsementRatingAllProperties(
    EndorsementRatingInheritedProperties, EndorsementRatingProperties, TypedDict
):
    pass


class EndorsementRatingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EndorsementRating", alias="@id")
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
        EndorsementRatingProperties,
        EndorsementRatingInheritedProperties,
        EndorsementRatingAllProperties,
    ] = EndorsementRatingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EndorsementRating"
    return model


EndorsementRating = create_schema_org_model()


def create_endorsementrating_model(
    model: Union[
        EndorsementRatingProperties,
        EndorsementRatingInheritedProperties,
        EndorsementRatingAllProperties,
    ]
):
    _type = deepcopy(EndorsementRatingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of EndorsementRating. Please see: https://schema.org/EndorsementRating"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: EndorsementRatingAllProperties):
    pydantic_type = create_endorsementrating_model(model=model)
    return pydantic_type(model).schema_json()
