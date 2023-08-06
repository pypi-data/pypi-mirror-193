"""
Dietetics and nutrition as a medical specialty.

https://schema.org/DietNutrition
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(DietNutritionInheritedProperties , DietNutritionProperties, TypedDict):
    pass


class DietNutritionBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DietNutrition",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DietNutritionProperties, DietNutritionInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DietNutrition"
    return model
    

DietNutrition = create_schema_org_model()


def create_dietnutrition_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_dietnutrition_model(model=model)
    return pydantic_type(model).schema_json()


