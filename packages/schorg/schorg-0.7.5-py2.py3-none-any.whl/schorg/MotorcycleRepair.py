"""
A motorcycle repair shop.

https://schema.org/MotorcycleRepair
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MotorcycleRepairInheritedProperties(TypedDict):
    """A motorcycle repair shop.

    References:
        https://schema.org/MotorcycleRepair
    Note:
        Model Depth 5
    Attributes:
    """


class MotorcycleRepairProperties(TypedDict):
    """A motorcycle repair shop.

    References:
        https://schema.org/MotorcycleRepair
    Note:
        Model Depth 5
    Attributes:
    """


class MotorcycleRepairAllProperties(
    MotorcycleRepairInheritedProperties, MotorcycleRepairProperties, TypedDict
):
    pass


class MotorcycleRepairBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="MotorcycleRepair", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        MotorcycleRepairProperties,
        MotorcycleRepairInheritedProperties,
        MotorcycleRepairAllProperties,
    ] = MotorcycleRepairAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MotorcycleRepair"
    return model


MotorcycleRepair = create_schema_org_model()


def create_motorcyclerepair_model(
    model: Union[
        MotorcycleRepairProperties,
        MotorcycleRepairInheritedProperties,
        MotorcycleRepairAllProperties,
    ]
):
    _type = deepcopy(MotorcycleRepairAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(
                f"{k} not part of MotorcycleRepair. Please see: https://schema.org/MotorcycleRepair"
            )
    # delete_keys = []
    # for k in _type.__annotations__.keys():
    #     if k not in model.__annotations__:
    #         delete_keys.append(k)
    # for k in delete_keys:
    #     del _type.__annotations__[k]
    return create_schema_org_model(type_=model)


def schema_json(model: MotorcycleRepairAllProperties):
    pydantic_type = create_motorcyclerepair_model(model=model)
    return pydantic_type(model).schema_json()
