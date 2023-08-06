"""
The status of a confirmed reservation.

https://schema.org/ReservationConfirmed
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ReservationConfirmedInheritedProperties , ReservationConfirmedProperties, TypedDict):
    pass


class ReservationConfirmedBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReservationConfirmed",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReservationConfirmedProperties, ReservationConfirmedInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationConfirmed"
    return model
    

ReservationConfirmed = create_schema_org_model()


def create_reservationconfirmed_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reservationconfirmed_model(model=model)
    return pydantic_type(model).schema_json()


