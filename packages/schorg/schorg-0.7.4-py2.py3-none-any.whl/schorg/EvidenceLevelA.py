"""
Data derived from multiple randomized clinical trials or meta-analyses.

https://schema.org/EvidenceLevelA
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EvidenceLevelAInheritedProperties(TypedDict):
    """Data derived from multiple randomized clinical trials or meta-analyses.

    References:
        https://schema.org/EvidenceLevelA
    Note:
        Model Depth 6
    Attributes:
    """


class EvidenceLevelAProperties(TypedDict):
    """Data derived from multiple randomized clinical trials or meta-analyses.

    References:
        https://schema.org/EvidenceLevelA
    Note:
        Model Depth 6
    Attributes:
    """


class EvidenceLevelAAllProperties(
    EvidenceLevelAInheritedProperties, EvidenceLevelAProperties, TypedDict
):
    pass


class EvidenceLevelABaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="EvidenceLevelA", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        EvidenceLevelAProperties,
        EvidenceLevelAInheritedProperties,
        EvidenceLevelAAllProperties,
    ] = EvidenceLevelAAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "EvidenceLevelA"
    return model


EvidenceLevelA = create_schema_org_model()


def create_evidencelevela_model(
    model: Union[
        EvidenceLevelAProperties,
        EvidenceLevelAInheritedProperties,
        EvidenceLevelAAllProperties,
    ]
):
    _type = deepcopy(EvidenceLevelAAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of EvidenceLevelAAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: EvidenceLevelAAllProperties):
    pydantic_type = create_evidencelevela_model(model=model)
    return pydantic_type(model).schema_json()
