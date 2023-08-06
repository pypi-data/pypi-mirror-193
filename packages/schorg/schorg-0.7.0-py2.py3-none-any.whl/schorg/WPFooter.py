"""
The footer section of the page.

https://schema.org/WPFooter
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WPFooterInheritedProperties(TypedDict):
    """The footer section of the page.

    References:
        https://schema.org/WPFooter
    Note:
        Model Depth 4
    Attributes:
        xpath: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
        cssSelector: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
    """

    xpath: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cssSelector: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class WPFooterProperties(TypedDict):
    """The footer section of the page.

    References:
        https://schema.org/WPFooter
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(WPFooterInheritedProperties , WPFooterProperties, TypedDict):
    pass


class WPFooterBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WPFooter",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'xpath': {'exclude': True}}
        fields = {'cssSelector': {'exclude': True}}
        


def create_schema_org_model(type_: Union[WPFooterProperties, WPFooterInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WPFooter"
    return model
    

WPFooter = create_schema_org_model()


def create_wpfooter_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wpfooter_model(model=model)
    return pydantic_type(model).schema_json()


