"""
An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content.

https://schema.org/AdvertiserContentArticle
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AdvertiserContentArticleInheritedProperties(TypedDict):
    """An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content.

    References:
        https://schema.org/AdvertiserContentArticle
    Note:
        Model Depth 4
    Attributes:
        pageEnd: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The page on which the work ends; for example "138" or "xvi".
        wordCount: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The number of words in the text of the Article.
        articleSection: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.
        articleBody: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The actual body of the article.
        speakable: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [[cssSelector]] property.3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For thiswe define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.
        backstory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): For an [[Article]], typically a [[NewsArticle]], the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc.
        pagination: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".
        pageStart: (Optional[Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]]): The page on which the work starts; for example "135" or "xiii".
    """

    pageEnd: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    wordCount: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]
    articleSection: NotRequired[
        Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]
    ]
    articleBody: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    speakable: NotRequired[
        Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]
    ]
    backstory: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    pagination: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    pageStart: NotRequired[
        Union[List[Union[str, SchemaOrgObj, int]], str, SchemaOrgObj, int]
    ]


class AdvertiserContentArticleProperties(TypedDict):
    """An [[Article]] that an external entity has paid to place or to produce to its specifications. Includes [advertorials](https://en.wikipedia.org/wiki/Advertorial), sponsored content, native advertising and other paid content.

    References:
        https://schema.org/AdvertiserContentArticle
    Note:
        Model Depth 4
    Attributes:
    """


class AdvertiserContentArticleAllProperties(
    AdvertiserContentArticleInheritedProperties,
    AdvertiserContentArticleProperties,
    TypedDict,
):
    pass


class AdvertiserContentArticleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AdvertiserContentArticle", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"pageEnd": {"exclude": True}}
        fields = {"wordCount": {"exclude": True}}
        fields = {"articleSection": {"exclude": True}}
        fields = {"articleBody": {"exclude": True}}
        fields = {"speakable": {"exclude": True}}
        fields = {"backstory": {"exclude": True}}
        fields = {"pagination": {"exclude": True}}
        fields = {"pageStart": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        AdvertiserContentArticleProperties,
        AdvertiserContentArticleInheritedProperties,
        AdvertiserContentArticleAllProperties,
    ] = AdvertiserContentArticleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AdvertiserContentArticle"
    return model


AdvertiserContentArticle = create_schema_org_model()


def create_advertisercontentarticle_model(
    model: Union[
        AdvertiserContentArticleProperties,
        AdvertiserContentArticleInheritedProperties,
        AdvertiserContentArticleAllProperties,
    ]
):
    _type = deepcopy(AdvertiserContentArticleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of AdvertiserContentArticle. Please see: https://schema.org/AdvertiserContentArticle"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: AdvertiserContentArticleAllProperties):
    pydantic_type = create_advertisercontentarticle_model(model=model)
    return pydantic_type(model).schema_json()
