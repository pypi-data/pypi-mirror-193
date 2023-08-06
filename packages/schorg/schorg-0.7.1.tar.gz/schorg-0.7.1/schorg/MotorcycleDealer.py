"""
A motorcycle dealer.

https://schema.org/MotorcycleDealer
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MotorcycleDealerInheritedProperties(TypedDict):
    """A motorcycle dealer.

    References:
        https://schema.org/MotorcycleDealer
    Note:
        Model Depth 5
    Attributes:
    """

    


class MotorcycleDealerProperties(TypedDict):
    """A motorcycle dealer.

    References:
        https://schema.org/MotorcycleDealer
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MotorcycleDealerInheritedProperties , MotorcycleDealerProperties, TypedDict):
    pass


class MotorcycleDealerBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MotorcycleDealer",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MotorcycleDealerProperties, MotorcycleDealerInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MotorcycleDealer"
    return model
    

MotorcycleDealer = create_schema_org_model()


def create_motorcycledealer_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_motorcycledealer_model(model=model)
    return pydantic_type(model).schema_json()


