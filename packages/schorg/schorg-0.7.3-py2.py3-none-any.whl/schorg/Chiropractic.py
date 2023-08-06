"""
A system of medicine focused on the relationship between the body's structure, mainly the spine, and its functioning.

https://schema.org/Chiropractic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ChiropracticInheritedProperties(TypedDict):
    """A system of medicine focused on the relationship between the body's structure, mainly the spine, and its functioning.

    References:
        https://schema.org/Chiropractic
    Note:
        Model Depth 6
    Attributes:
    """


class ChiropracticProperties(TypedDict):
    """A system of medicine focused on the relationship between the body's structure, mainly the spine, and its functioning.

    References:
        https://schema.org/Chiropractic
    Note:
        Model Depth 6
    Attributes:
    """


class ChiropracticAllProperties(
    ChiropracticInheritedProperties, ChiropracticProperties, TypedDict
):
    pass


class ChiropracticBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Chiropractic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ChiropracticProperties,
        ChiropracticInheritedProperties,
        ChiropracticAllProperties,
    ] = ChiropracticAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Chiropractic"
    return model


Chiropractic = create_schema_org_model()


def create_chiropractic_model(
    model: Union[
        ChiropracticProperties,
        ChiropracticInheritedProperties,
        ChiropracticAllProperties,
    ]
):
    _type = deepcopy(ChiropracticAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ChiropracticAllProperties):
    pydantic_type = create_chiropractic_model(model=model)
    return pydantic_type(model).schema_json()
