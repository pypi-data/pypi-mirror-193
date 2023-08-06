"""
HealthCare: this is a benefit for health care.

https://schema.org/HealthCare
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthCareInheritedProperties(TypedDict):
    """HealthCare: this is a benefit for health care.

    References:
        https://schema.org/HealthCare
    Note:
        Model Depth 5
    Attributes:
    """

    


class HealthCareProperties(TypedDict):
    """HealthCare: this is a benefit for health care.

    References:
        https://schema.org/HealthCare
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HealthCareInheritedProperties , HealthCareProperties, TypedDict):
    pass


class HealthCareBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HealthCare",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HealthCareProperties, HealthCareInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthCare"
    return model
    

HealthCare = create_schema_org_model()


def create_healthcare_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_healthcare_model(model=model)
    return pydantic_type(model).schema_json()


