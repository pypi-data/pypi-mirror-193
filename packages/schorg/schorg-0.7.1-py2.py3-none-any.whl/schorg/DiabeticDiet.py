"""
A diet appropriate for people with diabetes.

https://schema.org/DiabeticDiet
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(DiabeticDietInheritedProperties , DiabeticDietProperties, TypedDict):
    pass


class DiabeticDietBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="DiabeticDiet",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[DiabeticDietProperties, DiabeticDietInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "DiabeticDiet"
    return model
    

DiabeticDiet = create_schema_org_model()


def create_diabeticdiet_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_diabeticdiet_model(model=model)
    return pydantic_type(model).schema_json()


