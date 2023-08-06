"""
Brazilian size system for wearables.

https://schema.org/WearableSizeSystemBR
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemBRInheritedProperties(TypedDict):
    """Brazilian size system for wearables.

    References:
        https://schema.org/WearableSizeSystemBR
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemBRProperties(TypedDict):
    """Brazilian size system for wearables.

    References:
        https://schema.org/WearableSizeSystemBR
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemBRAllProperties(
    WearableSizeSystemBRInheritedProperties, WearableSizeSystemBRProperties, TypedDict
):
    pass


class WearableSizeSystemBRBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemBR", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemBRProperties,
        WearableSizeSystemBRInheritedProperties,
        WearableSizeSystemBRAllProperties,
    ] = WearableSizeSystemBRAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemBR"
    return model


WearableSizeSystemBR = create_schema_org_model()


def create_wearablesizesystembr_model(
    model: Union[
        WearableSizeSystemBRProperties,
        WearableSizeSystemBRInheritedProperties,
        WearableSizeSystemBRAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemBRAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableSizeSystemBRAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeSystemBRAllProperties):
    pydantic_type = create_wearablesizesystembr_model(model=model)
    return pydantic_type(model).schema_json()
