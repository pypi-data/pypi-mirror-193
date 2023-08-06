"""
Size group "Boys" for wearables.

https://schema.org/WearableSizeGroupBoys
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupBoysInheritedProperties(TypedDict):
    """Size group "Boys" for wearables.

    References:
        https://schema.org/WearableSizeGroupBoys
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupBoysProperties(TypedDict):
    """Size group "Boys" for wearables.

    References:
        https://schema.org/WearableSizeGroupBoys
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupBoysAllProperties(
    WearableSizeGroupBoysInheritedProperties, WearableSizeGroupBoysProperties, TypedDict
):
    pass


class WearableSizeGroupBoysBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupBoys", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupBoysProperties,
        WearableSizeGroupBoysInheritedProperties,
        WearableSizeGroupBoysAllProperties,
    ] = WearableSizeGroupBoysAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupBoys"
    return model


WearableSizeGroupBoys = create_schema_org_model()


def create_wearablesizegroupboys_model(
    model: Union[
        WearableSizeGroupBoysProperties,
        WearableSizeGroupBoysInheritedProperties,
        WearableSizeGroupBoysAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupBoysAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeGroupBoysAllProperties):
    pydantic_type = create_wearablesizegroupboys_model(model=model)
    return pydantic_type(model).schema_json()
