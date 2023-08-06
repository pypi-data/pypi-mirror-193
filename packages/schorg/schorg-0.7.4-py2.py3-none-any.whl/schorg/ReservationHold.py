"""
The status of a reservation on hold pending an update like credit card number or flight changes.

https://schema.org/ReservationHold
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReservationHoldInheritedProperties(TypedDict):
    """The status of a reservation on hold pending an update like credit card number or flight changes.

    References:
        https://schema.org/ReservationHold
    Note:
        Model Depth 6
    Attributes:
    """


class ReservationHoldProperties(TypedDict):
    """The status of a reservation on hold pending an update like credit card number or flight changes.

    References:
        https://schema.org/ReservationHold
    Note:
        Model Depth 6
    Attributes:
    """


class ReservationHoldAllProperties(
    ReservationHoldInheritedProperties, ReservationHoldProperties, TypedDict
):
    pass


class ReservationHoldBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReservationHold", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReservationHoldProperties,
        ReservationHoldInheritedProperties,
        ReservationHoldAllProperties,
    ] = ReservationHoldAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationHold"
    return model


ReservationHold = create_schema_org_model()


def create_reservationhold_model(
    model: Union[
        ReservationHoldProperties,
        ReservationHoldInheritedProperties,
        ReservationHoldAllProperties,
    ]
):
    _type = deepcopy(ReservationHoldAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of ReservationHoldAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: ReservationHoldAllProperties):
    pydantic_type = create_reservationhold_model(model=model)
    return pydantic_type(model).schema_json()
