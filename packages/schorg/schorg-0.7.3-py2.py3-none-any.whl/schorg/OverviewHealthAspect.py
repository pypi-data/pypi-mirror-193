"""
Overview of the content. Contains a summarized view of the topic with the most relevant information for an introduction.

https://schema.org/OverviewHealthAspect
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OverviewHealthAspectInheritedProperties(TypedDict):
    """Overview of the content. Contains a summarized view of the topic with the most relevant information for an introduction.

    References:
        https://schema.org/OverviewHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class OverviewHealthAspectProperties(TypedDict):
    """Overview of the content. Contains a summarized view of the topic with the most relevant information for an introduction.

    References:
        https://schema.org/OverviewHealthAspect
    Note:
        Model Depth 5
    Attributes:
    """


class OverviewHealthAspectAllProperties(
    OverviewHealthAspectInheritedProperties, OverviewHealthAspectProperties, TypedDict
):
    pass


class OverviewHealthAspectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="OverviewHealthAspect", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        OverviewHealthAspectProperties,
        OverviewHealthAspectInheritedProperties,
        OverviewHealthAspectAllProperties,
    ] = OverviewHealthAspectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OverviewHealthAspect"
    return model


OverviewHealthAspect = create_schema_org_model()


def create_overviewhealthaspect_model(
    model: Union[
        OverviewHealthAspectProperties,
        OverviewHealthAspectInheritedProperties,
        OverviewHealthAspectAllProperties,
    ]
):
    _type = deepcopy(OverviewHealthAspectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: OverviewHealthAspectAllProperties):
    pydantic_type = create_overviewhealthaspect_model(model=model)
    return pydantic_type(model).schema_json()
