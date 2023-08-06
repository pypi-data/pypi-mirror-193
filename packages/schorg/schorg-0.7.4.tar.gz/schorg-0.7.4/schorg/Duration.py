"""
Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).

https://schema.org/Duration
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DurationInheritedProperties(TypedDict):
    """Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).

    References:
        https://schema.org/Duration
    Note:
        Model Depth 4
    Attributes:
    """


class DurationProperties(TypedDict):
    """Quantity: Duration (use [ISO 8601 duration format](http://en.wikipedia.org/wiki/ISO_8601)).

    References:
        https://schema.org/Duration
    Note:
        Model Depth 4
    Attributes:
    """


class DurationAllProperties(DurationInheritedProperties, DurationProperties, TypedDict):
    pass


class DurationBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Duration", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DurationProperties, DurationInheritedProperties, DurationAllProperties
    ] = DurationAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Duration"
    return model


Duration = create_schema_org_model()


def create_duration_model(
    model: Union[DurationProperties, DurationInheritedProperties, DurationAllProperties]
):
    _type = deepcopy(DurationAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DurationAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DurationAllProperties):
    pydantic_type = create_duration_model(model=model)
    return pydantic_type(model).schema_json()
