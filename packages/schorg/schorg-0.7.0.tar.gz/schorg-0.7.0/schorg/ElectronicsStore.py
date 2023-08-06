"""
An electronics store.

https://schema.org/ElectronicsStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ElectronicsStoreInheritedProperties(TypedDict):
    """An electronics store.

    References:
        https://schema.org/ElectronicsStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class ElectronicsStoreProperties(TypedDict):
    """An electronics store.

    References:
        https://schema.org/ElectronicsStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ElectronicsStoreInheritedProperties , ElectronicsStoreProperties, TypedDict):
    pass


class ElectronicsStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ElectronicsStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ElectronicsStoreProperties, ElectronicsStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ElectronicsStore"
    return model
    

ElectronicsStore = create_schema_org_model()


def create_electronicsstore_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_electronicsstore_model(model=model)
    return pydantic_type(model).schema_json()


