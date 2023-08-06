"""
A computer store.

https://schema.org/ComputerStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class ComputerStoreInheritedProperties(TypedDict):
    """A computer store.

    References:
        https://schema.org/ComputerStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class ComputerStoreProperties(TypedDict):
    """A computer store.

    References:
        https://schema.org/ComputerStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(ComputerStoreInheritedProperties , ComputerStoreProperties, TypedDict):
    pass


class ComputerStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="ComputerStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[ComputerStoreProperties, ComputerStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "ComputerStore"
    return model
    

ComputerStore = create_schema_org_model()


def create_computerstore_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_computerstore_model(model=model)
    return pydantic_type(model).schema_json()


