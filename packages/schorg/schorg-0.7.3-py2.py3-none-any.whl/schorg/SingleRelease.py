"""
SingleRelease.

https://schema.org/SingleRelease
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SingleReleaseInheritedProperties(TypedDict):
    """SingleRelease.

    References:
        https://schema.org/SingleRelease
    Note:
        Model Depth 5
    Attributes:
    """


class SingleReleaseProperties(TypedDict):
    """SingleRelease.

    References:
        https://schema.org/SingleRelease
    Note:
        Model Depth 5
    Attributes:
    """


class SingleReleaseAllProperties(
    SingleReleaseInheritedProperties, SingleReleaseProperties, TypedDict
):
    pass


class SingleReleaseBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SingleRelease", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SingleReleaseProperties,
        SingleReleaseInheritedProperties,
        SingleReleaseAllProperties,
    ] = SingleReleaseAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SingleRelease"
    return model


SingleRelease = create_schema_org_model()


def create_singlerelease_model(
    model: Union[
        SingleReleaseProperties,
        SingleReleaseInheritedProperties,
        SingleReleaseAllProperties,
    ]
):
    _type = deepcopy(SingleReleaseAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: SingleReleaseAllProperties):
    pydantic_type = create_singlerelease_model(model=model)
    return pydantic_type(model).schema_json()
