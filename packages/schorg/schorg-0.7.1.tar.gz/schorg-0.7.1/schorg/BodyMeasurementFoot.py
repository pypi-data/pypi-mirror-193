"""
Foot length (measured between end of the most prominent toe and the most prominent part of the heel). Used, for example, to measure socks.

https://schema.org/BodyMeasurementFoot
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementFootInheritedProperties(TypedDict):
    """Foot length (measured between end of the most prominent toe and the most prominent part of the heel). Used, for example, to measure socks.

    References:
        https://schema.org/BodyMeasurementFoot
    Note:
        Model Depth 6
    Attributes:
    """

    


class BodyMeasurementFootProperties(TypedDict):
    """Foot length (measured between end of the most prominent toe and the most prominent part of the heel). Used, for example, to measure socks.

    References:
        https://schema.org/BodyMeasurementFoot
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(BodyMeasurementFootInheritedProperties , BodyMeasurementFootProperties, TypedDict):
    pass


class BodyMeasurementFootBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementFoot",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementFootProperties, BodyMeasurementFootInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementFoot"
    return model
    

BodyMeasurementFoot = create_schema_org_model()


def create_bodymeasurementfoot_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementfoot_model(model=model)
    return pydantic_type(model).schema_json()


