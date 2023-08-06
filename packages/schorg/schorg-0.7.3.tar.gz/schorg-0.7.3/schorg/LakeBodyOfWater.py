"""
A lake (for example, Lake Pontrachain).

https://schema.org/LakeBodyOfWater
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LakeBodyOfWaterInheritedProperties(TypedDict):
    """A lake (for example, Lake Pontrachain).

    References:
        https://schema.org/LakeBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """


class LakeBodyOfWaterProperties(TypedDict):
    """A lake (for example, Lake Pontrachain).

    References:
        https://schema.org/LakeBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """


class LakeBodyOfWaterAllProperties(
    LakeBodyOfWaterInheritedProperties, LakeBodyOfWaterProperties, TypedDict
):
    pass


class LakeBodyOfWaterBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LakeBodyOfWater", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LakeBodyOfWaterProperties,
        LakeBodyOfWaterInheritedProperties,
        LakeBodyOfWaterAllProperties,
    ] = LakeBodyOfWaterAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LakeBodyOfWater"
    return model


LakeBodyOfWater = create_schema_org_model()


def create_lakebodyofwater_model(
    model: Union[
        LakeBodyOfWaterProperties,
        LakeBodyOfWaterInheritedProperties,
        LakeBodyOfWaterAllProperties,
    ]
):
    _type = deepcopy(LakeBodyOfWaterAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LakeBodyOfWaterAllProperties):
    pydantic_type = create_lakebodyofwater_model(model=model)
    return pydantic_type(model).schema_json()
