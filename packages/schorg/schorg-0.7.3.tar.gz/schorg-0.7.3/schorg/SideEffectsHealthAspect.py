"""
Side effects that can be observed from the usage of the topic.

https://schema.org/SideEffectsHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SideEffectsHealthAspectInheritedProperties(TypedDict):
    """Side effects that can be observed from the usage of the topic.

    References:
        https://schema.org/SideEffectsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SideEffectsHealthAspectProperties(TypedDict):
    """Side effects that can be observed from the usage of the topic.

    References:
        https://schema.org/SideEffectsHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class SideEffectsHealthAspectAllProperties(
    SideEffectsHealthAspectInheritedProperties,
    SideEffectsHealthAspectProperties,
    TypedDict,
):
    pass


class SideEffectsHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SideEffectsHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SideEffectsHealthAspectProperties,
        SideEffectsHealthAspectInheritedProperties,
        SideEffectsHealthAspectAllProperties,
    ] = SideEffectsHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SideEffectsHealthAspect"
    return model


SideEffectsHealthAspect = create_schema_org_model()


def create_sideeffectshealthaspect_model(
    model: Union[
        SideEffectsHealthAspectProperties,
        SideEffectsHealthAspectInheritedProperties,
        SideEffectsHealthAspectAllProperties,
    ]
):
    _type = deepcopy(SideEffectsHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SideEffectsHealthAspectAllProperties):
    pydantic_type = create_sideeffectshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
