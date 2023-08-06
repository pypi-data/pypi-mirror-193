"""
Size group "Husky" (or "Stocky") for wearables.

https://schema.org/WearableSizeGroupHusky
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupHuskyInheritedProperties(TypedDict):
    """Size group "Husky" (or "Stocky") for wearables.

    References:
        https://schema.org/WearableSizeGroupHusky
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupHuskyProperties(TypedDict):
    """Size group "Husky" (or "Stocky") for wearables.

    References:
        https://schema.org/WearableSizeGroupHusky
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupHuskyAllProperties(
    WearableSizeGroupHuskyInheritedProperties,
    WearableSizeGroupHuskyProperties,
    TypedDict,
):
    pass


class WearableSizeGroupHuskyBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupHusky", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupHuskyProperties,
        WearableSizeGroupHuskyInheritedProperties,
        WearableSizeGroupHuskyAllProperties,
    ] = WearableSizeGroupHuskyAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupHusky"
    return model


WearableSizeGroupHusky = create_schema_org_model()


def create_wearablesizegrouphusky_model(
    model: Union[
        WearableSizeGroupHuskyProperties,
        WearableSizeGroupHuskyInheritedProperties,
        WearableSizeGroupHuskyAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupHuskyAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeGroupHuskyAllProperties):
    pydantic_type = create_wearablesizegrouphusky_model(model=model)
    return pydantic_type(model).schema_json()
