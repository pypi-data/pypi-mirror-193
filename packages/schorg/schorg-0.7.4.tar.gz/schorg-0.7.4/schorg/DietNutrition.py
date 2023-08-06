"""
Dietetics and nutrition as a medical specialty.

https://schema.org/DietNutrition
"""

from datetime import *
from copy import deepcopy
from typing import *
from time import *

from typing_extensions import TypedDict, NotRequired
from pydantic import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class DietNutritionInheritedProperties(TypedDict):
    """Dietetics and nutrition as a medical specialty.

    References:
        https://schema.org/DietNutrition
    Note:
        Model Depth 5
    Attributes:
    """


class DietNutritionProperties(TypedDict):
    """Dietetics and nutrition as a medical specialty.

    References:
        https://schema.org/DietNutrition
    Note:
        Model Depth 5
    Attributes:
    """


class DietNutritionAllProperties(
    DietNutritionInheritedProperties, DietNutritionProperties, TypedDict
):
    pass


class DietNutritionBaseModel(SchemaOrgBase):
    id_: Optional[Any] = Field(default="DietNutrition", alias="@id")
    context_: Optional[Any] = Field(default=None, alias="@context")
    graph_: Optional[Any] = Field(default=None, alias="@graph")

    class Config:
        ...


def create_schema_org_model(
    type_: Union[
        DietNutritionProperties,
        DietNutritionInheritedProperties,
        DietNutritionAllProperties,
    ] = DietNutritionAllProperties
) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DietNutrition"
    return model


DietNutrition = create_schema_org_model()


def create_dietnutrition_model(
    model: Union[
        DietNutritionProperties,
        DietNutritionInheritedProperties,
        DietNutritionAllProperties,
    ]
):
    _type = deepcopy(DietNutritionAllProperties)
    for k in model.__annotations__.keys():
        if k not in _type.__annotations__:
            raise TypeError(f"{k} not part of DietNutritionAllProperties")
    delete_keys = []
    for k in _type.__annotations__.keys():
        if k not in model.__annotations__:
            delete_keys.append(k)
    for k in delete_keys:
        del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: DietNutritionAllProperties):
    pydantic_type = create_dietnutrition_model(model=model)
    return pydantic_type(model).schema_json()
