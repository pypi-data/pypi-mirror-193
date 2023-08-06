"""
A state or province of a country.

https://schema.org/State
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class StateAllProperties(StateInheritedProperties, StateProperties, TypedDict):
    pass


class StateBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="State", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        StateProperties, StateInheritedProperties, StateAllProperties
    ] = StateAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "State"
    return model


State = create_schema_org_model()


def create_state_model(
    model: Union[StateProperties, StateInheritedProperties, StateAllProperties]
):
    _type = deepcopy(StateAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of State. Please see: https://schema.org/State"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: StateAllProperties):
    pydantic_type = create_state_model(model=model)
    return pydantic_type(model).schema_json()
