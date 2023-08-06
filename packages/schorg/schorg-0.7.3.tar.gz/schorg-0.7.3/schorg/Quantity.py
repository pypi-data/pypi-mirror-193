"""
Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.

https://schema.org/Quantity
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class QuantityInheritedProperties(TypedDict):
    """Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.

    References:
        https://schema.org/Quantity
    Note:
        Model Depth 3
    Attributes:
    """


class QuantityProperties(TypedDict):
    """Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 kg' or '4 milligrams'.

    References:
        https://schema.org/Quantity
    Note:
        Model Depth 3
    Attributes:
    """


class QuantityAllProperties(QuantityInheritedProperties, QuantityProperties, TypedDict):
    pass


class QuantityBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Quantity", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        QuantityProperties, QuantityInheritedProperties, QuantityAllProperties
    ] = QuantityAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Quantity"
    return model


Quantity = create_schema_org_model()


def create_quantity_model(
    model: Union[QuantityProperties, QuantityInheritedProperties, QuantityAllProperties]
):
    _type = deepcopy(QuantityAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: QuantityAllProperties):
    pydantic_type = create_quantity_model(model=model)
    return pydantic_type(model).schema_json()
