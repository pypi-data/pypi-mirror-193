"""
Size group "Maternity" for wearables.

https://schema.org/WearableSizeGroupMaternity
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupMaternityInheritedProperties(TypedDict):
    """Size group "Maternity" for wearables.

    References:
        https://schema.org/WearableSizeGroupMaternity
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeGroupMaternityProperties(TypedDict):
    """Size group "Maternity" for wearables.

    References:
        https://schema.org/WearableSizeGroupMaternity
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeGroupMaternityInheritedProperties , WearableSizeGroupMaternityProperties, TypedDict):
    pass


class WearableSizeGroupMaternityBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeGroupMaternity",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeGroupMaternityProperties, WearableSizeGroupMaternityInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupMaternity"
    return model
    

WearableSizeGroupMaternity = create_schema_org_model()


def create_wearablesizegroupmaternity_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizegroupmaternity_model(model=model)
    return pydantic_type(model).schema_json()


