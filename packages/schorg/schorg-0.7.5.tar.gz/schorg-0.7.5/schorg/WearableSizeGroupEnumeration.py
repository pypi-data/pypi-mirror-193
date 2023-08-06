"""
Enumerates common size groups (also known as "size types") for wearable products.

https://schema.org/WearableSizeGroupEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupEnumerationInheritedProperties(TypedDict):
    """Enumerates common size groups (also known as "size types") for wearable products.

    References:
        https://schema.org/WearableSizeGroupEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class WearableSizeGroupEnumerationProperties(TypedDict):
    """Enumerates common size groups (also known as "size types") for wearable products.

    References:
        https://schema.org/WearableSizeGroupEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class WearableSizeGroupEnumerationAllProperties(
    WearableSizeGroupEnumerationInheritedProperties,
    WearableSizeGroupEnumerationProperties,
    TypedDict,
):
    pass


class WearableSizeGroupEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupEnumerationProperties,
        WearableSizeGroupEnumerationInheritedProperties,
        WearableSizeGroupEnumerationAllProperties,
    ] = WearableSizeGroupEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupEnumeration"
    return model


WearableSizeGroupEnumeration = create_schema_org_model()


def create_wearablesizegroupenumeration_model(
    model: Union[
        WearableSizeGroupEnumerationProperties,
        WearableSizeGroupEnumerationInheritedProperties,
        WearableSizeGroupEnumerationAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableSizeGroupEnumeration. Please see: https://schema.org/WearableSizeGroupEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: WearableSizeGroupEnumerationAllProperties):
    pydantic_type = create_wearablesizegroupenumeration_model(model=model)
    return pydantic_type(model).schema_json()
