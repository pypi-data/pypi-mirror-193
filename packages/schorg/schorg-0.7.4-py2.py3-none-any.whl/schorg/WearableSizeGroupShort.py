"""
Size group "Short" for wearables.

https://schema.org/WearableSizeGroupShort
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupShortInheritedProperties(TypedDict):
    """Size group "Short" for wearables.

    References:
        https://schema.org/WearableSizeGroupShort
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupShortProperties(TypedDict):
    """Size group "Short" for wearables.

    References:
        https://schema.org/WearableSizeGroupShort
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupShortAllProperties(
    WearableSizeGroupShortInheritedProperties,
    WearableSizeGroupShortProperties,
    TypedDict,
):
    pass


class WearableSizeGroupShortBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupShort", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupShortProperties,
        WearableSizeGroupShortInheritedProperties,
        WearableSizeGroupShortAllProperties,
    ] = WearableSizeGroupShortAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupShort"
    return model


WearableSizeGroupShort = create_schema_org_model()


def create_wearablesizegroupshort_model(
    model: Union[
        WearableSizeGroupShortProperties,
        WearableSizeGroupShortInheritedProperties,
        WearableSizeGroupShortAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupShortAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableSizeGroupShortAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeGroupShortAllProperties):
    pydantic_type = create_wearablesizegroupshort_model(model=model)
    return pydantic_type(model).schema_json()
