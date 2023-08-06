"""
Indicates full game availability.

https://schema.org/FullGameAvailability
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class FullGameAvailabilityInheritedProperties(TypedDict):
    """Indicates full game availability.

    References:
        https://schema.org/FullGameAvailability
    Note:
        Model Depth 5
    Attributes:
    """


class FullGameAvailabilityProperties(TypedDict):
    """Indicates full game availability.

    References:
        https://schema.org/FullGameAvailability
    Note:
        Model Depth 5
    Attributes:
    """


class FullGameAvailabilityAllProperties(
    FullGameAvailabilityInheritedProperties, FullGameAvailabilityProperties, TypedDict
):
    pass


class FullGameAvailabilityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="FullGameAvailability", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        FullGameAvailabilityProperties,
        FullGameAvailabilityInheritedProperties,
        FullGameAvailabilityAllProperties,
    ] = FullGameAvailabilityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "FullGameAvailability"
    return model


FullGameAvailability = create_schema_org_model()


def create_fullgameavailability_model(
    model: Union[
        FullGameAvailabilityProperties,
        FullGameAvailabilityInheritedProperties,
        FullGameAvailabilityAllProperties,
    ]
):
    _type = deepcopy(FullGameAvailabilityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of FullGameAvailability. Please see: https://schema.org/FullGameAvailability"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: FullGameAvailabilityAllProperties):
    pydantic_type = create_fullgameavailability_model(model=model)
    return pydantic_type(model).schema_json()
