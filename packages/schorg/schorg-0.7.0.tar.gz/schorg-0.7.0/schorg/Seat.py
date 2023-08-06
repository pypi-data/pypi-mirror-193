"""
Used to describe a seat, such as a reserved seat in an event reservation.

https://schema.org/Seat
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SeatInheritedProperties(TypedDict):
    """Used to describe a seat, such as a reserved seat in an event reservation.

    References:
        https://schema.org/Seat
    Note:
        Model Depth 3
    Attributes:
    """

    


class SeatProperties(TypedDict):
    """Used to describe a seat, such as a reserved seat in an event reservation.

    References:
        https://schema.org/Seat
    Note:
        Model Depth 3
    Attributes:
        seatSection: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The section location of the reserved seat (e.g. Orchestra).
        seatNumber: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The location of the reserved seat (e.g., 27).
        seatingType: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The type/class of the seat.
        seatRow: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): The row location of the reserved seat (e.g., B).
    """

    seatSection: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    seatNumber: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    seatingType: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    seatRow: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class AllProperties(SeatInheritedProperties , SeatProperties, TypedDict):
    pass


class SeatBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Seat",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'seatSection': {'exclude': True}}
        fields = {'seatNumber': {'exclude': True}}
        fields = {'seatingType': {'exclude': True}}
        fields = {'seatRow': {'exclude': True}}
        


def create_schema_org_model(type_: Union[SeatProperties, SeatInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Seat"
    return model
    

Seat = create_schema_org_model()


def create_seat_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_seat_model(model=model)
    return pydantic_type(model).schema_json()


