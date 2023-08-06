"""
Front-wheel drive is a transmission layout where the engine drives the front wheels.

https://schema.org/FrontWheelDriveConfiguration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FrontWheelDriveConfigurationInheritedProperties(TypedDict):
    """Front-wheel drive is a transmission layout where the engine drives the front wheels.

    References:
        https://schema.org/FrontWheelDriveConfiguration
    Note:
        Model Depth 6
    Attributes:
    """

    


class FrontWheelDriveConfigurationProperties(TypedDict):
    """Front-wheel drive is a transmission layout where the engine drives the front wheels.

    References:
        https://schema.org/FrontWheelDriveConfiguration
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(FrontWheelDriveConfigurationInheritedProperties , FrontWheelDriveConfigurationProperties, TypedDict):
    pass


class FrontWheelDriveConfigurationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="FrontWheelDriveConfiguration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FrontWheelDriveConfigurationProperties, FrontWheelDriveConfigurationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FrontWheelDriveConfiguration"
    return model
    

FrontWheelDriveConfiguration = create_schema_org_model()


def create_frontwheeldriveconfiguration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_frontwheeldriveconfiguration_model(model=model)
    return pydantic_type(model).schema_json()


