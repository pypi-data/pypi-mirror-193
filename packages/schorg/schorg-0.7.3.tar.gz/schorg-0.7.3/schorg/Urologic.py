"""
A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining to the urinary tract and the urogenital system.

https://schema.org/Urologic
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class UrologicInheritedProperties(TypedDict):
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining to the urinary tract and the urogenital system.

    References:
        https://schema.org/Urologic
    Note:
        Model Depth 6
    Attributes:
    """


class UrologicProperties(TypedDict):
    """A specific branch of medical science that is concerned with the diagnosis and treatment of diseases pertaining to the urinary tract and the urogenital system.

    References:
        https://schema.org/Urologic
    Note:
        Model Depth 6
    Attributes:
    """


class UrologicAllProperties(UrologicInheritedProperties, UrologicProperties, TypedDict):
    pass


class UrologicBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="Urologic", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        UrologicProperties, UrologicInheritedProperties, UrologicAllProperties
    ] = UrologicAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Urologic"
    return model


Urologic = create_schema_org_model()


def create_urologic_model(
    model: Union[UrologicProperties, UrologicInheritedProperties, UrologicAllProperties]
):
    _type = deepcopy(UrologicAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: UrologicAllProperties):
    pydantic_type = create_urologic_model(model=model)
    return pydantic_type(model).schema_json()
