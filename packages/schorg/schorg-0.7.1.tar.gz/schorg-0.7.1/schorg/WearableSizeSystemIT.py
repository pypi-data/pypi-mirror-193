"""
Italian size system for wearables.

https://schema.org/WearableSizeSystemIT
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemITInheritedProperties(TypedDict):
    """Italian size system for wearables.

    References:
        https://schema.org/WearableSizeSystemIT
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeSystemITProperties(TypedDict):
    """Italian size system for wearables.

    References:
        https://schema.org/WearableSizeSystemIT
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeSystemITInheritedProperties , WearableSizeSystemITProperties, TypedDict):
    pass


class WearableSizeSystemITBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeSystemIT",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeSystemITProperties, WearableSizeSystemITInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemIT"
    return model
    

WearableSizeSystemIT = create_schema_org_model()


def create_wearablesizesystemit_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizesystemit_model(model=model)
    return pydantic_type(model).schema_json()


