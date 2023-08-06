"""
Size group "Extra Tall" for wearables.

https://schema.org/WearableSizeGroupExtraTall
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupExtraTallInheritedProperties(TypedDict):
    """Size group "Extra Tall" for wearables.

    References:
        https://schema.org/WearableSizeGroupExtraTall
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeGroupExtraTallProperties(TypedDict):
    """Size group "Extra Tall" for wearables.

    References:
        https://schema.org/WearableSizeGroupExtraTall
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeGroupExtraTallInheritedProperties , WearableSizeGroupExtraTallProperties, TypedDict):
    pass


class WearableSizeGroupExtraTallBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeGroupExtraTall",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeGroupExtraTallProperties, WearableSizeGroupExtraTallInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupExtraTall"
    return model
    

WearableSizeGroupExtraTall = create_schema_org_model()


def create_wearablesizegroupextratall_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizegroupextratall_model(model=model)
    return pydantic_type(model).schema_json()


