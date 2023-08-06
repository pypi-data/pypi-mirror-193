"""
A web page that provides medical information.

https://schema.org/MedicalWebPage
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MedicalWebPageInheritedProperties(TypedDict):
    """A web page that provides medical information.

    References:
        https://schema.org/MedicalWebPage
    Note:
        Model Depth 4
    Attributes:
        significantLink: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.
        specialty: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): One of the domain specialities to which this web page's content applies.
        reviewedBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): People or organizations that have reviewed the content on this web page for accuracy and/or completeness.
        lastReviewed: (Optional[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]): Date on which the content on this web page was last reviewed for accuracy and/or completeness.
        relatedLink: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): A link related to this web page, for example to other related web pages.
        breadcrumb: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A set of links that can help a user understand and navigate a website hierarchy.
        significantLinks: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): The most significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.
        mainContentOfPage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates if this web page element is the main subject of the page.
        speakable: (Optional[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]): Indicates sections of a Web page that are particularly 'speakable' in the sense of being highlighted as being especially appropriate for text-to-speech conversion. Other sections of a page may also be usefully spoken in particular circumstances; the 'speakable' property serves to indicate the parts most likely to be generally useful for speech.The *speakable* property can be repeated an arbitrary number of times, with three kinds of possible 'content-locator' values:1.) *id-value* URL references - uses *id-value* of an element in the page being annotated. The simplest use of *speakable* has (potentially relative) URL values, referencing identified sections of the document concerned.2.) CSS Selectors - addresses content in the annotated page, e.g. via class attribute. Use the [[cssSelector]] property.3.)  XPaths - addresses content via XPaths (assuming an XML view of the content). Use the [[xpath]] property.For more sophisticated markup of speakable sections beyond simple ID references, either CSS selectors or XPath expressions to pick out document section(s) as speakable. For thiswe define a supporting type, [[SpeakableSpecification]]  which is defined to be a possible value of the *speakable* property.         
        primaryImageOfPage: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Indicates the main image on the page.
    """

    significantLink: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    specialty: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    reviewedBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    lastReviewed: NotRequired[Union[List[Union[SchemaOrgObj, str, date]], SchemaOrgObj, str, date]]
    relatedLink: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    breadcrumb: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    significantLinks: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    mainContentOfPage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    speakable: NotRequired[Union[List[Union[SchemaOrgObj, str, AnyUrl]], SchemaOrgObj, str, AnyUrl]]
    primaryImageOfPage: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class MedicalWebPageProperties(TypedDict):
    """A web page that provides medical information.

    References:
        https://schema.org/MedicalWebPage
    Note:
        Model Depth 4
    Attributes:
        medicalAudience: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Medical audience for page.
        aspect: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment', 'causes', 'prognosis', 'etiology', 'epidemiology', etc.
    """

    medicalAudience: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    aspect: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(MedicalWebPageInheritedProperties , MedicalWebPageProperties, TypedDict):
    pass


class MedicalWebPageBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MedicalWebPage",alias='@id')
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
        fields = {'medicalAudience': {'exclude': True}}
        fields = {'aspect': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MedicalWebPageProperties, MedicalWebPageInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MedicalWebPage"
    return model
    

MedicalWebPage = create_schema_org_model()


def create_medicalwebpage_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_medicalwebpage_model(model=model)
    return pydantic_type(model).schema_json()


