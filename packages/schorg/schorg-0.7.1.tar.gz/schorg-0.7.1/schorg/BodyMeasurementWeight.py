"""
Body weight. Used, for example, to measure pantyhose.

https://schema.org/BodyMeasurementWeight
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(BodyMeasurementWeightInheritedProperties , BodyMeasurementWeightProperties, TypedDict):
    pass


class BodyMeasurementWeightBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementWeight",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementWeightProperties, BodyMeasurementWeightInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementWeight"
    return model
    

BodyMeasurementWeight = create_schema_org_model()


def create_bodymeasurementweight_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementweight_model(model=model)
    return pydantic_type(model).schema_json()


