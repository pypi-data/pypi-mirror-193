"""
A lake (for example, Lake Pontrachain).

https://schema.org/LakeBodyOfWater
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LakeBodyOfWaterInheritedProperties(TypedDict):
    """A lake (for example, Lake Pontrachain).

    References:
        https://schema.org/LakeBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """

    


class LakeBodyOfWaterProperties(TypedDict):
    """A lake (for example, Lake Pontrachain).

    References:
        https://schema.org/LakeBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(LakeBodyOfWaterInheritedProperties , LakeBodyOfWaterProperties, TypedDict):
    pass


class LakeBodyOfWaterBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LakeBodyOfWater",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LakeBodyOfWaterProperties, LakeBodyOfWaterInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LakeBodyOfWater"
    return model
    

LakeBodyOfWater = create_schema_org_model()


def create_lakebodyofwater_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_lakebodyofwater_model(model=model)
    return pydantic_type(model).schema_json()


