"""
The status of a confirmed reservation.

https://schema.org/ReservationConfirmed
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReservationConfirmedInheritedProperties(TypedDict):
    """The status of a confirmed reservation.

    References:
        https://schema.org/ReservationConfirmed
    Note:
        Model Depth 6
    Attributes:
    """


class ReservationConfirmedProperties(TypedDict):
    """The status of a confirmed reservation.

    References:
        https://schema.org/ReservationConfirmed
    Note:
        Model Depth 6
    Attributes:
    """


class ReservationConfirmedAllProperties(
    ReservationConfirmedInheritedProperties, ReservationConfirmedProperties, TypedDict
):
    pass


class ReservationConfirmedBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReservationConfirmed", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReservationConfirmedProperties,
        ReservationConfirmedInheritedProperties,
        ReservationConfirmedAllProperties,
    ] = ReservationConfirmedAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationConfirmed"
    return model


ReservationConfirmed = create_schema_org_model()


def create_reservationconfirmed_model(
    model: Union[
        ReservationConfirmedProperties,
        ReservationConfirmedInheritedProperties,
        ReservationConfirmedAllProperties,
    ]
):
    _type = deepcopy(ReservationConfirmedAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ReservationConfirmedAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReservationConfirmedAllProperties):
    pydantic_type = create_reservationconfirmed_model(model=model)
    return pydantic_type(model).schema_json()
