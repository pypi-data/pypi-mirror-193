"""
Inside leg (measured between crotch and soles of feet). Used, for example, to fit pants.

https://schema.org/BodyMeasurementInsideLeg
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(BodyMeasurementInsideLegInheritedProperties , BodyMeasurementInsideLegProperties, TypedDict):
    pass


class BodyMeasurementInsideLegBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementInsideLeg",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementInsideLegProperties, BodyMeasurementInsideLegInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementInsideLeg"
    return model
    

BodyMeasurementInsideLeg = create_schema_org_model()


def create_bodymeasurementinsideleg_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementinsideleg_model(model=model)
    return pydantic_type(model).schema_json()


