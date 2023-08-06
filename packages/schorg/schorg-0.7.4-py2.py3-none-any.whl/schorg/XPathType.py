"""
Text representing an XPath (typically but not necessarily version 1.0).

https://schema.org/XPathType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class XPathTypeInheritedProperties(TypedDict):
    """Text representing an XPath (typically but not necessarily version 1.0).

    References:
        https://schema.org/XPathType
    Note:
        Model Depth 6
    Attributes:
    """


class XPathTypeProperties(TypedDict):
    """Text representing an XPath (typically but not necessarily version 1.0).

    References:
        https://schema.org/XPathType
    Note:
        Model Depth 6
    Attributes:
    """


class XPathTypeAllProperties(
    XPathTypeInheritedProperties, XPathTypeProperties, TypedDict
):
    pass


class XPathTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="XPathType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        XPathTypeProperties, XPathTypeInheritedProperties, XPathTypeAllProperties
    ] = XPathTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "XPathType"
    return model


XPathType = create_schema_org_model()


def create_xpathtype_model(
    model: Union[
        XPathTypeProperties, XPathTypeInheritedProperties, XPathTypeAllProperties
    ]
):
    _type = deepcopy(XPathTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of XPathTypeAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: XPathTypeAllProperties):
    pydantic_type = create_xpathtype_model(model=model)
    return pydantic_type(model).schema_json()
