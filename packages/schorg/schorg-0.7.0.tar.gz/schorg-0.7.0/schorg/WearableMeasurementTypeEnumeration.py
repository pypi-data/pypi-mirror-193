"""
Enumerates common types of measurement for wearables products.

https://schema.org/WearableMeasurementTypeEnumeration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class WearableMeasurementTypeEnumerationInheritedProperties(TypedDict):
    """Enumerates common types of measurement for wearables products.

    References:
        https://schema.org/WearableMeasurementTypeEnumeration
    Note:
        Model Depth 5
    Attributes:
    """

    


class WearableMeasurementTypeEnumerationProperties(TypedDict):
    """Enumerates common types of measurement for wearables products.

    References:
        https://schema.org/WearableMeasurementTypeEnumeration
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(WearableMeasurementTypeEnumerationInheritedProperties , WearableMeasurementTypeEnumerationProperties, TypedDict):
    pass


class WearableMeasurementTypeEnumerationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="WearableMeasurementTypeEnumeration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[WearableMeasurementTypeEnumerationProperties, WearableMeasurementTypeEnumerationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "WearableMeasurementTypeEnumeration"
    return model
    

WearableMeasurementTypeEnumeration = create_schema_org_model()


def create_wearablemeasurementtypeenumeration_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_wearablemeasurementtypeenumeration_model(model=model)
    return pydantic_type(model).schema_json()


