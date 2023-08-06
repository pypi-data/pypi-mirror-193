"""
A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.

https://schema.org/Hematologic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HematologicInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.

    References:
        https://schema.org/Hematologic
    Note:
        Model Depth 6
    Attributes:
    """

    


class HematologicProperties(TypedDict):
    """A specific branch of medical science that pertains to diagnosis and treatment of disorders of blood and blood producing organs.

    References:
        https://schema.org/Hematologic
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(HematologicInheritedProperties , HematologicProperties, TypedDict):
    pass


class HematologicBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Hematologic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HematologicProperties, HematologicInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Hematologic"
    return model
    

Hematologic = create_schema_org_model()


def create_hematologic_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_hematologic_model(model=model)
    return pydantic_type(model).schema_json()


