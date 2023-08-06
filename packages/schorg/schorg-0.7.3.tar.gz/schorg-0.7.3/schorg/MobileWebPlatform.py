"""
Represents the broad notion of 'mobile' browsers as a Web Platform.

https://schema.org/MobileWebPlatform
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MobileWebPlatformInheritedProperties(TypedDict):
    """Represents the broad notion of 'mobile' browsers as a Web Platform.

    References:
        https://schema.org/MobileWebPlatform
    Note:
        Model Depth 5
    Attributes:
    """


class MobileWebPlatformProperties(TypedDict):
    """Represents the broad notion of 'mobile' browsers as a Web Platform.

    References:
        https://schema.org/MobileWebPlatform
    Note:
        Model Depth 5
    Attributes:
    """


class MobileWebPlatformAllProperties(
    MobileWebPlatformInheritedProperties, MobileWebPlatformProperties, TypedDict
):
    pass


class MobileWebPlatformBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MobileWebPlatform", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MobileWebPlatformProperties,
        MobileWebPlatformInheritedProperties,
        MobileWebPlatformAllProperties,
    ] = MobileWebPlatformAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MobileWebPlatform"
    return model


MobileWebPlatform = create_schema_org_model()


def create_mobilewebplatform_model(
    model: Union[
        MobileWebPlatformProperties,
        MobileWebPlatformInheritedProperties,
        MobileWebPlatformAllProperties,
    ]
):
    _type = deepcopy(MobileWebPlatformAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MobileWebPlatformAllProperties):
    pydantic_type = create_mobilewebplatform_model(model=model)
    return pydantic_type(model).schema_json()
