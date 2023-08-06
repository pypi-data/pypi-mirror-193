"""
Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.

https://schema.org/Podiatric
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class PodiatricInheritedProperties(TypedDict):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.

    References:
        https://schema.org/Podiatric
    Note:
        Model Depth 5
    Attributes:
    """


class PodiatricProperties(TypedDict):
    """Podiatry is the care of the human foot, especially the diagnosis and treatment of foot disorders.

    References:
        https://schema.org/Podiatric
    Note:
        Model Depth 5
    Attributes:
    """


class PodiatricAllProperties(
    PodiatricInheritedProperties, PodiatricProperties, TypedDict
):
    pass


class PodiatricBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Podiatric", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        PodiatricProperties, PodiatricInheritedProperties, PodiatricAllProperties
    ] = PodiatricAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Podiatric"
    return model


Podiatric = create_schema_org_model()


def create_podiatric_model(
    model: Union[
        PodiatricProperties, PodiatricInheritedProperties, PodiatricAllProperties
    ]
):
    _type = deepcopy(PodiatricAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of PodiatricAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: PodiatricAllProperties):
    pydantic_type = create_podiatric_model(model=model)
    return pydantic_type(model).schema_json()
