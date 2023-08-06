"""
Size group "Misses" (also known as "Missy") for wearables.

https://schema.org/WearableSizeGroupMisses
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupMissesInheritedProperties(TypedDict):
    """Size group "Misses" (also known as "Missy") for wearables.

    References:
        https://schema.org/WearableSizeGroupMisses
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupMissesProperties(TypedDict):
    """Size group "Misses" (also known as "Missy") for wearables.

    References:
        https://schema.org/WearableSizeGroupMisses
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupMissesAllProperties(
    WearableSizeGroupMissesInheritedProperties,
    WearableSizeGroupMissesProperties,
    TypedDict,
):
    pass


class WearableSizeGroupMissesBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupMisses", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupMissesProperties,
        WearableSizeGroupMissesInheritedProperties,
        WearableSizeGroupMissesAllProperties,
    ] = WearableSizeGroupMissesAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupMisses"
    return model


WearableSizeGroupMisses = create_schema_org_model()


def create_wearablesizegroupmisses_model(
    model: Union[
        WearableSizeGroupMissesProperties,
        WearableSizeGroupMissesInheritedProperties,
        WearableSizeGroupMissesAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupMissesAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeGroupMissesAllProperties):
    pydantic_type = create_wearablesizegroupmisses_model(model=model)
    return pydantic_type(model).schema_json()
