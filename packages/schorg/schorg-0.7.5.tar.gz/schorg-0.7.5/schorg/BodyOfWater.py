"""
A body of water, such as a sea, ocean, or lake.

https://schema.org/BodyOfWater
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyOfWaterInheritedProperties(TypedDict):
    """A body of water, such as a sea, ocean, or lake.

    References:
        https://schema.org/BodyOfWater
    Note:
        Model Depth 4
    Attributes:
    """


class BodyOfWaterProperties(TypedDict):
    """A body of water, such as a sea, ocean, or lake.

    References:
        https://schema.org/BodyOfWater
    Note:
        Model Depth 4
    Attributes:
    """


class BodyOfWaterAllProperties(
    BodyOfWaterInheritedProperties, BodyOfWaterProperties, TypedDict
):
    pass


class BodyOfWaterBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="BodyOfWater", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        BodyOfWaterProperties, BodyOfWaterInheritedProperties, BodyOfWaterAllProperties
    ] = BodyOfWaterAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyOfWater"
    return model


BodyOfWater = create_schema_org_model()


def create_bodyofwater_model(
    model: Union[
        BodyOfWaterProperties, BodyOfWaterInheritedProperties, BodyOfWaterAllProperties
    ]
):
    _type = deepcopy(BodyOfWaterAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of BodyOfWater. Please see: https://schema.org/BodyOfWater"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: BodyOfWaterAllProperties):
    pydantic_type = create_bodyofwater_model(model=model)
    return pydantic_type(model).schema_json()
