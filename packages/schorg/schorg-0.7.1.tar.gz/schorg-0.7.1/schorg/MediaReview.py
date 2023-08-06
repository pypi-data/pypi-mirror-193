"""
A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.    For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is    a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working    to combat misinformation, the specific structures for representing media objects, their versions and publication context, are still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not yet been finalized.

https://schema.org/MediaReview
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MediaReviewInheritedProperties(TypedDict):
    """A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.    For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is    a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working    to combat misinformation, the specific structures for representing media objects, their versions and publication context, are still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not yet been finalized.

    References:
        https://schema.org/MediaReview
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
    associatedMediaReview: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    associatedReview: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    positiveNotes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reviewRating: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reviewAspect: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    itemReviewed: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    negativeNotes: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    associatedClaimReview: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class MediaReviewProperties(TypedDict):
    """A [[MediaReview]] is a more specialized form of Review dedicated to the evaluation of media content online, typically in the context of fact-checking and misinformation.    For more general reviews of media in the broader sense, use [[UserReview]], [[CriticReview]] or other [[Review]] types. This definition is    a work in progress. While the [[MediaManipulationRatingEnumeration]] list reflects significant community review amongst fact-checkers and others working    to combat misinformation, the specific structures for representing media objects, their versions and publication context, are still evolving. Similarly, best practices for the relationship between [[MediaReview]] and [[ClaimReview]] markup have not yet been finalized.

    References:
        https://schema.org/MediaReview
    Note:
        Model Depth 4
    Attributes:
        originalMediaLink: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Link to the page containing an original version of the content, or directly to an online copy of the original [[MediaObject]] content, e.g. video file.
        originalMediaContextDescription: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Describes, in a [[MediaReview]] when dealing with [[DecontextualizedContent]], background information that can contribute to better interpretation of the [[MediaObject]].
        mediaAuthenticityCategory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates a MediaManipulationRatingEnumeration classification of a media object (in the context of how it was published or shared).
    """

    originalMediaLink: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    originalMediaContextDescription: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    mediaAuthenticityCategory: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class AllProperties(MediaReviewInheritedProperties , MediaReviewProperties, TypedDict):
    pass


class MediaReviewBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MediaReview",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'reviewBody': {'exclude': True}}
        fields = {'associatedMediaReview': {'exclude': True}}
        fields = {'associatedReview': {'exclude': True}}
        fields = {'positiveNotes': {'exclude': True}}
        fields = {'reviewRating': {'exclude': True}}
        fields = {'reviewAspect': {'exclude': True}}
        fields = {'itemReviewed': {'exclude': True}}
        fields = {'negativeNotes': {'exclude': True}}
        fields = {'associatedClaimReview': {'exclude': True}}
        fields = {'originalMediaLink': {'exclude': True}}
        fields = {'originalMediaContextDescription': {'exclude': True}}
        fields = {'mediaAuthenticityCategory': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MediaReviewProperties, MediaReviewInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MediaReview"
    return model
    

MediaReview = create_schema_org_model()


def create_mediareview_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mediareview_model(model=model)
    return pydantic_type(model).schema_json()


