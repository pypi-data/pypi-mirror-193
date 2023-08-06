"""
A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

https://schema.org/Reservoir
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReservoirInheritedProperties(TypedDict):
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

    References:
        https://schema.org/Reservoir
    Note:
        Model Depth 5
    Attributes:
    """


class ReservoirProperties(TypedDict):
    """A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

    References:
        https://schema.org/Reservoir
    Note:
        Model Depth 5
    Attributes:
    """


class ReservoirAllProperties(
    ReservoirInheritedProperties, ReservoirProperties, TypedDict
):
    pass


class ReservoirBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Reservoir", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReservoirProperties, ReservoirInheritedProperties, ReservoirAllProperties
    ] = ReservoirAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Reservoir"
    return model


Reservoir = create_schema_org_model()


def create_reservoir_model(
    model: Union[
        ReservoirProperties, ReservoirInheritedProperties, ReservoirAllProperties
    ]
):
    _type = deepcopy(ReservoirAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReservoirAllProperties):
    pydantic_type = create_reservoir_model(model=model)
    return pydantic_type(model).schema_json()
