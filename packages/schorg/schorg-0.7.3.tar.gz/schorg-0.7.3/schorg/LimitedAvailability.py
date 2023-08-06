"""
Indicates that the item has limited availability.

https://schema.org/LimitedAvailability
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LimitedAvailabilityInheritedProperties(TypedDict):
    """Indicates that the item has limited availability.

    References:
        https://schema.org/LimitedAvailability
    Note:
        Model Depth 5
    Attributes:
    """


class LimitedAvailabilityProperties(TypedDict):
    """Indicates that the item has limited availability.

    References:
        https://schema.org/LimitedAvailability
    Note:
        Model Depth 5
    Attributes:
    """


class LimitedAvailabilityAllProperties(
    LimitedAvailabilityInheritedProperties, LimitedAvailabilityProperties, TypedDict
):
    pass


class LimitedAvailabilityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LimitedAvailability", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LimitedAvailabilityProperties,
        LimitedAvailabilityInheritedProperties,
        LimitedAvailabilityAllProperties,
    ] = LimitedAvailabilityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LimitedAvailability"
    return model


LimitedAvailability = create_schema_org_model()


def create_limitedavailability_model(
    model: Union[
        LimitedAvailabilityProperties,
        LimitedAvailabilityInheritedProperties,
        LimitedAvailabilityAllProperties,
    ]
):
    _type = deepcopy(LimitedAvailabilityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LimitedAvailabilityAllProperties):
    pydantic_type = create_limitedavailability_model(model=model)
    return pydantic_type(model).schema_json()
