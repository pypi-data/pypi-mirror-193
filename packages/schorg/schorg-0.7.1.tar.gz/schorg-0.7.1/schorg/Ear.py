"""
Ear function assessment with clinical examination.

https://schema.org/Ear
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class EarInheritedProperties(TypedDict):
    """Ear function assessment with clinical examination.

    References:
        https://schema.org/Ear
    Note:
        Model Depth 5
    Attributes:
    """

    


class EarProperties(TypedDict):
    """Ear function assessment with clinical examination.

    References:
        https://schema.org/Ear
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(EarInheritedProperties , EarProperties, TypedDict):
    pass


class EarBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Ear",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[EarProperties, EarInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Ear"
    return model
    

Ear = create_schema_org_model()


def create_ear_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_ear_model(model=model)
    return pydantic_type(model).schema_json()


