"""
Content about the safety-related aspects of a health topic.

https://schema.org/SafetyHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SafetyHealthAspectInheritedProperties(TypedDict):
    """Content about the safety-related aspects of a health topic.

    References:
        https://schema.org/SafetyHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SafetyHealthAspectProperties(TypedDict):
    """Content about the safety-related aspects of a health topic.

    References:
        https://schema.org/SafetyHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SafetyHealthAspectAllProperties(
    SafetyHealthAspectInheritedProperties, SafetyHealthAspectProperties, TypedDict
):
    pass


class SafetyHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SafetyHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SafetyHealthAspectProperties,
        SafetyHealthAspectInheritedProperties,
        SafetyHealthAspectAllProperties,
    ] = SafetyHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SafetyHealthAspect"
    return model


SafetyHealthAspect = create_schema_org_model()


def create_safetyhealthaspect_model(
    model: Union[
        SafetyHealthAspectProperties,
        SafetyHealthAspectInheritedProperties,
        SafetyHealthAspectAllProperties,
    ]
):
    _type = deepcopy(SafetyHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SafetyHealthAspectAllProperties):
    pydantic_type = create_safetyhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
