"""
A navigation element of the page.

https://schema.org/SiteNavigationElement
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SiteNavigationElementInheritedProperties(TypedDict):
    """A navigation element of the page.

    References:
        https://schema.org/SiteNavigationElement
    Note:
        Model Depth 4
    Attributes:
        xpath: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
        cssSelector: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
    """

    xpath: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cssSelector: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class SiteNavigationElementProperties(TypedDict):
    """A navigation element of the page.

    References:
        https://schema.org/SiteNavigationElement
    Note:
        Model Depth 4
    Attributes:
    """


class SiteNavigationElementAllProperties(
    SiteNavigationElementInheritedProperties, SiteNavigationElementProperties, TypedDict
):
    pass


class SiteNavigationElementBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SiteNavigationElement", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"xpath": {"exclude": True}}
        fields = {"cssSelector": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        SiteNavigationElementProperties,
        SiteNavigationElementInheritedProperties,
        SiteNavigationElementAllProperties,
    ] = SiteNavigationElementAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SiteNavigationElement"
    return model


SiteNavigationElement = create_schema_org_model()


def create_sitenavigationelement_model(
    model: Union[
        SiteNavigationElementProperties,
        SiteNavigationElementInheritedProperties,
        SiteNavigationElementAllProperties,
    ]
):
    _type = deepcopy(SiteNavigationElementAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of SiteNavigationElementAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SiteNavigationElementAllProperties):
    pydantic_type = create_sitenavigationelement_model(model=model)
    return pydantic_type(model).schema_json()
