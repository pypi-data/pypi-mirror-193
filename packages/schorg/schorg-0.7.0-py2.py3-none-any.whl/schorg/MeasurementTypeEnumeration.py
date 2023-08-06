"""
Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.

https://schema.org/MeasurementTypeEnumeration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class MeasurementTypeEnumerationInheritedProperties(TypedDict):
    """Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.

    References:
        https://schema.org/MeasurementTypeEnumeration
    Note:
        Model Depth 4
    Attributes:
        supersededBy: (Optional[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]): Relates a term (i.e. a property, class or enumeration) to one that supersedes it.
    """

    supersededBy: NotRequired[Union[List[Union[SchemaOrgObj, str]], SchemaOrgObj, str]]
    


class MeasurementTypeEnumerationProperties(TypedDict):
    """Enumeration of common measurement types (or dimensions), for example "chest" for a person, "inseam" for pants, "gauge" for screws, or "wheel" for bicycles.

    References:
        https://schema.org/MeasurementTypeEnumeration
    Note:
        Model Depth 4
    Attributes:
    """

    


class AllProperties(MeasurementTypeEnumerationInheritedProperties , MeasurementTypeEnumerationProperties, TypedDict):
    pass


class MeasurementTypeEnumerationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="MeasurementTypeEnumeration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        
        fields = {'supersededBy': {'exclude': True}}
        


def create_schema_org_model(type_: Union[MeasurementTypeEnumerationProperties, MeasurementTypeEnumerationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "MeasurementTypeEnumeration"
    return model
    

MeasurementTypeEnumeration = create_schema_org_model()


def create_measurementtypeenumeration_model(model: AllProperties):
    _type =  AllProperties.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_measurementtypeenumeration_model(model=model)
    return pydantic_type(model).schema_json()


