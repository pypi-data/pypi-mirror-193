"""
A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders.

https://schema.org/Genetic
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GeneticInheritedProperties(TypedDict):
    """A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders.

    References:
        https://schema.org/Genetic
    Note:
        Model Depth 6
    Attributes:
    """

    


class GeneticProperties(TypedDict):
    """A specific branch of medical science that pertains to hereditary transmission and the variation of inherited characteristics and disorders.

    References:
        https://schema.org/Genetic
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(GeneticInheritedProperties , GeneticProperties, TypedDict):
    pass


class GeneticBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Genetic",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[GeneticProperties, GeneticInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Genetic"
    return model
    

Genetic = create_schema_org_model()


def create_genetic_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_genetic_model(model=model)
    return pydantic_type(model).schema_json()


