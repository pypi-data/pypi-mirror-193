"""
A garden store.

https://schema.org/GardenStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class GardenStoreInheritedProperties(TypedDict):
    """A garden store.

    References:
        https://schema.org/GardenStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class GardenStoreProperties(TypedDict):
    """A garden store.

    References:
        https://schema.org/GardenStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(GardenStoreInheritedProperties , GardenStoreProperties, TypedDict):
    pass


class GardenStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="GardenStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[GardenStoreProperties, GardenStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "GardenStore"
    return model
    

GardenStore = create_schema_org_model()


def create_gardenstore_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_gardenstore_model(model=model)
    return pydantic_type(model).schema_json()


