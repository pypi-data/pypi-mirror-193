"""
A state or province of a country.

https://schema.org/State
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class StateInheritedProperties(TypedDict):
    """A state or province of a country.

    References:
        https://schema.org/State
    Note:
        Model Depth 4
    Attributes:
    """

    


class StateProperties(TypedDict):
    """A state or province of a country.

    References:
        https://schema.org/State
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(StateInheritedProperties , StateProperties, TypedDict):
    pass


class StateBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="State",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[StateProperties, StateInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "State"
    return model
    

State = create_schema_org_model()


def create_state_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_state_model(model=model)
    return pydantic_type(model).schema_json()


