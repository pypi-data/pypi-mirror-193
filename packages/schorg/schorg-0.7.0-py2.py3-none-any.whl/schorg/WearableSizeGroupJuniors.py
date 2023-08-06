"""
Size group "Juniors" for wearables.

https://schema.org/WearableSizeGroupJuniors
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupJuniorsInheritedProperties(TypedDict):
    """Size group "Juniors" for wearables.

    References:
        https://schema.org/WearableSizeGroupJuniors
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeGroupJuniorsProperties(TypedDict):
    """Size group "Juniors" for wearables.

    References:
        https://schema.org/WearableSizeGroupJuniors
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeGroupJuniorsInheritedProperties , WearableSizeGroupJuniorsProperties, TypedDict):
    pass


class WearableSizeGroupJuniorsBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeGroupJuniors",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeGroupJuniorsProperties, WearableSizeGroupJuniorsInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupJuniors"
    return model
    

WearableSizeGroupJuniors = create_schema_org_model()


def create_wearablesizegroupjuniors_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizegroupjuniors_model(model=model)
    return pydantic_type(model).schema_json()


