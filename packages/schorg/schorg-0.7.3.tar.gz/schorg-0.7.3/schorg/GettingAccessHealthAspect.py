"""
Content that discusses practical and policy aspects for getting access to specific kinds of healthcare (e.g. distribution mechanisms for vaccines).

https://schema.org/GettingAccessHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GettingAccessHealthAspectInheritedProperties(TypedDict):
    """Content that discusses practical and policy aspects for getting access to specific kinds of healthcare (e.g. distribution mechanisms for vaccines).

    References:
        https://schema.org/GettingAccessHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class GettingAccessHealthAspectProperties(TypedDict):
    """Content that discusses practical and policy aspects for getting access to specific kinds of healthcare (e.g. distribution mechanisms for vaccines).

    References:
        https://schema.org/GettingAccessHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class GettingAccessHealthAspectAllProperties(
    GettingAccessHealthAspectInheritedProperties,
    GettingAccessHealthAspectProperties,
    TypedDict,
):
    pass


class GettingAccessHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GettingAccessHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GettingAccessHealthAspectProperties,
        GettingAccessHealthAspectInheritedProperties,
        GettingAccessHealthAspectAllProperties,
    ] = GettingAccessHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GettingAccessHealthAspect"
    return model


GettingAccessHealthAspect = create_schema_org_model()


def create_gettingaccesshealthaspect_model(
    model: Union[
        GettingAccessHealthAspectProperties,
        GettingAccessHealthAspectInheritedProperties,
        GettingAccessHealthAspectAllProperties,
    ]
):
    _type = deepcopy(GettingAccessHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GettingAccessHealthAspectAllProperties):
    pydantic_type = create_gettingaccesshealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
