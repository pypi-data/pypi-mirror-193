"""
Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.

https://schema.org/GraphicNovel
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GraphicNovelInheritedProperties(TypedDict):
    """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.

    References:
        https://schema.org/GraphicNovel
    Note:
        Model Depth 5
    Attributes:
    """


class GraphicNovelProperties(TypedDict):
    """Book format: GraphicNovel. May represent a bound collection of ComicIssue instances.

    References:
        https://schema.org/GraphicNovel
    Note:
        Model Depth 5
    Attributes:
    """


class GraphicNovelAllProperties(
    GraphicNovelInheritedProperties, GraphicNovelProperties, TypedDict
):
    pass


class GraphicNovelBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GraphicNovel", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GraphicNovelProperties,
        GraphicNovelInheritedProperties,
        GraphicNovelAllProperties,
    ] = GraphicNovelAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GraphicNovel"
    return model


GraphicNovel = create_schema_org_model()


def create_graphicnovel_model(
    model: Union[
        GraphicNovelProperties,
        GraphicNovelInheritedProperties,
        GraphicNovelAllProperties,
    ]
):
    _type = deepcopy(GraphicNovelAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: GraphicNovelAllProperties):
    pydantic_type = create_graphicnovel_model(model=model)
    return pydantic_type(model).schema_json()
