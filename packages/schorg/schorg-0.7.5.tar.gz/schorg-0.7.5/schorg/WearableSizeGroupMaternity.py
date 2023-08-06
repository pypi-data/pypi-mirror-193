"""
Size group "Maternity" for wearables.

https://schema.org/WearableSizeGroupMaternity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupMaternityInheritedProperties(TypedDict):
    """Size group "Maternity" for wearables.

    References:
        https://schema.org/WearableSizeGroupMaternity
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupMaternityProperties(TypedDict):
    """Size group "Maternity" for wearables.

    References:
        https://schema.org/WearableSizeGroupMaternity
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupMaternityAllProperties(
    WearableSizeGroupMaternityInheritedProperties,
    WearableSizeGroupMaternityProperties,
    TypedDict,
):
    pass


class WearableSizeGroupMaternityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupMaternity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupMaternityProperties,
        WearableSizeGroupMaternityInheritedProperties,
        WearableSizeGroupMaternityAllProperties,
    ] = WearableSizeGroupMaternityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupMaternity"
    return model


WearableSizeGroupMaternity = create_schema_org_model()


def create_wearablesizegroupmaternity_model(
    model: Union[
        WearableSizeGroupMaternityProperties,
        WearableSizeGroupMaternityInheritedProperties,
        WearableSizeGroupMaternityAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupMaternityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeGroupMaternity. Please see: https://schema.org/WearableSizeGroupMaternity"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeGroupMaternityAllProperties):
    pydantic_type = create_wearablesizegroupmaternity_model(model=model)
    return pydantic_type(model).schema_json()
