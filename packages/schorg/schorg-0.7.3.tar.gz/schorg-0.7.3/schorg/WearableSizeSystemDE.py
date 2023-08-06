"""
German size system for wearables.

https://schema.org/WearableSizeSystemDE
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemDEInheritedProperties(TypedDict):
    """German size system for wearables.

    References:
        https://schema.org/WearableSizeSystemDE
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemDEProperties(TypedDict):
    """German size system for wearables.

    References:
        https://schema.org/WearableSizeSystemDE
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemDEAllProperties(
    WearableSizeSystemDEInheritedProperties, WearableSizeSystemDEProperties, TypedDict
):
    pass


class WearableSizeSystemDEBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemDE", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemDEProperties,
        WearableSizeSystemDEInheritedProperties,
        WearableSizeSystemDEAllProperties,
    ] = WearableSizeSystemDEAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemDE"
    return model


WearableSizeSystemDE = create_schema_org_model()


def create_wearablesizesystemde_model(
    model: Union[
        WearableSizeSystemDEProperties,
        WearableSizeSystemDEInheritedProperties,
        WearableSizeSystemDEAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemDEAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeSystemDEAllProperties):
    pydantic_type = create_wearablesizesystemde_model(model=model)
    return pydantic_type(model).schema_json()
