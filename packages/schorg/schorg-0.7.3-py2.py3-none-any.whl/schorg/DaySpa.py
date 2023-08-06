"""
A day spa.

https://schema.org/DaySpa
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DaySpaInheritedProperties(TypedDict):
    """A day spa.

    References:
        https://schema.org/DaySpa
    Note:
        Model Depth 5
    Attributes:
    """


class DaySpaProperties(TypedDict):
    """A day spa.

    References:
        https://schema.org/DaySpa
    Note:
        Model Depth 5
    Attributes:
    """


class DaySpaAllProperties(DaySpaInheritedProperties, DaySpaProperties, TypedDict):
    pass


class DaySpaBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DaySpa", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DaySpaProperties, DaySpaInheritedProperties, DaySpaAllProperties
    ] = DaySpaAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DaySpa"
    return model


DaySpa = create_schema_org_model()


def create_dayspa_model(
    model: Union[DaySpaProperties, DaySpaInheritedProperties, DaySpaAllProperties]
):
    _type = deepcopy(DaySpaAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DaySpaAllProperties):
    pydantic_type = create_dayspa_model(model=model)
    return pydantic_type(model).schema_json()
