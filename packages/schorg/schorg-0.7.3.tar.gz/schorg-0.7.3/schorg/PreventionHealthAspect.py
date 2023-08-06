"""
Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic.

https://schema.org/PreventionHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PreventionHealthAspectInheritedProperties(TypedDict):
    """Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic.

    References:
        https://schema.org/PreventionHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class PreventionHealthAspectProperties(TypedDict):
    """Information about actions or measures that can be taken to avoid getting the topic or reaching a critical situation related to the topic.

    References:
        https://schema.org/PreventionHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class PreventionHealthAspectAllProperties(
    PreventionHealthAspectInheritedProperties,
    PreventionHealthAspectProperties,
    TypedDict,
):
    pass


class PreventionHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="PreventionHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PreventionHealthAspectProperties,
        PreventionHealthAspectInheritedProperties,
        PreventionHealthAspectAllProperties,
    ] = PreventionHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "PreventionHealthAspect"
    return model


PreventionHealthAspect = create_schema_org_model()


def create_preventionhealthaspect_model(
    model: Union[
        PreventionHealthAspectProperties,
        PreventionHealthAspectInheritedProperties,
        PreventionHealthAspectAllProperties,
    ]
):
    _type = deepcopy(PreventionHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PreventionHealthAspectAllProperties):
    pydantic_type = create_preventionhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
