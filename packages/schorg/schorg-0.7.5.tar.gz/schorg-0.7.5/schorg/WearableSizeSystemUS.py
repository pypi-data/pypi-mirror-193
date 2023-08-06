"""
United States size system for wearables.

https://schema.org/WearableSizeSystemUS
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemUSInheritedProperties(TypedDict):
    """United States size system for wearables.

    References:
        https://schema.org/WearableSizeSystemUS
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemUSProperties(TypedDict):
    """United States size system for wearables.

    References:
        https://schema.org/WearableSizeSystemUS
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemUSAllProperties(
    WearableSizeSystemUSInheritedProperties, WearableSizeSystemUSProperties, TypedDict
):
    pass


class WearableSizeSystemUSBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemUS", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemUSProperties,
        WearableSizeSystemUSInheritedProperties,
        WearableSizeSystemUSAllProperties,
    ] = WearableSizeSystemUSAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemUS"
    return model


WearableSizeSystemUS = create_schema_org_model()


def create_wearablesizesystemus_model(
    model: Union[
        WearableSizeSystemUSProperties,
        WearableSizeSystemUSInheritedProperties,
        WearableSizeSystemUSAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemUSAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeSystemUS. Please see: https://schema.org/WearableSizeSystemUS"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeSystemUSAllProperties):
    pydantic_type = create_wearablesizesystemus_model(model=model)
    return pydantic_type(model).schema_json()
