"""
Measurement of the height, for example the heel height of a shoe

https://schema.org/WearableMeasurementHeight
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementHeightInheritedProperties(TypedDict):
    """Measurement of the height, for example the heel height of a shoe

    References:
        https://schema.org/WearableMeasurementHeight
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementHeightProperties(TypedDict):
    """Measurement of the height, for example the heel height of a shoe

    References:
        https://schema.org/WearableMeasurementHeight
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementHeightAllProperties(
    WearableMeasurementHeightInheritedProperties,
    WearableMeasurementHeightProperties,
    TypedDict,
):
    pass


class WearableMeasurementHeightBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableMeasurementHeight", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementHeightProperties,
        WearableMeasurementHeightInheritedProperties,
        WearableMeasurementHeightAllProperties,
    ] = WearableMeasurementHeightAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementHeight"
    return model


WearableMeasurementHeight = create_schema_org_model()


def create_wearablemeasurementheight_model(
    model: Union[
        WearableMeasurementHeightProperties,
        WearableMeasurementHeightInheritedProperties,
        WearableMeasurementHeightAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementHeightAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableMeasurementHeightAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableMeasurementHeightAllProperties):
    pydantic_type = create_wearablemeasurementheight_model(model=model)
    return pydantic_type(model).schema_json()
