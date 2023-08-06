"""
Continental size system for wearables.

https://schema.org/WearableSizeSystemContinental
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemContinentalInheritedProperties(TypedDict):
    """Continental size system for wearables.

    References:
        https://schema.org/WearableSizeSystemContinental
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemContinentalProperties(TypedDict):
    """Continental size system for wearables.

    References:
        https://schema.org/WearableSizeSystemContinental
    Note:
        Model Depth 6
    Attributes:
    """


class WearableSizeSystemContinentalAllProperties(
    WearableSizeSystemContinentalInheritedProperties,
    WearableSizeSystemContinentalProperties,
    TypedDict,
):
    pass


class WearableSizeSystemContinentalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableSizeSystemContinental", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableSizeSystemContinentalProperties,
        WearableSizeSystemContinentalInheritedProperties,
        WearableSizeSystemContinentalAllProperties,
    ] = WearableSizeSystemContinentalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemContinental"
    return model


WearableSizeSystemContinental = create_schema_org_model()


def create_wearablesizesystemcontinental_model(
    model: Union[
        WearableSizeSystemContinentalProperties,
        WearableSizeSystemContinentalInheritedProperties,
        WearableSizeSystemContinentalAllProperties,
    ]
):
    _type = deepcopy(WearableSizeSystemContinentalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableSizeSystemContinentalAllProperties):
    pydantic_type = create_wearablesizesystemcontinental_model(model=model)
    return pydantic_type(model).schema_json()
