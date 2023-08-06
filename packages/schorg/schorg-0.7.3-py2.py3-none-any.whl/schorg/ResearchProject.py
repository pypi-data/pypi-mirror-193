"""
A Research project.

https://schema.org/ResearchProject
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ResearchProjectInheritedProperties(TypedDict):
    """A Research project.

    References:
        https://schema.org/ResearchProject
    Note:
        Model Depth 4
    Attributes:
    """


class ResearchProjectProperties(TypedDict):
    """A Research project.

    References:
        https://schema.org/ResearchProject
    Note:
        Model Depth 4
    Attributes:
    """


class ResearchProjectAllProperties(
    ResearchProjectInheritedProperties, ResearchProjectProperties, TypedDict
):
    pass


class ResearchProjectBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ResearchProject", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ResearchProjectProperties,
        ResearchProjectInheritedProperties,
        ResearchProjectAllProperties,
    ] = ResearchProjectAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ResearchProject"
    return model


ResearchProject = create_schema_org_model()


def create_researchproject_model(
    model: Union[
        ResearchProjectProperties,
        ResearchProjectInheritedProperties,
        ResearchProjectAllProperties,
    ]
):
    _type = deepcopy(ResearchProjectAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ResearchProjectAllProperties):
    pydantic_type = create_researchproject_model(model=model)
    return pydantic_type(model).schema_json()
