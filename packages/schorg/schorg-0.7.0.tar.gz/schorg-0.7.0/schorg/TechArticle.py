"""
A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.

https://schema.org/TechArticle
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TechArticleInheritedProperties(TypedDict):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.

    References:
        https://schema.org/TechArticle
    Note:
        Model Depth 4
    Attributes:
        pageEnd: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): The page on which the work ends; for example "138" or "xvi".
        wordCount: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): The number of words in the text of the Article.
        articleSection: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.
        articleBody: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The actual body of the article.
        speakable: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [[cssSelector]] property.3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For thiswe define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.         
        backstory: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): For an [[Article]], typically a [[NewsArticle]], the backstory property provides a textual summary giving a brief explanation of why and how an article was created. In a journalistic setting this could include information about reporting process, methods, interviews, data sources, etc.
        pagination: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".
        pageStart: (Optional[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]): The page on which the work starts; for example "135" or "xiii".
    """

    pageEnd: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    wordCount: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    articleSection: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    articleBody: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    speakable: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    backstory: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    pagination: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    pageStart: NotRequired[Union[List[Union[SchemaOrgObj, str, int]], SchemaOrgObj, str, int]]
    


class TechArticleProperties(TypedDict):
    """A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.

    References:
        https://schema.org/TechArticle
    Note:
        Model Depth 4
    Attributes:
        proficiencyLevel: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Proficiency needed for this content; expected values: 'Beginner', 'Expert'.
        dependencies: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Prerequisites needed to fulfill steps in article.
    """

    proficiencyLevel: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    dependencies: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(TechArticleInheritedProperties , TechArticleProperties, TypedDict):
    pass


class TechArticleBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="TechArticle",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'pageEnd': {'exclude': True}}
        fields = {'wordCount': {'exclude': True}}
        fields = {'articleSection': {'exclude': True}}
        fields = {'articleBody': {'exclude': True}}
        fields = {'speakable': {'exclude': True}}
        fields = {'backstory': {'exclude': True}}
        fields = {'pagination': {'exclude': True}}
        fields = {'pageStart': {'exclude': True}}
        fields = {'proficiencyLevel': {'exclude': True}}
        fields = {'dependencies': {'exclude': True}}
        


def create_schema_org_model(type_: Union[TechArticleProperties, TechArticleInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "TechArticle"
    return model
    

TechArticle = create_schema_org_model()


def create_techarticle_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_techarticle_model(model=model)
    return pydantic_type(model).schema_json()


