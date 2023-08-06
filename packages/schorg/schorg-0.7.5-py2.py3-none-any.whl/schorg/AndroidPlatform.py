"""
Represents the broad notion of Android-based operating systems.

https://schema.org/AndroidPlatform
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AndroidPlatformInheritedProperties(TypedDict):
    """Represents the broad notion of Android-based operating systems.

    References:
        https://schema.org/AndroidPlatform
    Note:
        Model Depth 5
    Attributes:
    """


class AndroidPlatformProperties(TypedDict):
    """Represents the broad notion of Android-based operating systems.

    References:
        https://schema.org/AndroidPlatform
    Note:
        Model Depth 5
    Attributes:
    """


class AndroidPlatformAllProperties(
    AndroidPlatformInheritedProperties, AndroidPlatformProperties, TypedDict
):
    pass


class AndroidPlatformBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AndroidPlatform", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AndroidPlatformProperties,
        AndroidPlatformInheritedProperties,
        AndroidPlatformAllProperties,
    ] = AndroidPlatformAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AndroidPlatform"
    return model


AndroidPlatform = create_schema_org_model()


def create_androidplatform_model(
    model: Union[
        AndroidPlatformProperties,
        AndroidPlatformInheritedProperties,
        AndroidPlatformAllProperties,
    ]
):
    _type = deepcopy(AndroidPlatformAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of AndroidPlatform. Please see: https://schema.org/AndroidPlatform"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: AndroidPlatformAllProperties):
    pydantic_type = create_androidplatform_model(model=model)
    return pydantic_type(model).schema_json()
