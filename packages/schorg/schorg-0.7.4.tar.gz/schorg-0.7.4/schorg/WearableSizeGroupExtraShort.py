"""
Size group "Extra Short" for wearables.

https://schema.org/WearableSizeGroupExtraShort
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupExtraShortInheritedProperties(TypedDict):
    """Size group "Extra Short" for wearables.

    References:
        https://schema.org/WearableSizeGroupExtraShort
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupExtraShortProperties(TypedDict):
    """Size group "Extra Short" for wearables.

    References:
        https://schema.org/WearableSizeGroupExtraShort
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupExtraShortAllProperties(
    WearableSizeGroupExtraShortInheritedProperties,
    WearableSizeGroupExtraShortProperties,
    TypedDict,
):
    pass


class WearableSizeGroupExtraShortBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupExtraShort", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupExtraShortProperties,
        WearableSizeGroupExtraShortInheritedProperties,
        WearableSizeGroupExtraShortAllProperties,
    ] = WearableSizeGroupExtraShortAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupExtraShort"
    return model


WearableSizeGroupExtraShort = create_schema_org_model()


def create_wearablesizegroupextrashort_model(
    model: Union[
        WearableSizeGroupExtraShortProperties,
        WearableSizeGroupExtraShortInheritedProperties,
        WearableSizeGroupExtraShortAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupExtraShortAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableSizeGroupExtraShortAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeGroupExtraShortAllProperties):
    pydantic_type = create_wearablesizegroupextrashort_model(model=model)
    return pydantic_type(model).schema_json()
