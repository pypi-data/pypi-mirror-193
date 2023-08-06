"""
All-wheel Drive is a transmission layout where the engine drives all four wheels.

https://schema.org/AllWheelDriveConfiguration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class AllWheelDriveConfigurationAllProperties(
    AllWheelDriveConfigurationInheritedProperties,
    AllWheelDriveConfigurationProperties,
    TypedDict,
):
    pass


class AllWheelDriveConfigurationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AllWheelDriveConfiguration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AllWheelDriveConfigurationProperties,
        AllWheelDriveConfigurationInheritedProperties,
        AllWheelDriveConfigurationAllProperties,
    ] = AllWheelDriveConfigurationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AllWheelDriveConfiguration"
    return model


AllWheelDriveConfiguration = create_schema_org_model()


def create_allwheeldriveconfiguration_model(
    model: Union[
        AllWheelDriveConfigurationProperties,
        AllWheelDriveConfigurationInheritedProperties,
        AllWheelDriveConfigurationAllProperties,
    ]
):
    _type = deepcopy(AllWheelDriveConfigurationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllWheelDriveConfigurationAllProperties):
    pydantic_type = create_allwheeldriveconfiguration_model(model=model)
    return pydantic_type(model).schema_json()
