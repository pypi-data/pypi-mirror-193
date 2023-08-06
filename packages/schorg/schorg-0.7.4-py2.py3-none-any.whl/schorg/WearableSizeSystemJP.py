"""
Japanese size system for wearables.

https://schema.org/WearableSizeSystemJP
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemJPInheritedProperties(TypedDict):
    """Japanese size system for wearables.

    References:
        https://schema.org/WearableSizeSystemJP
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemJPProperties(TypedDict):
    """Japanese size system for wearables.

    References:
        https://schema.org/WearableSizeSystemJP
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemJPAllProperties(
    WearableSizeSystemJPInheritedProperties, WearableSizeSystemJPProperties, TypedDict
):
    pass


class WearableSizeSystemJPBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemJP", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemJPProperties,
        WearableSizeSystemJPInheritedProperties,
        WearableSizeSystemJPAllProperties,
    ] = WearableSizeSystemJPAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemJP"
    return model


WearableSizeSystemJP = create_schema_org_model()


def create_wearablesizesystemjp_model(
    model: Union[
        WearableSizeSystemJPProperties,
        WearableSizeSystemJPInheritedProperties,
        WearableSizeSystemJPAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemJPAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableSizeSystemJPAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeSystemJPAllProperties):
    pydantic_type = create_wearablesizesystemjp_model(model=model)
    return pydantic_type(model).schema_json()
