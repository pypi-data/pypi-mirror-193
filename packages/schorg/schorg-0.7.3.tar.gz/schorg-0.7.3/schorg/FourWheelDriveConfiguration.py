"""
Four-wheel drive is a transmission layout where the engine primarily drives two wheels with a part-time four-wheel drive capability.

https://schema.org/FourWheelDriveConfiguration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class FourWheelDriveConfigurationAllProperties(
    FourWheelDriveConfigurationInheritedProperties,
    FourWheelDriveConfigurationProperties,
    TypedDict,
):
    pass


class FourWheelDriveConfigurationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FourWheelDriveConfiguration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FourWheelDriveConfigurationProperties,
        FourWheelDriveConfigurationInheritedProperties,
        FourWheelDriveConfigurationAllProperties,
    ] = FourWheelDriveConfigurationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FourWheelDriveConfiguration"
    return model


FourWheelDriveConfiguration = create_schema_org_model()


def create_fourwheeldriveconfiguration_model(
    model: Union[
        FourWheelDriveConfigurationProperties,
        FourWheelDriveConfigurationInheritedProperties,
        FourWheelDriveConfigurationAllProperties,
    ]
):
    _type = deepcopy(FourWheelDriveConfigurationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: FourWheelDriveConfigurationAllProperties):
    pydantic_type = create_fourwheeldriveconfiguration_model(model=model)
    return pydantic_type(model).schema_json()
