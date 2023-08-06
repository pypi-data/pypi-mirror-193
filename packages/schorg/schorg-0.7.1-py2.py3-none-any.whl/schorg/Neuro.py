"""
Neurological system clinical examination.

https://schema.org/Neuro
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NeuroInheritedProperties(TypedDict):
    """Neurological system clinical examination.

    References:
        https://schema.org/Neuro
    Note:
        Model Depth 5
    Attributes:
    """

    


class NeuroProperties(TypedDict):
    """Neurological system clinical examination.

    References:
        https://schema.org/Neuro
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(NeuroInheritedProperties , NeuroProperties, TypedDict):
    pass


class NeuroBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Neuro",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[NeuroProperties, NeuroInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Neuro"
    return model
    

Neuro = create_schema_org_model()


def create_neuro_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_neuro_model(model=model)
    return pydantic_type(model).schema_json()


