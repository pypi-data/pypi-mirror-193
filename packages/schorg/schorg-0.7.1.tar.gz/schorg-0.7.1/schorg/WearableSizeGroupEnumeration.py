"""
Enumerates common size groups (also known as "size types") for wearable products.

https://schema.org/WearableSizeGroupEnumeration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableSizeGroupEnumerationInheritedProperties(TypedDict):
    """Enumerates common size groups (also known as "size types") for wearable products.

    References:
        https://schema.org/WearableSizeGroupEnumeration
    Note:
        Model Depth 5
    Attributes:
    """

    


class WearableSizeGroupEnumerationProperties(TypedDict):
    """Enumerates common size groups (also known as "size types") for wearable products.

    References:
        https://schema.org/WearableSizeGroupEnumeration
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(WearableSizeGroupEnumerationInheritedProperties , WearableSizeGroupEnumerationProperties, TypedDict):
    pass


class WearableSizeGroupEnumerationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableSizeGroupEnumeration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableSizeGroupEnumerationProperties, WearableSizeGroupEnumerationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableSizeGroupEnumeration"
    return model
    

WearableSizeGroupEnumeration = create_schema_org_model()


def create_wearablesizegroupenumeration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablesizegroupenumeration_model(model=model)
    return pydantic_type(model).schema_json()


