"""
Continental size system for wearables.

https://schema.org/WearableSizeSystemContinental
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemContinentalInheritedProperties(TypedDict):
    """Continental size system for wearables.

    References:
        https://schema.org/WearableSizeSystemContinental
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeSystemContinentalProperties(TypedDict):
    """Continental size system for wearables.

    References:
        https://schema.org/WearableSizeSystemContinental
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeSystemContinentalInheritedProperties , WearableSizeSystemContinentalProperties, TypedDict):
    pass


class WearableSizeSystemContinentalBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeSystemContinental",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeSystemContinentalProperties, WearableSizeSystemContinentalInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemContinental"
    return model
    

WearableSizeSystemContinental = create_schema_org_model()


def create_wearablesizesystemcontinental_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizesystemcontinental_model(model=model)
    return pydantic_type(model).schema_json()


