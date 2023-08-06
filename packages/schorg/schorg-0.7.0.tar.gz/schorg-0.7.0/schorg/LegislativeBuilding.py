"""
A legislative building&#x2014;for example, the state capitol.

https://schema.org/LegislativeBuilding
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class LegislativeBuildingInheritedProperties(TypedDict):
    """A legislative building&#x2014;for example, the state capitol.

    References:
        https://schema.org/LegislativeBuilding
    Note:
        Model Depth 5
    Attributes:
    """

    


class LegislativeBuildingProperties(TypedDict):
    """A legislative building&#x2014;for example, the state capitol.

    References:
        https://schema.org/LegislativeBuilding
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(LegislativeBuildingInheritedProperties , LegislativeBuildingProperties, TypedDict):
    pass


class LegislativeBuildingBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="LegislativeBuilding",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[LegislativeBuildingProperties, LegislativeBuildingInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "LegislativeBuilding"
    return model
    

LegislativeBuilding = create_schema_org_model()


def create_legislativebuilding_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_legislativebuilding_model(model=model)
    return pydantic_type(model).schema_json()


