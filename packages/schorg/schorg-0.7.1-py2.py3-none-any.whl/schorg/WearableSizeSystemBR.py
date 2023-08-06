"""
Brazilian size system for wearables.

https://schema.org/WearableSizeSystemBR
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemBRInheritedProperties(TypedDict):
    """Brazilian size system for wearables.

    References:
        https://schema.org/WearableSizeSystemBR
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeSystemBRProperties(TypedDict):
    """Brazilian size system for wearables.

    References:
        https://schema.org/WearableSizeSystemBR
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeSystemBRInheritedProperties , WearableSizeSystemBRProperties, TypedDict):
    pass


class WearableSizeSystemBRBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeSystemBR",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeSystemBRProperties, WearableSizeSystemBRInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemBR"
    return model
    

WearableSizeSystemBR = create_schema_org_model()


def create_wearablesizesystembr_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizesystembr_model(model=model)
    return pydantic_type(model).schema_json()


