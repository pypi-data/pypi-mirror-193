"""
Japanese size system for wearables.

https://schema.org/WearableSizeSystemJP
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeSystemJPInheritedProperties(TypedDict):
    """Japanese size system for wearables.

    References:
        https://schema.org/WearableSizeSystemJP
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeSystemJPProperties(TypedDict):
    """Japanese size system for wearables.

    References:
        https://schema.org/WearableSizeSystemJP
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeSystemJPInheritedProperties , WearableSizeSystemJPProperties, TypedDict):
    pass


class WearableSizeSystemJPBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeSystemJP",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeSystemJPProperties, WearableSizeSystemJPInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeSystemJP"
    return model
    

WearableSizeSystemJP = create_schema_org_model()


def create_wearablesizesystemjp_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizesystemjp_model(model=model)
    return pydantic_type(model).schema_json()


