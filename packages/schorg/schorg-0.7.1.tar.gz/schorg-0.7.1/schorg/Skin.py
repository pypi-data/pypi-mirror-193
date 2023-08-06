"""
Skin assessment with clinical examination.

https://schema.org/Skin
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class SkinInheritedProperties(TypedDict):
    """Skin assessment with clinical examination.

    References:
        https://schema.org/Skin
    Note:
        Model Depth 5
    Attributes:
    """

    


class SkinProperties(TypedDict):
    """Skin assessment with clinical examination.

    References:
        https://schema.org/Skin
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(SkinInheritedProperties , SkinProperties, TypedDict):
    pass


class SkinBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="Skin",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[SkinProperties, SkinInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "Skin"
    return model
    

Skin = create_schema_org_model()


def create_skin_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_skin_model(model=model)
    return pydantic_type(model).schema_json()


