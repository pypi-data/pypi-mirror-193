"""
A sea (for example, the Caspian sea).

https://schema.org/SeaBodyOfWater
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SeaBodyOfWaterInheritedProperties(TypedDict):
    """A sea (for example, the Caspian sea).

    References:
        https://schema.org/SeaBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """


class SeaBodyOfWaterProperties(TypedDict):
    """A sea (for example, the Caspian sea).

    References:
        https://schema.org/SeaBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """


class SeaBodyOfWaterAllProperties(
    SeaBodyOfWaterInheritedProperties, SeaBodyOfWaterProperties, TypedDict
):
    pass


class SeaBodyOfWaterBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="SeaBodyOfWater", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        SeaBodyOfWaterProperties,
        SeaBodyOfWaterInheritedProperties,
        SeaBodyOfWaterAllProperties,
    ] = SeaBodyOfWaterAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SeaBodyOfWater"
    return model


SeaBodyOfWater = create_schema_org_model()


def create_seabodyofwater_model(
    model: Union[
        SeaBodyOfWaterProperties,
        SeaBodyOfWaterInheritedProperties,
        SeaBodyOfWaterAllProperties,
    ]
):
    _type = deepcopy(SeaBodyOfWaterAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of SeaBodyOfWater. Please see: https://schema.org/SeaBodyOfWater"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: SeaBodyOfWaterAllProperties):
    pydantic_type = create_seabodyofwater_model(model=model)
    return pydantic_type(model).schema_json()
