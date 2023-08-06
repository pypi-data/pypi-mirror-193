"""
A body of water, such as a sea, ocean, or lake.

https://schema.org/BodyOfWater
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class BodyOfWaterInheritedProperties(TypedDict):
    """A body of water, such as a sea, ocean, or lake.

    References:
        https://schema.org/BodyOfWater
    Note:
        Model Depth 4
    Attributes:
    """

    


class BodyOfWaterProperties(TypedDict):
    """A body of water, such as a sea, ocean, or lake.

    References:
        https://schema.org/BodyOfWater
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(BodyOfWaterInheritedProperties , BodyOfWaterProperties, TypedDict):
    pass


class BodyOfWaterBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="BodyOfWater",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[BodyOfWaterProperties, BodyOfWaterInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "BodyOfWater"
    return model
    

BodyOfWater = create_schema_org_model()


def create_bodyofwater_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_bodyofwater_model(model=model)
    return pydantic_type(model).schema_json()


