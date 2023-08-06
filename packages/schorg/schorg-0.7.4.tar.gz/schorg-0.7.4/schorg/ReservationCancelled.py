"""
The status for a previously confirmed reservation that is now cancelled.

https://schema.org/ReservationCancelled
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReservationCancelledInheritedProperties(TypedDict):
    """The status for a previously confirmed reservation that is now cancelled.

    References:
        https://schema.org/ReservationCancelled
    Note:
        Model Depth 6
    Attributes:
    """


class ReservationCancelledProperties(TypedDict):
    """The status for a previously confirmed reservation that is now cancelled.

    References:
        https://schema.org/ReservationCancelled
    Note:
        Model Depth 6
    Attributes:
    """


class ReservationCancelledAllProperties(
    ReservationCancelledInheritedProperties, ReservationCancelledProperties, TypedDict
):
    pass


class ReservationCancelledBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReservationCancelled", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReservationCancelledProperties,
        ReservationCancelledInheritedProperties,
        ReservationCancelledAllProperties,
    ] = ReservationCancelledAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationCancelled"
    return model


ReservationCancelled = create_schema_org_model()


def create_reservationcancelled_model(
    model: Union[
        ReservationCancelledProperties,
        ReservationCancelledInheritedProperties,
        ReservationCancelledAllProperties,
    ]
):
    _type = deepcopy(ReservationCancelledAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ReservationCancelledAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReservationCancelledAllProperties):
    pydantic_type = create_reservationcancelled_model(model=model)
    return pydantic_type(model).schema_json()
