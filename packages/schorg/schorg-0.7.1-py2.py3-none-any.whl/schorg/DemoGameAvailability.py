"""
Indicates demo game availability, i.e. a somehow limited demonstration of the full game.

https://schema.org/DemoGameAvailability
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(DemoGameAvailabilityInheritedProperties , DemoGameAvailabilityProperties, TypedDict):
    pass


class DemoGameAvailabilityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DemoGameAvailability",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DemoGameAvailabilityProperties, DemoGameAvailabilityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DemoGameAvailability"
    return model
    

DemoGameAvailability = create_schema_org_model()


def create_demogameavailability_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_demogameavailability_model(model=model)
    return pydantic_type(model).schema_json()


