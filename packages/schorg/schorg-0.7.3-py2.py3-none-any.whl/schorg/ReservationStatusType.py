"""
Enumerated status values for Reservation.

https://schema.org/ReservationStatusType
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReservationStatusTypeInheritedProperties(TypedDict):
    """Enumerated status values for Reservation.

    References:
        https://schema.org/ReservationStatusType
    Note:
        Model Depth 5
    Attributes:
    """


class ReservationStatusTypeProperties(TypedDict):
    """Enumerated status values for Reservation.

    References:
        https://schema.org/ReservationStatusType
    Note:
        Model Depth 5
    Attributes:
    """


class ReservationStatusTypeAllProperties(
    ReservationStatusTypeInheritedProperties, ReservationStatusTypeProperties, TypedDict
):
    pass


class ReservationStatusTypeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReservationStatusType", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReservationStatusTypeProperties,
        ReservationStatusTypeInheritedProperties,
        ReservationStatusTypeAllProperties,
    ] = ReservationStatusTypeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationStatusType"
    return model


ReservationStatusType = create_schema_org_model()


def create_reservationstatustype_model(
    model: Union[
        ReservationStatusTypeProperties,
        ReservationStatusTypeInheritedProperties,
        ReservationStatusTypeAllProperties,
    ]
):
    _type = deepcopy(ReservationStatusTypeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReservationStatusTypeAllProperties):
    pydantic_type = create_reservationstatustype_model(model=model)
    return pydantic_type(model).schema_json()
