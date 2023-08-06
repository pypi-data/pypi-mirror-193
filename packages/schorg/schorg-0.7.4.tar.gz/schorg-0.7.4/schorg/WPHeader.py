"""
The header section of the page.

https://schema.org/WPHeader
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WPHeaderInheritedProperties(TypedDict):
    """The header section of the page.

    References:
        https://schema.org/WPHeader
    Note:
        Model Depth 4
    Attributes:
        xpath: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
        cssSelector: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
    """

    xpath: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    cssSelector: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]


class WPHeaderProperties(TypedDict):
    """The header section of the page.

    References:
        https://schema.org/WPHeader
    Note:
        Model Depth 4
    Attributes:
    """


class WPHeaderAllProperties(WPHeaderInheritedProperties, WPHeaderProperties, TypedDict):
    pass


class WPHeaderBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WPHeader", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"xpath": {"exclude": True}}
        fields = {"cssSelector": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        WPHeaderProperties, WPHeaderInheritedProperties, WPHeaderAllProperties
    ] = WPHeaderAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WPHeader"
    return model


WPHeader = create_schema_org_model()


def create_wpheader_model(
    model: Union[WPHeaderProperties, WPHeaderInheritedProperties, WPHeaderAllProperties]
):
    _type = deepcopy(WPHeaderAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WPHeaderAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WPHeaderAllProperties):
    pydantic_type = create_wpheader_model(model=model)
    return pydantic_type(model).schema_json()
