"""
A diet focused on reduced sodium intake.

https://schema.org/LowSaltDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LowSaltDietInheritedProperties(TypedDict):
    """A diet focused on reduced sodium intake.

    References:
        https://schema.org/LowSaltDiet
    Note:
        Model Depth 5
    Attributes:
    """


class LowSaltDietProperties(TypedDict):
    """A diet focused on reduced sodium intake.

    References:
        https://schema.org/LowSaltDiet
    Note:
        Model Depth 5
    Attributes:
    """


class LowSaltDietAllProperties(
    LowSaltDietInheritedProperties, LowSaltDietProperties, TypedDict
):
    pass


class LowSaltDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LowSaltDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LowSaltDietProperties, LowSaltDietInheritedProperties, LowSaltDietAllProperties
    ] = LowSaltDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LowSaltDiet"
    return model


LowSaltDiet = create_schema_org_model()


def create_lowsaltdiet_model(
    model: Union[
        LowSaltDietProperties, LowSaltDietInheritedProperties, LowSaltDietAllProperties
    ]
):
    _type = deepcopy(LowSaltDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LowSaltDietAllProperties):
    pydantic_type = create_lowsaltdiet_model(model=model)
    return pydantic_type(model).schema_json()
