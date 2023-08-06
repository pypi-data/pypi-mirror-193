"""
United Kingdom size system for wearables.

https://schema.org/WearableSizeSystemUK
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemUKInheritedProperties(TypedDict):
    """United Kingdom size system for wearables.

    References:
        https://schema.org/WearableSizeSystemUK
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemUKProperties(TypedDict):
    """United Kingdom size system for wearables.

    References:
        https://schema.org/WearableSizeSystemUK
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemUKAllProperties(
    WearableSizeSystemUKInheritedProperties, WearableSizeSystemUKProperties, TypedDict
):
    pass


class WearableSizeSystemUKBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemUK", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemUKProperties,
        WearableSizeSystemUKInheritedProperties,
        WearableSizeSystemUKAllProperties,
    ] = WearableSizeSystemUKAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemUK"
    return model


WearableSizeSystemUK = create_schema_org_model()


def create_wearablesizesystemuk_model(
    model: Union[
        WearableSizeSystemUKProperties,
        WearableSizeSystemUKInheritedProperties,
        WearableSizeSystemUKAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemUKAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeSystemUK. Please see: https://schema.org/WearableSizeSystemUK"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeSystemUKAllProperties):
    pydantic_type = create_wearablesizesystemuk_model(model=model)
    return pydantic_type(model).schema_json()
