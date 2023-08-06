"""
Measurement of the waist section, for example of pants

https://schema.org/WearableMeasurementWaist
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementWaistInheritedProperties(TypedDict):
    """Measurement of the waist section, for example of pants

    References:
        https://schema.org/WearableMeasurementWaist
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementWaistProperties(TypedDict):
    """Measurement of the waist section, for example of pants

    References:
        https://schema.org/WearableMeasurementWaist
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementWaistAllProperties(
    WearableMeasurementWaistInheritedProperties,
    WearableMeasurementWaistProperties,
    TypedDict,
):
    pass


class WearableMeasurementWaistBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableMeasurementWaist", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementWaistProperties,
        WearableMeasurementWaistInheritedProperties,
        WearableMeasurementWaistAllProperties,
    ] = WearableMeasurementWaistAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementWaist"
    return model


WearableMeasurementWaist = create_schema_org_model()


def create_wearablemeasurementwaist_model(
    model: Union[
        WearableMeasurementWaistProperties,
        WearableMeasurementWaistInheritedProperties,
        WearableMeasurementWaistAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementWaistAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of WearableMeasurementWaistAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableMeasurementWaistAllProperties):
    pydantic_type = create_wearablemeasurementwaist_model(model=model)
    return pydantic_type(model).schema_json()
