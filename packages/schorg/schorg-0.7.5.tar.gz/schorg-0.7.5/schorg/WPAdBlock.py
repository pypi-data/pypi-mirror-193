"""
An advertising section of the page.

https://schema.org/WPAdBlock
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class WPAdBlockAllProperties(
    WPAdBlockInheritedProperties, WPAdBlockProperties, TypedDict
):
    pass


class WPAdBlockBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WPAdBlock", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"xpath": {"exclude": True}}
        fields = {"cssSelector": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        WPAdBlockProperties, WPAdBlockInheritedProperties, WPAdBlockAllProperties
    ] = WPAdBlockAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WPAdBlock"
    return model


WPAdBlock = create_schema_org_model()


def create_wpadblock_model(
    model: Union[
        WPAdBlockProperties, WPAdBlockInheritedProperties, WPAdBlockAllProperties
    ]
):
    _type = deepcopy(WPAdBlockAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WPAdBlock. Please see: https://schema.org/WPAdBlock"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WPAdBlockAllProperties):
    pydantic_type = create_wpadblock_model(model=model)
    return pydantic_type(model).schema_json()
