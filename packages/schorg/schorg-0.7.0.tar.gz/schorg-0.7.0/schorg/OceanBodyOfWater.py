"""
An ocean (for example, the Pacific).

https://schema.org/OceanBodyOfWater
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OceanBodyOfWaterInheritedProperties(TypedDict):
    """An ocean (for example, the Pacific).

    References:
        https://schema.org/OceanBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """

    


class OceanBodyOfWaterProperties(TypedDict):
    """An ocean (for example, the Pacific).

    References:
        https://schema.org/OceanBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(OceanBodyOfWaterInheritedProperties , OceanBodyOfWaterProperties, TypedDict):
    pass


class OceanBodyOfWaterBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OceanBodyOfWater",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OceanBodyOfWaterProperties, OceanBodyOfWaterInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OceanBodyOfWater"
    return model
    

OceanBodyOfWater = create_schema_org_model()


def create_oceanbodyofwater_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_oceanbodyofwater_model(model=model)
    return pydantic_type(model).schema_json()


