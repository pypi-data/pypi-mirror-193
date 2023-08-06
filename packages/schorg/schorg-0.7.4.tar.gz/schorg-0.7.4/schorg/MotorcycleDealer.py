"""
A motorcycle dealer.

https://schema.org/MotorcycleDealer
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


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


class MotorcycleDealerAllProperties(
    MotorcycleDealerInheritedProperties, MotorcycleDealerProperties, TypedDict
):
    pass


class MotorcycleDealerBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MotorcycleDealer", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MotorcycleDealerProperties,
        MotorcycleDealerInheritedProperties,
        MotorcycleDealerAllProperties,
    ] = MotorcycleDealerAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MotorcycleDealer"
    return model


MotorcycleDealer = create_schema_org_model()


def create_motorcycledealer_model(
    model: Union[
        MotorcycleDealerProperties,
        MotorcycleDealerInheritedProperties,
        MotorcycleDealerAllProperties,
    ]
):
    _type = deepcopy(MotorcycleDealerAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of MotorcycleDealerAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: MotorcycleDealerAllProperties):
    pydantic_type = create_motorcycledealer_model(model=model)
    return pydantic_type(model).schema_json()
