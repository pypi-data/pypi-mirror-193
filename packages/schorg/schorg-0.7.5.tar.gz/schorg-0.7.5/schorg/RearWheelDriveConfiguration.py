"""
Real-wheel drive is a transmission layout where the engine drives the rear wheels.

https://schema.org/RearWheelDriveConfiguration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class RearWheelDriveConfigurationAllProperties(
    RearWheelDriveConfigurationInheritedProperties,
    RearWheelDriveConfigurationProperties,
    TypedDict,
):
    pass


class RearWheelDriveConfigurationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="RearWheelDriveConfiguration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        RearWheelDriveConfigurationProperties,
        RearWheelDriveConfigurationInheritedProperties,
        RearWheelDriveConfigurationAllProperties,
    ] = RearWheelDriveConfigurationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "RearWheelDriveConfiguration"
    return model


RearWheelDriveConfiguration = create_schema_org_model()


def create_rearwheeldriveconfiguration_model(
    model: Union[
        RearWheelDriveConfigurationProperties,
        RearWheelDriveConfigurationInheritedProperties,
        RearWheelDriveConfigurationAllProperties,
    ]
):
    _type = deepcopy(RearWheelDriveConfigurationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of RearWheelDriveConfiguration. Please see: https://schema.org/RearWheelDriveConfiguration"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: RearWheelDriveConfigurationAllProperties):
    pydantic_type = create_rearwheeldriveconfiguration_model(model=model)
    return pydantic_type(model).schema_json()
