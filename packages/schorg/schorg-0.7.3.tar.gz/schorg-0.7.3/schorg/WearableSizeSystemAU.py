"""
Australian size system for wearables.

https://schema.org/WearableSizeSystemAU
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemAUInheritedProperties(TypedDict):
    """Australian size system for wearables.

    References:
        https://schema.org/WearableSizeSystemAU
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemAUProperties(TypedDict):
    """Australian size system for wearables.

    References:
        https://schema.org/WearableSizeSystemAU
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemAUAllProperties(
    WearableSizeSystemAUInheritedProperties, WearableSizeSystemAUProperties, TypedDict
):
    pass


class WearableSizeSystemAUBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemAU", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemAUProperties,
        WearableSizeSystemAUInheritedProperties,
        WearableSizeSystemAUAllProperties,
    ] = WearableSizeSystemAUAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemAU"
    return model


WearableSizeSystemAU = create_schema_org_model()


def create_wearablesizesystemau_model(
    model: Union[
        WearableSizeSystemAUProperties,
        WearableSizeSystemAUInheritedProperties,
        WearableSizeSystemAUAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemAUAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeSystemAUAllProperties):
    pydantic_type = create_wearablesizesystemau_model(model=model)
    return pydantic_type(model).schema_json()
