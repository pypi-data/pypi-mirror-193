"""
A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.

https://schema.org/Pathology
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PathologyInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.

    References:
        https://schema.org/Pathology
    Note:
        Model Depth 6
    Attributes:
    """


class PathologyProperties(TypedDict):
    """A specific branch of medical science that is concerned with the study of the cause, origin and nature of a disease state, including its consequences as a result of manifestation of the disease. In clinical care, the term is used to designate a branch of medicine using laboratory tests to diagnose and determine the prognostic significance of illness.

    References:
        https://schema.org/Pathology
    Note:
        Model Depth 6
    Attributes:
    """


class PathologyAllProperties(
    PathologyInheritedProperties, PathologyProperties, TypedDict
):
    pass


class PathologyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Pathology", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PathologyProperties, PathologyInheritedProperties, PathologyAllProperties
    ] = PathologyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Pathology"
    return model


Pathology = create_schema_org_model()


def create_pathology_model(
    model: Union[
        PathologyProperties, PathologyInheritedProperties, PathologyAllProperties
    ]
):
    _type = deepcopy(PathologyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PathologyAllProperties):
    pydantic_type = create_pathology_model(model=model)
    return pydantic_type(model).schema_json()
