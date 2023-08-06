"""
All-wheel Drive is a transmission layout where the engine drives all four wheels.

https://schema.org/AllWheelDriveConfiguration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AllWheelDriveConfigurationInheritedProperties(TypedDict):
    """All-wheel Drive is a transmission layout where the engine drives all four wheels.

    References:
        https://schema.org/AllWheelDriveConfiguration
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllWheelDriveConfigurationProperties(TypedDict):
    """All-wheel Drive is a transmission layout where the engine drives all four wheels.

    References:
        https://schema.org/AllWheelDriveConfiguration
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(AllWheelDriveConfigurationInheritedProperties , AllWheelDriveConfigurationProperties, TypedDict):
    pass


class AllWheelDriveConfigurationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="AllWheelDriveConfiguration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AllWheelDriveConfigurationProperties, AllWheelDriveConfigurationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AllWheelDriveConfiguration"
    return model
    

AllWheelDriveConfiguration = create_schema_org_model()


def create_allwheeldriveconfiguration_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_allwheeldriveconfiguration_model(model=model)
    return pydantic_type(model).schema_json()


