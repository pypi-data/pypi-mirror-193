"""
Content about the effectiveness-related aspects of a health topic.

https://schema.org/EffectivenessHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EffectivenessHealthAspectInheritedProperties(TypedDict):
    """Content about the effectiveness-related aspects of a health topic.

    References:
        https://schema.org/EffectivenessHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class EffectivenessHealthAspectProperties(TypedDict):
    """Content about the effectiveness-related aspects of a health topic.

    References:
        https://schema.org/EffectivenessHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class EffectivenessHealthAspectAllProperties(
    EffectivenessHealthAspectInheritedProperties,
    EffectivenessHealthAspectProperties,
    TypedDict,
):
    pass


class EffectivenessHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EffectivenessHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EffectivenessHealthAspectProperties,
        EffectivenessHealthAspectInheritedProperties,
        EffectivenessHealthAspectAllProperties,
    ] = EffectivenessHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EffectivenessHealthAspect"
    return model


EffectivenessHealthAspect = create_schema_org_model()


def create_effectivenesshealthaspect_model(
    model: Union[
        EffectivenessHealthAspectProperties,
        EffectivenessHealthAspectInheritedProperties,
        EffectivenessHealthAspectAllProperties,
    ]
):
    _type = deepcopy(EffectivenessHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EffectivenessHealthAspectAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EffectivenessHealthAspectAllProperties):
    pydantic_type = create_effectivenesshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
