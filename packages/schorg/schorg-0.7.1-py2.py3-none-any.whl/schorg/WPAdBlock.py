"""
An advertising section of the page.

https://schema.org/WPAdBlock
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WPAdBlockInheritedProperties(TypedDict):
    """An advertising section of the page.

    References:
        https://schema.org/WPAdBlock
    Note:
        Model Depth 4
    Attributes:
        xpath: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
        cssSelector: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
    """

    xpath: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cssSelector: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    


class WPAdBlockProperties(TypedDict):
    """An advertising section of the page.

    References:
        https://schema.org/WPAdBlock
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(WPAdBlockInheritedProperties , WPAdBlockProperties, TypedDict):
    pass


class WPAdBlockBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WPAdBlock",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'xpath': {'exclude': True}}
        fields = {'cssSelector': {'exclude': True}}
        


def create_schema_org_model(type_: Union[WPAdBlockProperties, WPAdBlockInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WPAdBlock"
    return model
    

WPAdBlock = create_schema_org_model()


def create_wpadblock_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wpadblock_model(model=model)
    return pydantic_type(model).schema_json()


