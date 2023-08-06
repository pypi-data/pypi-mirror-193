"""
Represents the distance fee (e.g., price per km or mile) part of the total price for an offered product, for example a car rental.

https://schema.org/DistanceFee
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DistanceFeeInheritedProperties(TypedDict):
    """Represents the distance fee (e.g., price per km or mile) part of the total price for an offered product, for example a car rental.

    References:
        https://schema.org/DistanceFee
    Note:
        Model Depth 5
    Attributes:
    """


class DistanceFeeProperties(TypedDict):
    """Represents the distance fee (e.g., price per km or mile) part of the total price for an offered product, for example a car rental.

    References:
        https://schema.org/DistanceFee
    Note:
        Model Depth 5
    Attributes:
    """


class DistanceFeeAllProperties(
    DistanceFeeInheritedProperties, DistanceFeeProperties, TypedDict
):
    pass


class DistanceFeeBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DistanceFee", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DistanceFeeProperties, DistanceFeeInheritedProperties, DistanceFeeAllProperties
    ] = DistanceFeeAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DistanceFee"
    return model


DistanceFee = create_schema_org_model()


def create_distancefee_model(
    model: Union[
        DistanceFeeProperties, DistanceFeeInheritedProperties, DistanceFeeAllProperties
    ]
):
    _type = deepcopy(DistanceFeeAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DistanceFeeAllProperties):
    pydantic_type = create_distancefee_model(model=model)
    return pydantic_type(model).schema_json()
