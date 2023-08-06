"""
A diet exclusive of animal meat.

https://schema.org/VegetarianDiet
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VegetarianDietInheritedProperties(TypedDict):
    """A diet exclusive of animal meat.

    References:
        https://schema.org/VegetarianDiet
    Note:
        Model Depth 5
    Attributes:
    """


class VegetarianDietProperties(TypedDict):
    """A diet exclusive of animal meat.

    References:
        https://schema.org/VegetarianDiet
    Note:
        Model Depth 5
    Attributes:
    """


class VegetarianDietAllProperties(
    VegetarianDietInheritedProperties, VegetarianDietProperties, TypedDict
):
    pass


class VegetarianDietBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="VegetarianDiet", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        VegetarianDietProperties,
        VegetarianDietInheritedProperties,
        VegetarianDietAllProperties,
    ] = VegetarianDietAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "VegetarianDiet"
    return model


VegetarianDiet = create_schema_org_model()


def create_vegetariandiet_model(
    model: Union[
        VegetarianDietProperties,
        VegetarianDietInheritedProperties,
        VegetarianDietAllProperties,
    ]
):
    _type = deepcopy(VegetarianDietAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: VegetarianDietAllProperties):
    pydantic_type = create_vegetariandiet_model(model=model)
    return pydantic_type(model).schema_json()
