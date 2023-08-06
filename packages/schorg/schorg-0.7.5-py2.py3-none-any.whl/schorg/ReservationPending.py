"""
The status of a reservation when a request has been sent, but not confirmed.

https://schema.org/ReservationPending
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ReservationPendingInheritedProperties(TypedDict):
    """The status of a reservation when a request has been sent, but not confirmed.

    References:
        https://schema.org/ReservationPending
    Note:
        Model Depth 6
    Attributes:
    """


class ReservationPendingProperties(TypedDict):
    """The status of a reservation when a request has been sent, but not confirmed.

    References:
        https://schema.org/ReservationPending
    Note:
        Model Depth 6
    Attributes:
    """


class ReservationPendingAllProperties(
    ReservationPendingInheritedProperties, ReservationPendingProperties, TypedDict
):
    pass


class ReservationPendingBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="ReservationPending", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        ReservationPendingProperties,
        ReservationPendingInheritedProperties,
        ReservationPendingAllProperties,
    ] = ReservationPendingAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationPending"
    return model


ReservationPending = create_schema_org_model()


def create_reservationpending_model(
    model: Union[
        ReservationPendingProperties,
        ReservationPendingInheritedProperties,
        ReservationPendingAllProperties,
    ]
):
    _type = deepcopy(ReservationPendingAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of ReservationPending. Please see: https://schema.org/ReservationPending"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: ReservationPendingAllProperties):
    pydantic_type = create_reservationpending_model(model=model)
    return pydantic_type(model).schema_json()
