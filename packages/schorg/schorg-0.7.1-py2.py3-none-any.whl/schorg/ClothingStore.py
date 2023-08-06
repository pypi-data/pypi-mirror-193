"""
A clothing store.

https://schema.org/ClothingStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ClothingStoreInheritedProperties(TypedDict):
    """A clothing store.

    References:
        https://schema.org/ClothingStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class ClothingStoreProperties(TypedDict):
    """A clothing store.

    References:
        https://schema.org/ClothingStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ClothingStoreInheritedProperties , ClothingStoreProperties, TypedDict):
    pass


class ClothingStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ClothingStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ClothingStoreProperties, ClothingStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ClothingStore"
    return model
    

ClothingStore = create_schema_org_model()


def create_clothingstore_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_clothingstore_model(model=model)
    return pydantic_type(model).schema_json()


