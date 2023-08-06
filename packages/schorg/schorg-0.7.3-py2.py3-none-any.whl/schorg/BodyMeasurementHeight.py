"""
Body height (measured between crown of head and soles of feet). Used, for example, to fit jackets.

https://schema.org/BodyMeasurementHeight
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementHeightInheritedProperties(TypedDict):
    """Body height (measured between crown of head and soles of feet). Used, for example, to fit jackets.

    References:
        https://schema.org/BodyMeasurementHeight
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementHeightProperties(TypedDict):
    """Body height (measured between crown of head and soles of feet). Used, for example, to fit jackets.

    References:
        https://schema.org/BodyMeasurementHeight
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementHeightAllProperties(
    BodyMeasurementHeightInheritedProperties, BodyMeasurementHeightProperties, TypedDict
):
    pass


class BodyMeasurementHeightBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementHeight", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementHeightProperties,
        BodyMeasurementHeightInheritedProperties,
        BodyMeasurementHeightAllProperties,
    ] = BodyMeasurementHeightAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementHeight"
    return model


BodyMeasurementHeight = create_schema_org_model()


def create_bodymeasurementheight_model(
    model: Union[
        BodyMeasurementHeightProperties,
        BodyMeasurementHeightInheritedProperties,
        BodyMeasurementHeightAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementHeightAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: BodyMeasurementHeightAllProperties):
    pydantic_type = create_bodymeasurementheight_model(model=model)
    return pydantic_type(model).schema_json()
