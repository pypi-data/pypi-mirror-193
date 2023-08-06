"""
A gas station.

https://schema.org/GasStation
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GasStationInheritedProperties(TypedDict):
    """A gas station.

    References:
        https://schema.org/GasStation
    Note:
        Model Depth 5
    Attributes:
    """


class GasStationProperties(TypedDict):
    """A gas station.

    References:
        https://schema.org/GasStation
    Note:
        Model Depth 5
    Attributes:
    """


class GasStationAllProperties(
    GasStationInheritedProperties, GasStationProperties, TypedDict
):
    pass


class GasStationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="GasStation", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        GasStationProperties, GasStationInheritedProperties, GasStationAllProperties
    ] = GasStationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GasStation"
    return model


GasStation = create_schema_org_model()


def create_gasstation_model(
    model: Union[
        GasStationProperties, GasStationInheritedProperties, GasStationAllProperties
    ]
):
    _type = deepcopy(GasStationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of GasStation. Please see: https://schema.org/GasStation"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: GasStationAllProperties):
    pydantic_type = create_gasstation_model(model=model)
    return pydantic_type(model).schema_json()
