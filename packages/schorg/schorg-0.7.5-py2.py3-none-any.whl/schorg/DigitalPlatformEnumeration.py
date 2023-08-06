"""
Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]. It is not supposed to be comprehensive - when a suitable code is not enumerated here, textual or URL values can be used instead. These codes are at a fairly high level and do not deal with versioning and other nuance. Additional codes can be suggested [in github](https://github.com/schemaorg/schemaorg/issues/3057). 

https://schema.org/DigitalPlatformEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DigitalPlatformEnumerationInheritedProperties(TypedDict):
    """Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]. It is not supposed to be comprehensive - when a suitable code is not enumerated here, textual or URL values can be used instead. These codes are at a fairly high level and do not deal with versioning and other nuance. Additional codes can be suggested [in github](https://github.com/schemaorg/schemaorg/issues/3057).

    References:
        https://schema.org/DigitalPlatformEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[str, SchemaOrgObj]], str, SchemaOrgObj]]


class DigitalPlatformEnumerationProperties(TypedDict):
    """Enumerates some common technology platforms, for use with properties such as [[actionPlatform]]. It is not supposed to be comprehensive - when a suitable code is not enumerated here, textual or URL values can be used instead. These codes are at a fairly high level and do not deal with versioning and other nuance. Additional codes can be suggested [in github](https://github.com/schemaorg/schemaorg/issues/3057).

    References:
        https://schema.org/DigitalPlatformEnumeration
    Note:
        Model Depth 4
    Attributes:
    """


class DigitalPlatformEnumerationAllProperties(
    DigitalPlatformEnumerationInheritedProperties,
    DigitalPlatformEnumerationProperties,
    TypedDict,
):
    pass


class DigitalPlatformEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DigitalPlatformEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:

        fields = {"supersededBy": {"exclude": True}}


def create_schema_org_model(
    type_: Union[
        DigitalPlatformEnumerationProperties,
        DigitalPlatformEnumerationInheritedProperties,
        DigitalPlatformEnumerationAllProperties,
    ] = DigitalPlatformEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DigitalPlatformEnumeration"
    return model


DigitalPlatformEnumeration = create_schema_org_model()


def create_digitalplatformenumeration_model(
    model: Union[
        DigitalPlatformEnumerationProperties,
        DigitalPlatformEnumerationInheritedProperties,
        DigitalPlatformEnumerationAllProperties,
    ]
):
    _type = deepcopy(DigitalPlatformEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of DigitalPlatformEnumeration. Please see: https://schema.org/DigitalPlatformEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: DigitalPlatformEnumerationAllProperties):
    pydantic_type = create_digitalplatformenumeration_model(model=model)
    return pydantic_type(model).schema_json()
