"""
A car rental business.

https://schema.org/AutoRental
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AutoRentalInheritedProperties(TypedDict):
    """A car rental business.

    References:
        https://schema.org/AutoRental
    Note:
        Model Depth 5
    Attributes:
    """


class AutoRentalProperties(TypedDict):
    """A car rental business.

    References:
        https://schema.org/AutoRental
    Note:
        Model Depth 5
    Attributes:
    """


class AutoRentalAllProperties(
    AutoRentalInheritedProperties, AutoRentalProperties, TypedDict
):
    pass


class AutoRentalBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="AutoRental", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        AutoRentalProperties, AutoRentalInheritedProperties, AutoRentalAllProperties
    ] = AutoRentalAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "AutoRental"
    return model


AutoRental = create_schema_org_model()


def create_autorental_model(
    model: Union[
        AutoRentalProperties, AutoRentalInheritedProperties, AutoRentalAllProperties
    ]
):
    _type = deepcopy(AutoRentalAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AutoRentalAllProperties):
    pydantic_type = create_autorental_model(model=model)
    return pydantic_type(model).schema_json()
