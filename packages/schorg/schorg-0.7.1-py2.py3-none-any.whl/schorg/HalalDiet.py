"""
A diet conforming to Islamic dietary practices.

https://schema.org/HalalDiet
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


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

    


class AllProperties(HalalDietInheritedProperties , HalalDietProperties, TypedDict):
    pass


class HalalDietBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HalalDiet",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HalalDietProperties, HalalDietInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HalalDiet"
    return model
    

HalalDiet = create_schema_org_model()


def create_halaldiet_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_halaldiet_model(model=model)
    return pydantic_type(model).schema_json()


