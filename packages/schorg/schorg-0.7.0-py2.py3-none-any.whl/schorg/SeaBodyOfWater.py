"""
A sea (for example, the Caspian sea).

https://schema.org/SeaBodyOfWater
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SeaBodyOfWaterInheritedProperties(TypedDict):
    """A sea (for example, the Caspian sea).

    References:
        https://schema.org/SeaBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """

    


class SeaBodyOfWaterProperties(TypedDict):
    """A sea (for example, the Caspian sea).

    References:
        https://schema.org/SeaBodyOfWater
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SeaBodyOfWaterInheritedProperties , SeaBodyOfWaterProperties, TypedDict):
    pass


class SeaBodyOfWaterBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="SeaBodyOfWater",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SeaBodyOfWaterProperties, SeaBodyOfWaterInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "SeaBodyOfWater"
    return model
    

SeaBodyOfWater = create_schema_org_model()


def create_seabodyofwater_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_seabodyofwater_model(model=model)
    return pydantic_type(model).schema_json()


