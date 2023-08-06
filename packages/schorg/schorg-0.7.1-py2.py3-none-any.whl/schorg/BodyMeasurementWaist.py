"""
Girth of natural waistline (between hip bones and lower ribs). Used, for example, to fit pants.

https://schema.org/BodyMeasurementWaist
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(BodyMeasurementWaistInheritedProperties , BodyMeasurementWaistProperties, TypedDict):
    pass


class BodyMeasurementWaistBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementWaist",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementWaistProperties, BodyMeasurementWaistInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementWaist"
    return model
    

BodyMeasurementWaist = create_schema_org_model()


def create_bodymeasurementwaist_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementwaist_model(model=model)
    return pydantic_type(model).schema_json()


