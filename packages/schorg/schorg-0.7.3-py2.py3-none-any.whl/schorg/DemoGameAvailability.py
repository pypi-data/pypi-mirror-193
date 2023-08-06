"""
Indicates demo game availability, i.e. a somehow limited demonstration of the full game.

https://schema.org/DemoGameAvailability
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DemoGameAvailabilityInheritedProperties(TypedDict):
    """Indicates demo game availability, i.e. a somehow limited demonstration of the full game.

    References:
        https://schema.org/DemoGameAvailability
    Note:
        Model Depth 5
    Attributes:
    """


class DemoGameAvailabilityProperties(TypedDict):
    """Indicates demo game availability, i.e. a somehow limited demonstration of the full game.

    References:
        https://schema.org/DemoGameAvailability
    Note:
        Model Depth 5
    Attributes:
    """


class DemoGameAvailabilityAllProperties(
    DemoGameAvailabilityInheritedProperties, DemoGameAvailabilityProperties, TypedDict
):
    pass


class DemoGameAvailabilityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DemoGameAvailability", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DemoGameAvailabilityProperties,
        DemoGameAvailabilityInheritedProperties,
        DemoGameAvailabilityAllProperties,
    ] = DemoGameAvailabilityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DemoGameAvailability"
    return model


DemoGameAvailability = create_schema_org_model()


def create_demogameavailability_model(
    model: Union[
        DemoGameAvailabilityProperties,
        DemoGameAvailabilityInheritedProperties,
        DemoGameAvailabilityAllProperties,
    ]
):
    _type = deepcopy(DemoGameAvailabilityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DemoGameAvailabilityAllProperties):
    pydantic_type = create_demogameavailability_model(model=model)
    return pydantic_type(model).schema_json()
