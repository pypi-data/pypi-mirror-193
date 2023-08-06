"""
Enumerated status values for Reservation.

https://schema.org/ReservationStatusType
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ReservationStatusTypeInheritedProperties , ReservationStatusTypeProperties, TypedDict):
    pass


class ReservationStatusTypeBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReservationStatusType",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReservationStatusTypeProperties, ReservationStatusTypeInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationStatusType"
    return model
    

ReservationStatusType = create_schema_org_model()


def create_reservationstatustype_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reservationstatustype_model(model=model)
    return pydantic_type(model).schema_json()


