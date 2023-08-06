"""
A sidebar section of the page.

https://schema.org/WPSideBar
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WPSideBarInheritedProperties(TypedDict):
    """A sidebar section of the page.

    References:
        https://schema.org/WPSideBar
    Note:
        Model Depth 4
    Attributes:
        xpath: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
        cssSelector: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
    """

    xpath: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cssSelector: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class WPSideBarProperties(TypedDict):
    """A sidebar section of the page.

    References:
        https://schema.org/WPSideBar
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(WPSideBarInheritedProperties , WPSideBarProperties, TypedDict):
    pass


class WPSideBarBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WPSideBar",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'xpath': {'exclude': True}}
        fields = {'cssSelector': {'exclude': True}}
        


def create_schema_org_model(type_: Union[WPSideBarProperties, WPSideBarInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WPSideBar"
    return model
    

WPSideBar = create_schema_org_model()


def create_wpsidebar_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wpsidebar_model(model=model)
    return pydantic_type(model).schema_json()


