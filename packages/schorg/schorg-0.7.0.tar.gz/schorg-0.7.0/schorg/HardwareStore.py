"""
A hardware store.

https://schema.org/HardwareStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HardwareStoreInheritedProperties(TypedDict):
    """A hardware store.

    References:
        https://schema.org/HardwareStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class HardwareStoreProperties(TypedDict):
    """A hardware store.

    References:
        https://schema.org/HardwareStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HardwareStoreInheritedProperties , HardwareStoreProperties, TypedDict):
    pass


class HardwareStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HardwareStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HardwareStoreProperties, HardwareStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HardwareStore"
    return model
    

HardwareStore = create_schema_org_model()


def create_hardwarestore_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_hardwarestore_model(model=model)
    return pydantic_type(model).schema_json()


