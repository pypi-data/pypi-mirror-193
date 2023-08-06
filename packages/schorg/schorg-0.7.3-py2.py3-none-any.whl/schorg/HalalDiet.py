"""
A diet conforming to Islamic dietary practices.

https://schema.org/HalalDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HalalDietInheritedProperties(TypedDict):
    """A diet conforming to Islamic dietary practices.

    References:
        https://schema.org/HalalDiet
    Note:
        Model Depth 5
    Attributes:
    """


class HalalDietProperties(TypedDict):
    """A diet conforming to Islamic dietary practices.

    References:
        https://schema.org/HalalDiet
    Note:
        Model Depth 5
    Attributes:
    """


class HalalDietAllProperties(
    HalalDietInheritedProperties, HalalDietProperties, TypedDict
):
    pass


class HalalDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="HalalDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        HalalDietProperties, HalalDietInheritedProperties, HalalDietAllProperties
    ] = HalalDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HalalDiet"
    return model


HalalDiet = create_schema_org_model()


def create_halaldiet_model(
    model: Union[
        HalalDietProperties, HalalDietInheritedProperties, HalalDietAllProperties
    ]
):
    _type = deepcopy(HalalDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: HalalDietAllProperties):
    pydantic_type = create_halaldiet_model(model=model)
    return pydantic_type(model).schema_json()
