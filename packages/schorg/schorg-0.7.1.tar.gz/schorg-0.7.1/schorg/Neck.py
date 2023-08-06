"""
Neck assessment with clinical examination.

https://schema.org/Neck
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class NeckInheritedProperties(TypedDict):
    """Neck assessment with clinical examination.

    References:
        https://schema.org/Neck
    Note:
        Model Depth 5
    Attributes:
    """

    


class NeckProperties(TypedDict):
    """Neck assessment with clinical examination.

    References:
        https://schema.org/Neck
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(NeckInheritedProperties , NeckProperties, TypedDict):
    pass


class NeckBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Neck",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[NeckProperties, NeckInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Neck"
    return model
    

Neck = create_schema_org_model()


def create_neck_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_neck_model(model=model)
    return pydantic_type(model).schema_json()


