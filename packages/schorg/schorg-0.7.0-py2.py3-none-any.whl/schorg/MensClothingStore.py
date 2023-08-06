"""
A men's clothing store.

https://schema.org/MensClothingStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MensClothingStoreInheritedProperties(TypedDict):
    """A men's clothing store.

    References:
        https://schema.org/MensClothingStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class MensClothingStoreProperties(TypedDict):
    """A men's clothing store.

    References:
        https://schema.org/MensClothingStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(MensClothingStoreInheritedProperties , MensClothingStoreProperties, TypedDict):
    pass


class MensClothingStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MensClothingStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[MensClothingStoreProperties, MensClothingStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MensClothingStore"
    return model
    

MensClothingStore = create_schema_org_model()


def create_mensclothingstore_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_mensclothingstore_model(model=model)
    return pydantic_type(model).schema_json()


