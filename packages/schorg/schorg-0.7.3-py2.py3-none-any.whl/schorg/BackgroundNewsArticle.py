"""
A [[NewsArticle]] providing historical context, definition and detail on a specific topic (aka "explainer" or "backgrounder"). For example, an in-depth article or frequently-asked-questions ([FAQ](https://en.wikipedia.org/wiki/FAQ)) document on topics such as Climate Change or the European Union. Other kinds of background material from a non-news setting are often described using [[Book]] or [[Article]], in particular [[ScholarlyArticle]]. See also [[NewsArticle]] for related vocabulary from a learning/education perspective.

https://schema.org/BackgroundNewsArticle
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BackgroundNewsArticleInheritedProperties(TypedDict):
    """A [[NewsArticle]] providing historical context, definition and detail on a specific topic (aka "explainer" or "backgrounder"). For example, an in-depth article or frequently-asked-questions ([FAQ](https://en.wikipedia.org/wiki/FAQ)) document on topics such as Climate Change or the European Union. Other kinds of background material from a non-news setting are often described using [[Book]] or [[Article]], in particular [[ScholarlyArticle]]. See also [[NewsArticle]] for related vocabulary from a learning/education perspective.

    References:
        https://schema.org/BackgroundNewsArticle
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


class BackgroundNewsArticleProperties(TypedDict):
    """A [[NewsArticle]] providing historical context, definition and detail on a specific topic (aka "explainer" or "backgrounder"). For example, an in-depth article or frequently-asked-questions ([FAQ](https://en.wikipedia.org/wiki/FAQ)) document on topics such as Climate Change or the European Union. Other kinds of background material from a non-news setting are often described using [[Book]] or [[Article]], in particular [[ScholarlyArticle]]. See also [[NewsArticle]] for related vocabulary from a learning/education perspective.

    References:
        https://schema.org/BackgroundNewsArticle
    Note:
        Model Depth 5
    Attributes:
    """


class BackgroundNewsArticleAllProperties(
    BackgroundNewsArticleInheritedProperties, BackgroundNewsArticleProperties, TypedDict
):
    pass


class BackgroundNewsArticleBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BackgroundNewsArticle", alias="@id")
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
        BackgroundNewsArticleProperties,
        BackgroundNewsArticleInheritedProperties,
        BackgroundNewsArticleAllProperties,
    ] = BackgroundNewsArticleAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BackgroundNewsArticle"
    return model


BackgroundNewsArticle = create_schema_org_model()


def create_backgroundnewsarticle_model(
    model: Union[
        BackgroundNewsArticleProperties,
        BackgroundNewsArticleInheritedProperties,
        BackgroundNewsArticleAllProperties,
    ]
):
    _type = deepcopy(BackgroundNewsArticleAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BackgroundNewsArticleAllProperties):
    pydantic_type = create_backgroundnewsarticle_model(model=model)
    return pydantic_type(model).schema_json()
