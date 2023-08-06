"""
Represents the broad notion of 'desktop' browsers as a Web Platform.

https://schema.org/DesktopWebPlatform
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DesktopWebPlatformInheritedProperties(TypedDict):
    """Represents the broad notion of 'desktop' browsers as a Web Platform.

    References:
        https://schema.org/DesktopWebPlatform
    Note:
        Model Depth 5
    Attributes:
    """


class DesktopWebPlatformProperties(TypedDict):
    """Represents the broad notion of 'desktop' browsers as a Web Platform.

    References:
        https://schema.org/DesktopWebPlatform
    Note:
        Model Depth 5
    Attributes:
    """


class DesktopWebPlatformAllProperties(
    DesktopWebPlatformInheritedProperties, DesktopWebPlatformProperties, TypedDict
):
    pass


class DesktopWebPlatformBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DesktopWebPlatform", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DesktopWebPlatformProperties,
        DesktopWebPlatformInheritedProperties,
        DesktopWebPlatformAllProperties,
    ] = DesktopWebPlatformAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DesktopWebPlatform"
    return model


DesktopWebPlatform = create_schema_org_model()


def create_desktopwebplatform_model(
    model: Union[
        DesktopWebPlatformProperties,
        DesktopWebPlatformInheritedProperties,
        DesktopWebPlatformAllProperties,
    ]
):
    _type = deepcopy(DesktopWebPlatformAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DesktopWebPlatformAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DesktopWebPlatformAllProperties):
    pydantic_type = create_desktopwebplatform_model(model=model)
    return pydantic_type(model).schema_json()
