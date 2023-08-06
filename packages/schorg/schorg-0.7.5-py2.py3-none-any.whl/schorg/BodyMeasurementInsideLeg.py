"""
Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.

https://schema.org/BodyMeasurementInsideLeg
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementInsideLegInheritedProperties(TypedDict):
    """Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.

    References:
        https://schema.org/BodyMeasurementInsideLeg
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementInsideLegProperties(TypedDict):
    """Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.

    References:
        https://schema.org/BodyMeasurementInsideLeg
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementInsideLegAllProperties(
    BodyMeasurementInsideLegInheritedProperties,
    BodyMeasurementInsideLegProperties,
    TypedDict,
):
    pass


class BodyMeasurementInsideLegBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementInsideLeg", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementInsideLegProperties,
        BodyMeasurementInsideLegInheritedProperties,
        BodyMeasurementInsideLegAllProperties,
    ] = BodyMeasurementInsideLegAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementInsideLeg"
    return model


BodyMeasurementInsideLeg = create_schema_org_model()


def create_bodymeasurementinsideleg_model(
    model: Union[
        BodyMeasurementInsideLegProperties,
        BodyMeasurementInsideLegInheritedProperties,
        BodyMeasurementInsideLegAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementInsideLegAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BodyMeasurementInsideLeg. Please see: https://schema.org/BodyMeasurementInsideLeg"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BodyMeasurementInsideLegAllProperties):
    pydantic_type = create_bodymeasurementinsideleg_model(model=model)
    return pydantic_type(model).schema_json()
