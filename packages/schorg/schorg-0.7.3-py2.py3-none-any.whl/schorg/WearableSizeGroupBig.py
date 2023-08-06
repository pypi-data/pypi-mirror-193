"""
Size group "Big" for wearables.

https://schema.org/WearableSizeGroupBig
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupBigInheritedProperties(TypedDict):
    """Size group "Big" for wearables.

    References:
        https://schema.org/WearableSizeGroupBig
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupBigProperties(TypedDict):
    """Size group "Big" for wearables.

    References:
        https://schema.org/WearableSizeGroupBig
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeGroupBigAllProperties(
    WearableSizeGroupBigInheritedProperties, WearableSizeGroupBigProperties, TypedDict
):
    pass


class WearableSizeGroupBigBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeGroupBig", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeGroupBigProperties,
        WearableSizeGroupBigInheritedProperties,
        WearableSizeGroupBigAllProperties,
    ] = WearableSizeGroupBigAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupBig"
    return model


WearableSizeGroupBig = create_schema_org_model()


def create_wearablesizegroupbig_model(
    model: Union[
        WearableSizeGroupBigProperties,
        WearableSizeGroupBigInheritedProperties,
        WearableSizeGroupBigAllProperties,
    ]
):
    _type = deepcopy(WearableSizeGroupBigAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeGroupBigAllProperties):
    pydantic_type = create_wearablesizegroupbig_model(model=model)
    return pydantic_type(model).schema_json()
