"""
GS1 (formerly NRF) size system for wearables.

https://schema.org/WearableSizeSystemGS1
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemGS1InheritedProperties(TypedDict):
    """GS1 (formerly NRF) size system for wearables.

    References:
        https://schema.org/WearableSizeSystemGS1
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeSystemGS1Properties(TypedDict):
    """GS1 (formerly NRF) size system for wearables.

    References:
        https://schema.org/WearableSizeSystemGS1
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeSystemGS1InheritedProperties , WearableSizeSystemGS1Properties, TypedDict):
    pass


class WearableSizeSystemGS1BaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeSystemGS1",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeSystemGS1Properties, WearableSizeSystemGS1InheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemGS1"
    return model
    

WearableSizeSystemGS1 = create_schema_org_model()


def create_wearablesizesystemgs1_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizesystemgs1_model(model=model)
    return pydantic_type(model).schema_json()


