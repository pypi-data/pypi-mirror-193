"""
The [[ReportageNewsArticle]] type is a subtype of [[NewsArticle]] representing news articles which are the result of journalistic news reporting conventions.In practice many news publishers produce a wide variety of article types, many of which might be considered a [[NewsArticle]] but not a [[ReportageNewsArticle]]. For example, opinion pieces, reviews, analysis, sponsored or satirical articles, or articles that combine several of these elements.The [[ReportageNewsArticle]] type is based on a stricter ideal for "news" as a work of journalism, with articles based on factual information either observed or verified by the author, or reported and verified from knowledgeable sources.  This often includes perspectives from multiple viewpoints on a particular issue (distinguishing news reports from public relations or propaganda).  News reports in the [[ReportageNewsArticle]] sense de-emphasize the opinion of the author, with commentary and value judgements typically expressed elsewhere.A [[ReportageNewsArticle]] which goes deeper into analysis can also be marked with an additional type of [[AnalysisNewsArticle]].

https://schema.org/ReportageNewsArticle
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReportageNewsArticleInheritedProperties(TypedDict):
    """The [[ReportageNewsArticle]] type is a subtype of [[NewsArticle]] representing news articles which are the result of journalistic news reporting conventions.In practice many news publishers produce a wide variety of article types, many of which might be considered a [[NewsArticle]] but not a [[ReportageNewsArticle]]. For example, opinion pieces, reviews, analysis, sponsored or satirical articles, or articles that combine several of these elements.The [[ReportageNewsArticle]] type is based on a stricter ideal for "news" as a work of journalism, with articles based on factual information either observed or verified by the author, or reported and verified from knowledgeable sources.  This often includes perspectives from multiple viewpoints on a particular issue (distinguishing news reports from public relations or propaganda).  News reports in the [[ReportageNewsArticle]] sense de-emphasize the opinion of the author, with commentary and value judgements typically expressed elsewhere.A [[ReportageNewsArticle]] which goes deeper into analysis can also be marked with an additional type of [[AnalysisNewsArticle]].

    References:
        https://schema.org/ReportageNewsArticle
    Note:
        Model Depth 5
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


class ReportageNewsArticleProperties(TypedDict):
    """The [[ReportageNewsArticle]] type is a subtype of [[NewsArticle]] representing news articles which are the result of journalistic news reporting conventions.In practice many news publishers produce a wide variety of article types, many of which might be considered a [[NewsArticle]] but not a [[ReportageNewsArticle]]. For example, opinion pieces, reviews, analysis, sponsored or satirical articles, or articles that combine several of these elements.The [[ReportageNewsArticle]] type is based on a stricter ideal for "news" as a work of journalism, with articles based on factual information either observed or verified by the author, or reported and verified from knowledgeable sources.  This often includes perspectives from multiple viewpoints on a particular issue (distinguishing news reports from public relations or propaganda).  News reports in the [[ReportageNewsArticle]] sense de-emphasize the opinion of the author, with commentary and value judgements typically expressed elsewhere.A [[ReportageNewsArticle]] which goes deeper into analysis can also be marked with an additional type of [[AnalysisNewsArticle]].

    References:
        https://schema.org/ReportageNewsArticle
    Note:
        Model Depth 5
    Attributes:
    """


class ReportageNewsArticleAllProperties(
    ReportageNewsArticleInheritedProperties, ReportageNewsArticleProperties, TypedDict
):
    pass


class ReportageNewsArticleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReportageNewsArticle", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"printColumn": {"exclude": True}}
        fields = {"printEdition": {"exclude": True}}
        fields = {"printSection": {"exclude": True}}
        fields = {"printPage": {"exclude": True}}
        fields = {"dateline": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        ReportageNewsArticleProperties,
        ReportageNewsArticleInheritedProperties,
        ReportageNewsArticleAllProperties,
    ] = ReportageNewsArticleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReportageNewsArticle"
    return model


ReportageNewsArticle = create_schema_org_model()


def create_reportagenewsarticle_model(
    model: Union[
        ReportageNewsArticleProperties,
        ReportageNewsArticleInheritedProperties,
        ReportageNewsArticleAllProperties,
    ]
):
    _type = deepcopy(ReportageNewsArticleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReportageNewsArticleAllProperties):
    pydantic_type = create_reportagenewsarticle_model(model=model)
    return pydantic_type(model).schema_json()
