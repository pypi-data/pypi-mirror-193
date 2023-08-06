"""
Size group "Juniors" for wearables.

https://schema.org/WearableSizeGroupJuniors
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupJuniorsInheritedProperties(TypedDict):
    """Size group "Juniors" for wearables.

    References:
        https://schema.org/WearableSizeGroupJuniors
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupJuniorsProperties(TypedDict):
    """Size group "Juniors" for wearables.

    References:
        https://schema.org/WearableSizeGroupJuniors
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupJuniorsAllProperties(
    WearableSizeGroupJuniorsInheritedProperties,
    WearableSizeGroupJuniorsProperties,
    TypedDict,
):
    pass


class WearableSizeGroupJuniorsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupJuniors", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupJuniorsProperties,
        WearableSizeGroupJuniorsInheritedProperties,
        WearableSizeGroupJuniorsAllProperties,
    ] = WearableSizeGroupJuniorsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupJuniors"
    return model


WearableSizeGroupJuniors = create_schema_org_model()


def create_wearablesizegroupjuniors_model(
    model: Union[
        WearableSizeGroupJuniorsProperties,
        WearableSizeGroupJuniorsInheritedProperties,
        WearableSizeGroupJuniorsAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupJuniorsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableSizeGroupJuniorsAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeGroupJuniorsAllProperties):
    pydantic_type = create_wearablesizegroupjuniors_model(model=model)
    return pydantic_type(model).schema_json()
