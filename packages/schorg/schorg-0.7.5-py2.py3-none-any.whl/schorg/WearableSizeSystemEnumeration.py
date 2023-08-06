"""
Enumerates common size systems specific for wearable products

https://schema.org/WearableSizeSystemEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemEnumerationInheritedProperties(TypedDict):
    """Enumerates common size systems specific for wearable products

    References:
        https://schema.org/WearableSizeSystemEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class WearableSizeSystemEnumerationProperties(TypedDict):
    """Enumerates common size systems specific for wearable products

    References:
        https://schema.org/WearableSizeSystemEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class WearableSizeSystemEnumerationAllProperties(
    WearableSizeSystemEnumerationInheritedProperties,
    WearableSizeSystemEnumerationProperties,
    TypedDict,
):
    pass


class WearableSizeSystemEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemEnumerationProperties,
        WearableSizeSystemEnumerationInheritedProperties,
        WearableSizeSystemEnumerationAllProperties,
    ] = WearableSizeSystemEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemEnumeration"
    return model


WearableSizeSystemEnumeration = create_schema_org_model()


def create_wearablesizesystemenumeration_model(
    model: Union[
        WearableSizeSystemEnumerationProperties,
        WearableSizeSystemEnumerationInheritedProperties,
        WearableSizeSystemEnumerationAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeSystemEnumeration. Please see: https://schema.org/WearableSizeSystemEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeSystemEnumerationAllProperties):
    pydantic_type = create_wearablesizesystemenumeration_model(model=model)
    return pydantic_type(model).schema_json()
