"""
Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel drive capability.

https://schema.org/FourWheelDriveConfiguration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FourWheelDriveConfigurationInheritedProperties(TypedDict):
    """Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel drive capability.

    References:
        https://schema.org/FourWheelDriveConfiguration
    Note:
        Model Depth 6
    Attributes:
    """

    


class FourWheelDriveConfigurationProperties(TypedDict):
    """Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel drive capability.

    References:
        https://schema.org/FourWheelDriveConfiguration
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(FourWheelDriveConfigurationInheritedProperties , FourWheelDriveConfigurationProperties, TypedDict):
    pass


class FourWheelDriveConfigurationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="FourWheelDriveConfiguration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[FourWheelDriveConfigurationProperties, FourWheelDriveConfigurationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FourWheelDriveConfiguration"
    return model
    

FourWheelDriveConfiguration = create_schema_org_model()


def create_fourwheeldriveconfiguration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_fourwheeldriveconfiguration_model(model=model)
    return pydantic_type(model).schema_json()


