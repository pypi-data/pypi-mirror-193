"""
Body weight. Used, for example, to measure pantyhose.

https://schema.org/BodyMeasurementWeight
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementWeightInheritedProperties(TypedDict):
    """Body weight. Used, for example, to measure pantyhose.

    References:
        https://schema.org/BodyMeasurementWeight
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementWeightProperties(TypedDict):
    """Body weight. Used, for example, to measure pantyhose.

    References:
        https://schema.org/BodyMeasurementWeight
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementWeightAllProperties(
    BodyMeasurementWeightInheritedProperties, BodyMeasurementWeightProperties, TypedDict
):
    pass


class BodyMeasurementWeightBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementWeight", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementWeightProperties,
        BodyMeasurementWeightInheritedProperties,
        BodyMeasurementWeightAllProperties,
    ] = BodyMeasurementWeightAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementWeight"
    return model


BodyMeasurementWeight = create_schema_org_model()


def create_bodymeasurementweight_model(
    model: Union[
        BodyMeasurementWeightProperties,
        BodyMeasurementWeightInheritedProperties,
        BodyMeasurementWeightAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementWeightAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BodyMeasurementWeight. Please see: https://schema.org/BodyMeasurementWeight"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BodyMeasurementWeightAllProperties):
    pydantic_type = create_bodymeasurementweight_model(model=model)
    return pydantic_type(model).schema_json()
