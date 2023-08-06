"""
Data derived from a single randomized trial, or nonrandomized studies.

https://schema.org/EvidenceLevelB
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EvidenceLevelBInheritedProperties(TypedDict):
    """Data derived from a single randomized trial, or nonrandomized studies.

    References:
        https://schema.org/EvidenceLevelB
    Note:
        Model Depth 6
    Attributes:
    """


class EvidenceLevelBProperties(TypedDict):
    """Data derived from a single randomized trial, or nonrandomized studies.

    References:
        https://schema.org/EvidenceLevelB
    Note:
        Model Depth 6
    Attributes:
    """


class EvidenceLevelBAllProperties(
    EvidenceLevelBInheritedProperties, EvidenceLevelBProperties, TypedDict
):
    pass


class EvidenceLevelBBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EvidenceLevelB", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EvidenceLevelBProperties,
        EvidenceLevelBInheritedProperties,
        EvidenceLevelBAllProperties,
    ] = EvidenceLevelBAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EvidenceLevelB"
    return model


EvidenceLevelB = create_schema_org_model()


def create_evidencelevelb_model(
    model: Union[
        EvidenceLevelBProperties,
        EvidenceLevelBInheritedProperties,
        EvidenceLevelBAllProperties,
    ]
):
    _type = deepcopy(EvidenceLevelBAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EvidenceLevelBAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EvidenceLevelBAllProperties):
    pydantic_type = create_evidencelevelb_model(model=model)
    return pydantic_type(model).schema_json()
