"""
An office equipment store.

https://schema.org/OfficeEquipmentStore
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class OfficeEquipmentStoreInheritedProperties(TypedDict):
    """An office equipment store.

    References:
        https://schema.org/OfficeEquipmentStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class OfficeEquipmentStoreProperties(TypedDict):
    """An office equipment store.

    References:
        https://schema.org/OfficeEquipmentStore
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(OfficeEquipmentStoreInheritedProperties , OfficeEquipmentStoreProperties, TypedDict):
    pass


class OfficeEquipmentStoreBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="OfficeEquipmentStore",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[OfficeEquipmentStoreProperties, OfficeEquipmentStoreInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "OfficeEquipmentStore"
    return model
    

OfficeEquipmentStore = create_schema_org_model()


def create_officeequipmentstore_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_officeequipmentstore_model(model=model)
    return pydantic_type(model).schema_json()


