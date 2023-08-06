"""
Measurement of the hip section, for example of a skirt

https://schema.org/WearableMeasurementHips
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementHipsInheritedProperties(TypedDict):
    """Measurement of the hip section, for example of a skirt

    References:
        https://schema.org/WearableMeasurementHips
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementHipsProperties(TypedDict):
    """Measurement of the hip section, for example of a skirt

    References:
        https://schema.org/WearableMeasurementHips
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementHipsAllProperties(
    WearableMeasurementHipsInheritedProperties,
    WearableMeasurementHipsProperties,
    TypedDict,
):
    pass


class WearableMeasurementHipsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableMeasurementHips", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementHipsProperties,
        WearableMeasurementHipsInheritedProperties,
        WearableMeasurementHipsAllProperties,
    ] = WearableMeasurementHipsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementHips"
    return model


WearableMeasurementHips = create_schema_org_model()


def create_wearablemeasurementhips_model(
    model: Union[
        WearableMeasurementHipsProperties,
        WearableMeasurementHipsInheritedProperties,
        WearableMeasurementHipsAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementHipsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableMeasurementHipsAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableMeasurementHipsAllProperties):
    pydantic_type = create_wearablemeasurementhips_model(model=model)
    return pydantic_type(model).schema_json()
