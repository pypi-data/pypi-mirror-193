"""
Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts.

https://schema.org/BodyMeasurementArm
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementArmInheritedProperties(TypedDict):
    """Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts.

    References:
        https://schema.org/BodyMeasurementArm
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementArmProperties(TypedDict):
    """Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts.

    References:
        https://schema.org/BodyMeasurementArm
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementArmAllProperties(
    BodyMeasurementArmInheritedProperties, BodyMeasurementArmProperties, TypedDict
):
    pass


class BodyMeasurementArmBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementArm", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementArmProperties,
        BodyMeasurementArmInheritedProperties,
        BodyMeasurementArmAllProperties,
    ] = BodyMeasurementArmAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementArm"
    return model


BodyMeasurementArm = create_schema_org_model()


def create_bodymeasurementarm_model(
    model: Union[
        BodyMeasurementArmProperties,
        BodyMeasurementArmInheritedProperties,
        BodyMeasurementArmAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementArmAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BodyMeasurementArm. Please see: https://schema.org/BodyMeasurementArm"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BodyMeasurementArmAllProperties):
    pydantic_type = create_bodymeasurementarm_model(model=model)
    return pydantic_type(model).schema_json()
