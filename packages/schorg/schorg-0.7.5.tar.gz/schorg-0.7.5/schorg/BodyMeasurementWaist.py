"""
Girth of natural waistline (between hip bones and lower ribs). Used, for example, to fit pants.

https://schema.org/BodyMeasurementWaist
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementWaistInheritedProperties(TypedDict):
    """Girth of natural waistline (between hip bones and lower ribs). Used, for example, to fit pants.

    References:
        https://schema.org/BodyMeasurementWaist
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementWaistProperties(TypedDict):
    """Girth of natural waistline (between hip bones and lower ribs). Used, for example, to fit pants.

    References:
        https://schema.org/BodyMeasurementWaist
    Note:
        Model Depth 6
    Attributes:
    """


class BodyMeasurementWaistAllProperties(
    BodyMeasurementWaistInheritedProperties, BodyMeasurementWaistProperties, TypedDict
):
    pass


class BodyMeasurementWaistBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementWaist", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementWaistProperties,
        BodyMeasurementWaistInheritedProperties,
        BodyMeasurementWaistAllProperties,
    ] = BodyMeasurementWaistAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementWaist"
    return model


BodyMeasurementWaist = create_schema_org_model()


def create_bodymeasurementwaist_model(
    model: Union[
        BodyMeasurementWaistProperties,
        BodyMeasurementWaistInheritedProperties,
        BodyMeasurementWaistAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementWaistAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BodyMeasurementWaist. Please see: https://schema.org/BodyMeasurementWaist"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BodyMeasurementWaistAllProperties):
    pydantic_type = create_bodymeasurementwaist_model(model=model)
    return pydantic_type(model).schema_json()
