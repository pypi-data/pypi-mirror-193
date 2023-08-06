"""
A diet conforming to Hindu dietary practices, in particular, beef-free.

https://schema.org/HinduDiet
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HinduDietInheritedProperties(TypedDict):
    """A diet conforming to Hindu dietary practices, in particular, beef-free.

    References:
        https://schema.org/HinduDiet
    Note:
        Model Depth 5
    Attributes:
    """

    


class HinduDietProperties(TypedDict):
    """A diet conforming to Hindu dietary practices, in particular, beef-free.

    References:
        https://schema.org/HinduDiet
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HinduDietInheritedProperties , HinduDietProperties, TypedDict):
    pass


class HinduDietBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HinduDiet",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HinduDietProperties, HinduDietInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HinduDiet"
    return model
    

HinduDiet = create_schema_org_model()


def create_hindudiet_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_hindudiet_model(model=model)
    return pydantic_type(model).schema_json()


