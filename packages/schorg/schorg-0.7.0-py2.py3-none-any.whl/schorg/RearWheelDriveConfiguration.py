"""
Real-wheel drive is a transmission layout where the engine drives the rear wheels.

https://schema.org/RearWheelDriveConfiguration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class RearWheelDriveConfigurationInheritedProperties(TypedDict):
    """Real-wheel drive is a transmission layout where the engine drives the rear wheels.

    References:
        https://schema.org/RearWheelDriveConfiguration
    Note:
        Model Depth 6
    Attributes:
    """

    


class RearWheelDriveConfigurationProperties(TypedDict):
    """Real-wheel drive is a transmission layout where the engine drives the rear wheels.

    References:
        https://schema.org/RearWheelDriveConfiguration
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(RearWheelDriveConfigurationInheritedProperties , RearWheelDriveConfigurationProperties, TypedDict):
    pass


class RearWheelDriveConfigurationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="RearWheelDriveConfiguration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[RearWheelDriveConfigurationProperties, RearWheelDriveConfigurationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RearWheelDriveConfiguration"
    return model
    

RearWheelDriveConfiguration = create_schema_org_model()


def create_rearwheeldriveconfiguration_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_rearwheeldriveconfiguration_model(model=model)
    return pydantic_type(model).schema_json()


