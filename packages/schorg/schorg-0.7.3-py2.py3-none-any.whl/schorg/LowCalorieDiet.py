"""
A diet focused on reduced calorie intake.

https://schema.org/LowCalorieDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LowCalorieDietInheritedProperties(TypedDict):
    """A diet focused on reduced calorie intake.

    References:
        https://schema.org/LowCalorieDiet
    Note:
        Model Depth 5
    Attributes:
    """


class LowCalorieDietProperties(TypedDict):
    """A diet focused on reduced calorie intake.

    References:
        https://schema.org/LowCalorieDiet
    Note:
        Model Depth 5
    Attributes:
    """


class LowCalorieDietAllProperties(
    LowCalorieDietInheritedProperties, LowCalorieDietProperties, TypedDict
):
    pass


class LowCalorieDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="LowCalorieDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        LowCalorieDietProperties,
        LowCalorieDietInheritedProperties,
        LowCalorieDietAllProperties,
    ] = LowCalorieDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LowCalorieDiet"
    return model


LowCalorieDiet = create_schema_org_model()


def create_lowcaloriediet_model(
    model: Union[
        LowCalorieDietProperties,
        LowCalorieDietInheritedProperties,
        LowCalorieDietAllProperties,
    ]
):
    _type = deepcopy(LowCalorieDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: LowCalorieDietAllProperties):
    pydantic_type = create_lowcaloriediet_model(model=model)
    return pydantic_type(model).schema_json()
