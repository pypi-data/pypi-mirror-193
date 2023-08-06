"""
French size system for wearables.

https://schema.org/WearableSizeSystemFR
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemFRInheritedProperties(TypedDict):
    """French size system for wearables.

    References:
        https://schema.org/WearableSizeSystemFR
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemFRProperties(TypedDict):
    """French size system for wearables.

    References:
        https://schema.org/WearableSizeSystemFR
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemFRAllProperties(
    WearableSizeSystemFRInheritedProperties, WearableSizeSystemFRProperties, TypedDict
):
    pass


class WearableSizeSystemFRBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemFR", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemFRProperties,
        WearableSizeSystemFRInheritedProperties,
        WearableSizeSystemFRAllProperties,
    ] = WearableSizeSystemFRAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemFR"
    return model


WearableSizeSystemFR = create_schema_org_model()


def create_wearablesizesystemfr_model(
    model: Union[
        WearableSizeSystemFRProperties,
        WearableSizeSystemFRInheritedProperties,
        WearableSizeSystemFRAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemFRAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableSizeSystemFRAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeSystemFRAllProperties):
    pydantic_type = create_wearablesizesystemfr_model(model=model)
    return pydantic_type(model).schema_json()
