"""
Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

https://schema.org/BodyMeasurementHips
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementHipsInheritedProperties(TypedDict):
    """Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

    References:
        https://schema.org/BodyMeasurementHips
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementHipsProperties(TypedDict):
    """Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

    References:
        https://schema.org/BodyMeasurementHips
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementHipsAllProperties(
    BodyMeasurementHipsInheritedProperties, BodyMeasurementHipsProperties, TypedDict
):
    pass


class BodyMeasurementHipsBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementHips", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementHipsProperties,
        BodyMeasurementHipsInheritedProperties,
        BodyMeasurementHipsAllProperties,
    ] = BodyMeasurementHipsAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementHips"
    return model


BodyMeasurementHips = create_schema_org_model()


def create_bodymeasurementhips_model(
    model: Union[
        BodyMeasurementHipsProperties,
        BodyMeasurementHipsInheritedProperties,
        BodyMeasurementHipsAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementHipsAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BodyMeasurementHips. Please see: https://schema.org/BodyMeasurementHips"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BodyMeasurementHipsAllProperties):
    pydantic_type = create_bodymeasurementhips_model(model=model)
    return pydantic_type(model).schema_json()
