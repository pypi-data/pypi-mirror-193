"""
Content about how to screen or further filter a topic.

https://schema.org/ScreeningHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ScreeningHealthAspectInheritedProperties(TypedDict):
    """Content about how to screen or further filter a topic.

    References:
        https://schema.org/ScreeningHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class ScreeningHealthAspectProperties(TypedDict):
    """Content about how to screen or further filter a topic.

    References:
        https://schema.org/ScreeningHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class ScreeningHealthAspectAllProperties(
    ScreeningHealthAspectInheritedProperties, ScreeningHealthAspectProperties, TypedDict
):
    pass


class ScreeningHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ScreeningHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ScreeningHealthAspectProperties,
        ScreeningHealthAspectInheritedProperties,
        ScreeningHealthAspectAllProperties,
    ] = ScreeningHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ScreeningHealthAspect"
    return model


ScreeningHealthAspect = create_schema_org_model()


def create_screeninghealthaspect_model(
    model: Union[
        ScreeningHealthAspectProperties,
        ScreeningHealthAspectInheritedProperties,
        ScreeningHealthAspectAllProperties,
    ]
):
    _type = deepcopy(ScreeningHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ScreeningHealthAspectAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ScreeningHealthAspectAllProperties):
    pydantic_type = create_screeninghealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
