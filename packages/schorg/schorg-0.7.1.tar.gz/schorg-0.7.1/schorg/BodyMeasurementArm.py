"""
Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts.

https://schema.org/BodyMeasurementArm
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyMeasurementArmInheritedProperties(TypedDict):
    """Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts.

    References:
        https://schema.org/BodyMeasurementArm
    Note:
        Model Depth 6
    Attributes:
    """

    


class BodyMeasurementArmProperties(TypedDict):
    """Arm length (measured between arms/shoulder line intersection and the prominent wrist bone). Used, for example, to fit shirts.

    References:
        https://schema.org/BodyMeasurementArm
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(BodyMeasurementArmInheritedProperties , BodyMeasurementArmProperties, TypedDict):
    pass


class BodyMeasurementArmBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyMeasurementArm",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyMeasurementArmProperties, BodyMeasurementArmInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyMeasurementArm"
    return model
    

BodyMeasurementArm = create_schema_org_model()


def create_bodymeasurementarm_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodymeasurementarm_model(model=model)
    return pydantic_type(model).schema_json()


