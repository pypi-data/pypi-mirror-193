"""
A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).

https://schema.org/ClaimReview
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ClaimReviewInheritedProperties(TypedDict):
    """A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).

    References:
        https://schema.org/ClaimReview
    Note:
        Model Depth 4
    Attributes:
        reviewBody: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The actual body of the review.
        associatedMediaReview: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An associated [[MediaReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]].
        associatedReview: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An associated [[Review]].
        positiveNotes: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Provides positive considerations regarding something, for example product highlights or (alongside [[negativeNotes]]) pro/con lists for reviews.In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).
        reviewRating: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating``` applies to rating given by the review. The [[aggregateRating]] property applies to the review itself, as a creative work.
        reviewAspect: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): This Review or Rating is relevant to this part or facet of the itemReviewed.
        itemReviewed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The item that is being reviewed/rated.
        negativeNotes: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Provides negative considerations regarding something, most typically in pro/con lists for reviews (alongside [[positiveNotes]]). For symmetry In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]] used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used on [[Product]].The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).
        associatedClaimReview: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An associated [[ClaimReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]].
    """

    reviewBody: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    associatedMediaReview: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    associatedReview: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    positiveNotes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reviewRating: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reviewAspect: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    itemReviewed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    negativeNotes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    associatedClaimReview: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]


class ClaimReviewProperties(TypedDict):
    """A fact-checking review of claims made (or reported) in some creative work (referenced via itemReviewed).

    References:
        https://schema.org/ClaimReview
    Note:
        Model Depth 4
    Attributes:
        claimReviewed: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A short summary of the specific claims reviewed in a ClaimReview.
    """

    claimReviewed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class ClaimReviewAllProperties(
    ClaimReviewInheritedProperties, ClaimReviewProperties, TypedDict
):
    pass


class ClaimReviewBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ClaimReview", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"reviewBody": {"exclude": True}}
        fields = {"associatedMediaReview": {"exclude": True}}
        fields = {"associatedReview": {"exclude": True}}
        fields = {"positiveNotes": {"exclude": True}}
        fields = {"reviewRating": {"exclude": True}}
        fields = {"reviewAspect": {"exclude": True}}
        fields = {"itemReviewed": {"exclude": True}}
        fields = {"negativeNotes": {"exclude": True}}
        fields = {"associatedClaimReview": {"exclude": True}}
        fields = {"claimReviewed": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ClaimReviewProperties, ClaimReviewInheritedProperties, ClaimReviewAllProperties
    ] = ClaimReviewAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ClaimReview"
    return model


ClaimReview = create_schema_org_model()


def create_claimreview_model(
    model: Union[
        ClaimReviewProperties, ClaimReviewInheritedProperties, ClaimReviewAllProperties
    ]
):
    _type = deepcopy(ClaimReviewAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ClaimReviewAllProperties):
    pydantic_type = create_claimreview_model(model=model)
    return pydantic_type(model).schema_json()
