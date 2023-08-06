"""
Represents the generic notion of the Web Platform. More specific codes include [[MobileWebPlatform]] and [[DesktopWebPlatform]], as an incomplete list. 

https://schema.org/GenericWebPlatform
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GenericWebPlatformInheritedProperties(TypedDict):
    """Represents the generic notion of the Web Platform. More specific codes include [[MobileWebPlatform]] and [[DesktopWebPlatform]], as an incomplete list.

    References:
        https://schema.org/GenericWebPlatform
    Note:
        Model Depth 5
    Attributes:
    """


class GenericWebPlatformProperties(TypedDict):
    """Represents the generic notion of the Web Platform. More specific codes include [[MobileWebPlatform]] and [[DesktopWebPlatform]], as an incomplete list.

    References:
        https://schema.org/GenericWebPlatform
    Note:
        Model Depth 5
    Attributes:
    """


class GenericWebPlatformAllProperties(
    GenericWebPlatformInheritedProperties, GenericWebPlatformProperties, TypedDict
):
    pass


class GenericWebPlatformBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GenericWebPlatform", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GenericWebPlatformProperties,
        GenericWebPlatformInheritedProperties,
        GenericWebPlatformAllProperties,
    ] = GenericWebPlatformAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GenericWebPlatform"
    return model


GenericWebPlatform = create_schema_org_model()


def create_genericwebplatform_model(
    model: Union[
        GenericWebPlatformProperties,
        GenericWebPlatformInheritedProperties,
        GenericWebPlatformAllProperties,
    ]
):
    _type = deepcopy(GenericWebPlatformAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of GenericWebPlatform. Please see: https://schema.org/GenericWebPlatform"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: GenericWebPlatformAllProperties):
    pydantic_type = create_genericwebplatform_model(model=model)
    return pydantic_type(model).schema_json()
