"""
Web page type: Checkout page.

https://schema.org/CheckoutPage
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class CheckoutPageInheritedProperties(TypedDict):
    """Web page type: Checkout page.

    References:
        https://schema.org/CheckoutPage
    Note:
        Model Depth 4
    Attributes:
        significantLink: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.
        specialty: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): One of the domain specialities to which this web page's content applies.
        reviewedBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): People or organizations that have reviewed the content on this web page for accuracy and/or completeness.
        lastReviewed: (Optional[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]): Date on which the content on this web page was last reviewed for accuracy and/or completeness.
        relatedLink: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): A link related to this web page, for example to other related web pages.
        breadcrumb: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A set of links that can help a user understand and navigate a website hierarchy.
        significantLinks: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): The most significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.
        mainContentOfPage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates if this web page element is the main subject of the page.
        speakable: (Optional[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]): Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [[cssSelector]] property.3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For thiswe define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.         
        primaryImageOfPage: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Indicates the main image on the page.
    """

    significantLink: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    specialty: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    reviewedBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    lastReviewed: NotRequired[Union[List[Union[str, SchemaOrgObj, date]], str, SchemaOrgObj, date]]
    relatedLink: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    breadcrumb: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    significantLinks: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    mainContentOfPage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    speakable: NotRequired[Union[List[Union[AnyUrl, str, SchemaOrgObj]], AnyUrl, str, SchemaOrgObj]]
    primaryImageOfPage: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class CheckoutPageProperties(TypedDict):
    """Web page type: Checkout page.

    References:
        https://schema.org/CheckoutPage
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(CheckoutPageInheritedProperties , CheckoutPageProperties, TypedDict):
    pass


class CheckoutPageBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="CheckoutPage",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'significantLink': {'exclude': True}}
        fields = {'specialty': {'exclude': True}}
        fields = {'reviewedBy': {'exclude': True}}
        fields = {'lastReviewed': {'exclude': True}}
        fields = {'relatedLink': {'exclude': True}}
        fields = {'breadcrumb': {'exclude': True}}
        fields = {'significantLinks': {'exclude': True}}
        fields = {'mainContentOfPage': {'exclude': True}}
        fields = {'speakable': {'exclude': True}}
        fields = {'primaryImageOfPage': {'exclude': True}}
        


def create_schema_org_model(type_: Union[CheckoutPageProperties, CheckoutPageInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "CheckoutPage"
    return model
    

CheckoutPage = create_schema_org_model()


def create_checkoutpage_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_checkoutpage_model(model=model)
    return pydantic_type(model).schema_json()


