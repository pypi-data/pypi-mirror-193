"""
Girth of hips (measured around the buttocks). Used, for example, to fit skirts.

https://schema.org/BodyMeasurementHips
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(BodyMeasurementHipsInheritedProperties , BodyMeasurementHipsProperties, TypedDict):
    pass


class BodyMeasurementHipsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementHips",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementHipsProperties, BodyMeasurementHipsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementHips"
    return model
    

BodyMeasurementHips = create_schema_org_model()


def create_bodymeasurementhips_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementhips_model(model=model)
    return pydantic_type(model).schema_json()


