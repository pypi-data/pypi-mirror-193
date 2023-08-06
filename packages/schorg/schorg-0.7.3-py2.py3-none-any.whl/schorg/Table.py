"""
A table on a Web page.

https://schema.org/Table
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class TableInheritedProperties(TypedDict):
    """A table on a Web page.

    References:
        https://schema.org/Table
    Note:
        Model Depth 4
    Attributes:
        xpath: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): An XPath, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
        cssSelector: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): A CSS selector, e.g. of a [[SpeakableSpecification]] or [[WebPageElement]]. In the latter case, multiple matches within a page can constitute a single conceptual "Web page element".
    """

    xpath: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]
    cssSelector: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class TableProperties(TypedDict):
    """A table on a Web page.

    References:
        https://schema.org/Table
    Note:
        Model Depth 4
    Attributes:
    """


class TableAllProperties(TableInheritedProperties, TableProperties, TypedDict):
    pass


class TableBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Table", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"xpath": {"exclude": True}}
        fields = {"cssSelector": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        TableProperties, TableInheritedProperties, TableAllProperties
    ] = TableAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Table"
    return model


Table = create_schema_org_model()


def create_table_model(
    model: Union[TableProperties, TableInheritedProperties, TableAllProperties]
):
    _type = deepcopy(TableAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: TableAllProperties):
    pydantic_type = create_table_model(model=model)
    return pydantic_type(model).schema_json()
