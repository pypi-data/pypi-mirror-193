"""
Size group "Extra Short" for wearables.

https://schema.org/WearableSizeGroupExtraShort
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupExtraShortInheritedProperties(TypedDict):
    """Size group "Extra Short" for wearables.

    References:
        https://schema.org/WearableSizeGroupExtraShort
    Note:
        Model Depth 6
    Attributes:
    """

    


class WearableSizeGroupExtraShortProperties(TypedDict):
    """Size group "Extra Short" for wearables.

    References:
        https://schema.org/WearableSizeGroupExtraShort
    Note:
        Model Depth 6
    Attributes:
    """

    


class AllProperties(WearableSizeGroupExtraShortInheritedProperties , WearableSizeGroupExtraShortProperties, TypedDict):
    pass


class WearableSizeGroupExtraShortBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeGroupExtraShort",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeGroupExtraShortProperties, WearableSizeGroupExtraShortInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupExtraShort"
    return model
    

WearableSizeGroupExtraShort = create_schema_org_model()


def create_wearablesizegroupextrashort_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizegroupextrashort_model(model=model)
    return pydantic_type(model).schema_json()


