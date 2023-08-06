"""
A reservoir of water, typically an artificially created lake, like the Lake Kariba reservoir.

https://schema.org/Reservoir
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ReservoirInheritedProperties , ReservoirProperties, TypedDict):
    pass


class ReservoirBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Reservoir",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReservoirProperties, ReservoirInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Reservoir"
    return model
    

Reservoir = create_schema_org_model()


def create_reservoir_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reservoir_model(model=model)
    return pydantic_type(model).schema_json()


