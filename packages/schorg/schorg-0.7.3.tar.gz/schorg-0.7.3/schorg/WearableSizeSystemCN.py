"""
Chinese size system for wearables.

https://schema.org/WearableSizeSystemCN
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemCNInheritedProperties(TypedDict):
    """Chinese size system for wearables.

    References:
        https://schema.org/WearableSizeSystemCN
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemCNProperties(TypedDict):
    """Chinese size system for wearables.

    References:
        https://schema.org/WearableSizeSystemCN
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemCNAllProperties(
    WearableSizeSystemCNInheritedProperties, WearableSizeSystemCNProperties, TypedDict
):
    pass


class WearableSizeSystemCNBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemCN", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemCNProperties,
        WearableSizeSystemCNInheritedProperties,
        WearableSizeSystemCNAllProperties,
    ] = WearableSizeSystemCNAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemCN"
    return model


WearableSizeSystemCN = create_schema_org_model()


def create_wearablesizesystemcn_model(
    model: Union[
        WearableSizeSystemCNProperties,
        WearableSizeSystemCNInheritedProperties,
        WearableSizeSystemCNAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemCNAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeSystemCNAllProperties):
    pydantic_type = create_wearablesizesystemcn_model(model=model)
    return pydantic_type(model).schema_json()
