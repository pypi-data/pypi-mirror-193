"""
Pathogenic virus that causes viral infection.

https://schema.org/Virus
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class VirusInheritedProperties(TypedDict):
    """Pathogenic virus that causes viral infection.

    References:
        https://schema.org/Virus
    Note:
        Model Depth 6
    Attributes:
    """

    


class VirusProperties(TypedDict):
    """Pathogenic virus that causes viral infection.

    References:
        https://schema.org/Virus
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(VirusInheritedProperties , VirusProperties, TypedDict):
    pass


class VirusBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Virus",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[VirusProperties, VirusInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Virus"
    return model
    

Virus = create_schema_org_model()


def create_virus_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_virus_model(model=model)
    return pydantic_type(model).schema_json()


