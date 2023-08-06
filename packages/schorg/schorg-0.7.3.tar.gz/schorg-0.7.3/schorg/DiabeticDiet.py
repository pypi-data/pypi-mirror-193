"""
A diet appropriate for people with diabetes.

https://schema.org/DiabeticDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DiabeticDietInheritedProperties(TypedDict):
    """A diet appropriate for people with diabetes.

    References:
        https://schema.org/DiabeticDiet
    Note:
        Model Depth 5
    Attributes:
    """


class DiabeticDietProperties(TypedDict):
    """A diet appropriate for people with diabetes.

    References:
        https://schema.org/DiabeticDiet
    Note:
        Model Depth 5
    Attributes:
    """


class DiabeticDietAllProperties(
    DiabeticDietInheritedProperties, DiabeticDietProperties, TypedDict
):
    pass


class DiabeticDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DiabeticDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DiabeticDietProperties,
        DiabeticDietInheritedProperties,
        DiabeticDietAllProperties,
    ] = DiabeticDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DiabeticDiet"
    return model


DiabeticDiet = create_schema_org_model()


def create_diabeticdiet_model(
    model: Union[
        DiabeticDietProperties,
        DiabeticDietInheritedProperties,
        DiabeticDietAllProperties,
    ]
):
    _type = deepcopy(DiabeticDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DiabeticDietAllProperties):
    pydantic_type = create_diabeticdiet_model(model=model)
    return pydantic_type(model).schema_json()
