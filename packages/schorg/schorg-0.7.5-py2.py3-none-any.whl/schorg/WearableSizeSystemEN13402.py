"""
EN 13402 (joint European standard for size labelling of clothes).

https://schema.org/WearableSizeSystemEN13402
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemEN13402InheritedProperties(TypedDict):
    """EN 13402 (joint European standard for size labelling of clothes).

    References:
        https://schema.org/WearableSizeSystemEN13402
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemEN13402Properties(TypedDict):
    """EN 13402 (joint European standard for size labelling of clothes).

    References:
        https://schema.org/WearableSizeSystemEN13402
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemEN13402AllProperties(
    WearableSizeSystemEN13402InheritedProperties,
    WearableSizeSystemEN13402Properties,
    TypedDict,
):
    pass


class WearableSizeSystemEN13402BaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemEN13402", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemEN13402Properties,
        WearableSizeSystemEN13402InheritedProperties,
        WearableSizeSystemEN13402AllProperties,
    ] = WearableSizeSystemEN13402AllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemEN13402"
    return model


WearableSizeSystemEN13402 = create_schema_org_model()


def create_wearablesizesystemen13402_model(
    model: Union[
        WearableSizeSystemEN13402Properties,
        WearableSizeSystemEN13402InheritedProperties,
        WearableSizeSystemEN13402AllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemEN13402AllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeSystemEN13402. Please see: https://schema.org/WearableSizeSystemEN13402"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeSystemEN13402AllProperties):
    pydantic_type = create_wearablesizesystemen13402_model(model=model)
    return pydantic_type(model).schema_json()
