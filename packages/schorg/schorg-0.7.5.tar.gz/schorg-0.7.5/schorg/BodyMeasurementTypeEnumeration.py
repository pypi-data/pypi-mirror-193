"""
Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.

https://schema.org/BodyMeasurementTypeEnumeration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementTypeEnumerationInheritedProperties(TypedDict):
    """Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.

    References:
        https://schema.org/BodyMeasurementTypeEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class BodyMeasurementTypeEnumerationProperties(TypedDict):
    """Enumerates types (or dimensions) of a person's body measurements, for example for fitting of clothes.

    References:
        https://schema.org/BodyMeasurementTypeEnumeration
    Note:
        Model Depth 5
    Attributes:
    """


class BodyMeasurementTypeEnumerationAllProperties(
    BodyMeasurementTypeEnumerationInheritedProperties,
    BodyMeasurementTypeEnumerationProperties,
    TypedDict,
):
    pass


class BodyMeasurementTypeEnumerationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyMeasurementTypeEnumeration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyMeasurementTypeEnumerationProperties,
        BodyMeasurementTypeEnumerationInheritedProperties,
        BodyMeasurementTypeEnumerationAllProperties,
    ] = BodyMeasurementTypeEnumerationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementTypeEnumeration"
    return model


BodyMeasurementTypeEnumeration = create_schema_org_model()


def create_bodymeasurementtypeenumeration_model(
    model: Union[
        BodyMeasurementTypeEnumerationProperties,
        BodyMeasurementTypeEnumerationInheritedProperties,
        BodyMeasurementTypeEnumerationAllProperties,
    ]
):
    _type = deepcopy(BodyMeasurementTypeEnumerationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BodyMeasurementTypeEnumeration. Please see: https://schema.org/BodyMeasurementTypeEnumeration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BodyMeasurementTypeEnumerationAllProperties):
    pydantic_type = create_bodymeasurementtypeenumeration_model(model=model)
    return pydantic_type(model).schema_json()
