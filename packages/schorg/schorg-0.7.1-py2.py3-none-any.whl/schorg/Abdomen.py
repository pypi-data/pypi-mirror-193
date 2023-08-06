"""
Abdomen clinical examination.

https://schema.org/Abdomen
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class AbdomenInheritedProperties(TypedDict):
    """Abdomen clinical examination.

    References:
        https://schema.org/Abdomen
    Note:
        Model Depth 5
    Attributes:
    """

    


class AbdomenProperties(TypedDict):
    """Abdomen clinical examination.

    References:
        https://schema.org/Abdomen
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(AbdomenInheritedProperties , AbdomenProperties, TypedDict):
    pass


class AbdomenBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Abdomen",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[AbdomenProperties, AbdomenInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Abdomen"
    return model
    

Abdomen = create_schema_org_model()


def create_abdomen_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_abdomen_model(model=model)
    return pydantic_type(model).schema_json()


