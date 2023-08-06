"""
Mexican size system for wearables.

https://schema.org/WearableSizeSystemMX
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemMXInheritedProperties(TypedDict):
    """Mexican size system for wearables.

    References:
        https://schema.org/WearableSizeSystemMX
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemMXProperties(TypedDict):
    """Mexican size system for wearables.

    References:
        https://schema.org/WearableSizeSystemMX
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemMXAllProperties(
    WearableSizeSystemMXInheritedProperties, WearableSizeSystemMXProperties, TypedDict
):
    pass


class WearableSizeSystemMXBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemMX", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemMXProperties,
        WearableSizeSystemMXInheritedProperties,
        WearableSizeSystemMXAllProperties,
    ] = WearableSizeSystemMXAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemMX"
    return model


WearableSizeSystemMX = create_schema_org_model()


def create_wearablesizesystemmx_model(
    model: Union[
        WearableSizeSystemMXProperties,
        WearableSizeSystemMXInheritedProperties,
        WearableSizeSystemMXAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemMXAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeSystemMX. Please see: https://schema.org/WearableSizeSystemMX"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeSystemMXAllProperties):
    pydantic_type = create_wearablesizesystemmx_model(model=model)
    return pydantic_type(model).schema_json()
