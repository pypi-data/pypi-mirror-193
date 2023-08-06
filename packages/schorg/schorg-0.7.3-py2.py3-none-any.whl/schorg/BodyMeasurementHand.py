"""
Maximum hand girth (measured over the knuckles of the open right hand excluding thumb, fingers together). Used, for example, to fit gloves.

https://schema.org/BodyMeasurementHand
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementHandInheritedProperties(TypedDict):
    """Maximum hand girth (measured over the knuckles of the open right hand excluding thumb, fingers together). Used, for example, to fit gloves.

    References:
        https://schema.org/BodyMeasurementHand
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementHandProperties(TypedDict):
    """Maximum hand girth (measured over the knuckles of the open right hand excluding thumb, fingers together). Used, for example, to fit gloves.

    References:
        https://schema.org/BodyMeasurementHand
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementHandAllProperties(
    BodyMeasurementHandInheritedProperties, BodyMeasurementHandProperties, TypedDict
):
    pass


class BodyMeasurementHandBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementHand", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementHandProperties,
        BodyMeasurementHandInheritedProperties,
        BodyMeasurementHandAllProperties,
    ] = BodyMeasurementHandAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementHand"
    return model


BodyMeasurementHand = create_schema_org_model()


def create_bodymeasurementhand_model(
    model: Union[
        BodyMeasurementHandProperties,
        BodyMeasurementHandInheritedProperties,
        BodyMeasurementHandAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementHandAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BodyMeasurementHandAllProperties):
    pydantic_type = create_bodymeasurementhand_model(model=model)
    return pydantic_type(model).schema_json()
