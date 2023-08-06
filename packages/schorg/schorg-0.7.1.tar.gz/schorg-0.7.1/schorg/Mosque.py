"""
A mosque.

https://schema.org/Mosque
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MosqueInheritedProperties(TypedDict):
    """A mosque.

    References:
        https://schema.org/Mosque
    Note:
        Model Depth 5
    Attributes:
    """

    


class MosqueProperties(TypedDict):
    """A mosque.

    References:
        https://schema.org/Mosque
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MosqueInheritedProperties , MosqueProperties, TypedDict):
    pass


class MosqueBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Mosque",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MosqueProperties, MosqueInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Mosque"
    return model
    

Mosque = create_schema_org_model()


def create_mosque_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mosque_model(model=model)
    return pydantic_type(model).schema_json()


