"""
Measurement of the outside leg, for example of pants

https://schema.org/WearableMeasurementOutsideLeg
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementOutsideLegInheritedProperties(TypedDict):
    """Measurement of the outside leg, for example of pants

    References:
        https://schema.org/WearableMeasurementOutsideLeg
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementOutsideLegProperties(TypedDict):
    """Measurement of the outside leg, for example of pants

    References:
        https://schema.org/WearableMeasurementOutsideLeg
    Note:
        Model Depth 6
    Attributes:
    """


class WearableMeasurementOutsideLegAllProperties(
    WearableMeasurementOutsideLegInheritedProperties,
    WearableMeasurementOutsideLegProperties,
    TypedDict,
):
    pass


class WearableMeasurementOutsideLegBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="WearableMeasurementOutsideLeg", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        WearableMeasurementOutsideLegProperties,
        WearableMeasurementOutsideLegInheritedProperties,
        WearableMeasurementOutsideLegAllProperties,
    ] = WearableMeasurementOutsideLegAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementOutsideLeg"
    return model


WearableMeasurementOutsideLeg = create_schema_org_model()


def create_wearablemeasurementoutsideleg_model(
    model: Union[
        WearableMeasurementOutsideLegProperties,
        WearableMeasurementOutsideLegInheritedProperties,
        WearableMeasurementOutsideLegAllProperties,
    ]
):
    _type = deepcopy(WearableMeasurementOutsideLegAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of WearableMeasurementOutsideLegAllProperties"
            )
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: WearableMeasurementOutsideLegAllProperties):
    pydantic_type = create_wearablemeasurementoutsideleg_model(model=model)
    return pydantic_type(model).schema_json()
