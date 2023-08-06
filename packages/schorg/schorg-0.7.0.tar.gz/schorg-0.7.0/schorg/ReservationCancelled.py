"""
The status for a previously confirmed reservation that is now cancelled.

https://schema.org/ReservationCancelled
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(ReservationCancelledInheritedProperties , ReservationCancelledProperties, TypedDict):
    pass


class ReservationCancelledBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ReservationCancelled",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ReservationCancelledProperties, ReservationCancelledInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ReservationCancelled"
    return model
    

ReservationCancelled = create_schema_org_model()


def create_reservationcancelled_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_reservationcancelled_model(model=model)
    return pydantic_type(model).schema_json()


