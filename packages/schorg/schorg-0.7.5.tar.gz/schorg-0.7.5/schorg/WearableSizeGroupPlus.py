"""
Size group "Plus" for wearables.

https://schema.org/WearableSizeGroupPlus
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupPlusInheritedProperties(TypedDict):
    """Size group "Plus" for wearables.

    References:
        https://schema.org/WearableSizeGroupPlus
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupPlusProperties(TypedDict):
    """Size group "Plus" for wearables.

    References:
        https://schema.org/WearableSizeGroupPlus
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupPlusAllProperties(
    WearableSizeGroupPlusInheritedProperties, WearableSizeGroupPlusProperties, TypedDict
):
    pass


class WearableSizeGroupPlusBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupPlus", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupPlusProperties,
        WearableSizeGroupPlusInheritedProperties,
        WearableSizeGroupPlusAllProperties,
    ] = WearableSizeGroupPlusAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupPlus"
    return model


WearableSizeGroupPlus = create_schema_org_model()


def create_wearablesizegroupplus_model(
    model: Union[
        WearableSizeGroupPlusProperties,
        WearableSizeGroupPlusInheritedProperties,
        WearableSizeGroupPlusAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupPlusAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeGroupPlus. Please see: https://schema.org/WearableSizeGroupPlus"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeGroupPlusAllProperties):
    pydantic_type = create_wearablesizegroupplus_model(model=model)
    return pydantic_type(model).schema_json()
