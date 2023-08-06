"""
A toy store.

https://schema.org/ToyStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ToyStoreInheritedProperties(TypedDict):
    """A toy store.

    References:
        https://schema.org/ToyStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class ToyStoreProperties(TypedDict):
    """A toy store.

    References:
        https://schema.org/ToyStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ToyStoreInheritedProperties , ToyStoreProperties, TypedDict):
    pass


class ToyStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ToyStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ToyStoreProperties, ToyStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ToyStore"
    return model
    

ToyStore = create_schema_org_model()


def create_toystore_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_toystore_model(model=model)
    return pydantic_type(model).schema_json()


