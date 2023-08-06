"""
[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s.

https://schema.org/Recommendation
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RecommendationInheritedProperties(TypedDict):
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s.

    References:
        https://schema.org/Recommendation
    Note:
        Model Depth 4
    Attributes:
        reviewBody: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The actual body of the review.
        associatedMediaReview: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An associated [[MediaReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]].
        associatedReview: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An associated [[Review]].
        positiveNotes: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Provides positive considerations regarding something, for example product highlights or (alongside [[negativeNotes]]) pro/con lists for reviews.In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described.The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most positive is at the beginning of the list).
        reviewRating: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The rating given in this review. Note that reviews can themselves be rated. The ```reviewRating``` applies to rating given by the review. The [[aggregateRating]] property applies to the review itself, as a creative work.
        reviewAspect: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): This Review or Rating is relevant to this part or facet of the itemReviewed.
        itemReviewed: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The item that is being reviewed/rated.
        negativeNotes: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Provides negative considerations regarding something, most typically in pro/con lists for reviews (alongside [[positiveNotes]]). For symmetry In the case of a [[Review]], the property describes the [[itemReviewed]] from the perspective of the review; in the case of a [[Product]], the product itself is being described. Since product descriptions tend to emphasise positive claims, it may be relatively unusual to find [[negativeNotes]] used in this way. Nevertheless for the sake of symmetry, [[negativeNotes]] can be used on [[Product]].The property values can be expressed either as unstructured text (repeated as necessary), or if ordered, as a list (in which case the most negative is at the beginning of the list).
        associatedClaimReview: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An associated [[ClaimReview]], related by specific common content, topic or claim. The expectation is that this property would be most typically used in cases where a single activity is conducting both claim reviews and media reviews, in which case [[relatedMediaReview]] would commonly be used on a [[ClaimReview]], while [[relatedClaimReview]] would be used on [[MediaReview]].
    """

    reviewBody: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    associatedMediaReview: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    associatedReview: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]
    positiveNotes: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    reviewRating: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    reviewAspect: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    itemReviewed: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    negativeNotes: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    associatedClaimReview: NotRequired[
        Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]
    ]


class RecommendationProperties(TypedDict):
    """[[Recommendation]] is a type of [[Review]] that suggests or proposes something as the best option or best course of action. Recommendations may be for products or services, or other concrete things, as in the case of a ranked list or product guide. A [[Guide]] may list multiple recommendations for different categories. For example, in a [[Guide]] about which TVs to buy, the author may have several [[Recommendation]]s.

    References:
        https://schema.org/Recommendation
    Note:
        Model Depth 4
    Attributes:
        category: (Optional[Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]]): A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.
    """

    category: NotRequired[
        Union[List[Union[AnyUrl, SchemaOrgObj, str]], AnyUrl, SchemaOrgObj, str]
    ]


class RecommendationAllProperties(
    RecommendationInheritedProperties, RecommendationProperties, TypedDict
):
    pass


class RecommendationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Recommendation", alias="@id")
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
        fields = {"category": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        RecommendationProperties,
        RecommendationInheritedProperties,
        RecommendationAllProperties,
    ] = RecommendationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Recommendation"
    return model


Recommendation = create_schema_org_model()


def create_recommendation_model(
    model: Union[
        RecommendationProperties,
        RecommendationInheritedProperties,
        RecommendationAllProperties,
    ]
):
    _type = deepcopy(RecommendationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of RecommendationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: RecommendationAllProperties):
    pydantic_type = create_recommendation_model(model=model)
    return pydantic_type(model).schema_json()
