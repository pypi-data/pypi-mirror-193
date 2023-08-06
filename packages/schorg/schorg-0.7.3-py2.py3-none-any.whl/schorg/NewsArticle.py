"""
A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.A more detailed overview of [schema.org News markup](/docs/news.html) is also available.

https://schema.org/NewsArticle
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NewsArticleInheritedProperties(TypedDict):
    """A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.A more detailed overview of [schema.org News markup](/docs/news.html) is also available.

    References:
        https://schema.org/NewsArticle
    Note:
        Model Depth 4
    Attributes:
        pageEnd: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The page on which the work ends; for example "138" or "xvi".
        wordCount: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The number of words in the text of the Article.
        articleSection: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.
        articleBody: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The actual body of the article.
        speakable: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [[cssSelector]] property.3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For thiswe define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.
        backstory: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): For an [[Article]], typically a [[NewsArticle]], the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc.
        pagination: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".
        pageStart: (Optional[Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]]): The page on which the work starts; for example "135" or "xiii".
    """

    pageEnd: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]
    wordCount: NotRequired[
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
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
        Union[List[Union[str, int, SchemaOrgObj]], str, int, SchemaOrgObj]
    ]


class NewsArticleProperties(TypedDict):
    """A NewsArticle is an article whose content reports news, or provides background context and supporting materials for understanding the news.A more detailed overview of [schema.org News markup](/docs/news.html) is also available.

    References:
        https://schema.org/NewsArticle
    Note:
        Model Depth 4
    Attributes:
        printColumn: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The number of the column in which the NewsArticle appears in the print edition.
        printEdition: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): The edition of the print product in which the NewsArticle appears.
        printSection: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If this NewsArticle appears in print, this field indicates the print section in which the article appeared.
        printPage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).
        dateline: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A [dateline](https://en.wikipedia.org/wiki/Dateline) is a brief piece of text included in news articles that describes where and when the story was written or filed though the date is often omitted. Sometimes only a placename is provided.Structured representations of dateline-related information can also be expressed more explicitly using [[locationCreated]] (which represents where a work was created, e.g. where a news report was written).  For location depicted or described in the content, use [[contentLocation]].Dateline summaries are oriented more towards human readers than towards automated processing, and can vary substantially. Some examples: "BEIRUT, Lebanon, June 2.", "Paris, France", "December 19, 2017 11:43AM Reporting from Washington", "Beijing/Moscow", "QUEZON CITY, Philippines".
    """

    printColumn: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    printEdition: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    printSection: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    printPage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    dateline: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class NewsArticleAllProperties(
    NewsArticleInheritedProperties, NewsArticleProperties, TypedDict
):
    pass


class NewsArticleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="NewsArticle", alias="@id")
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
        fields = {"printColumn": {"exclude": True}}
        fields = {"printEdition": {"exclude": True}}
        fields = {"printSection": {"exclude": True}}
        fields = {"printPage": {"exclude": True}}
        fields = {"dateline": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        NewsArticleProperties, NewsArticleInheritedProperties, NewsArticleAllProperties
    ] = NewsArticleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "NewsArticle"
    return model


NewsArticle = create_schema_org_model()


def create_newsarticle_model(
    model: Union[
        NewsArticleProperties, NewsArticleInheritedProperties, NewsArticleAllProperties
    ]
):
    _type = deepcopy(NewsArticleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: NewsArticleAllProperties):
    pydantic_type = create_newsarticle_model(model=model)
    return pydantic_type(model).schema_json()
