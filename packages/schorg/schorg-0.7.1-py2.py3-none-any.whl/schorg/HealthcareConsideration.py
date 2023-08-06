"""
Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.

https://schema.org/HealthcareConsideration
"""

from typing import *
from typing_extensions import TypedDict, NotRequired
from pydantic import *
from datetime import *
from time import *


from schorg.schema_org_obj import SchemaOrgObj, SchemaOrgBase


class HealthcareConsiderationInheritedProperties(TypedDict):
    """Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.

    References:
        https://schema.org/HealthcareConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class HealthcareConsiderationProperties(TypedDict):
    """Item is a pharmaceutical (e.g., a prescription or OTC drug) or a restricted medical device.

    References:
        https://schema.org/HealthcareConsideration
    Note:
        Model Depth 5
    Attributes:
    """

    


class AllProperties(HealthcareConsiderationInheritedProperties , HealthcareConsiderationProperties, TypedDict):
    pass


class HealthcareConsiderationBaseModel(SchemaOrgBase):
    id_ : Optional[Any] = Field(default="HealthcareConsideration",alias='@id')
    context_ : Optional[Any] = Field(default=None,alias='@context')
    graph_ : Optional[Any] = Field(default=None,alias='@graph')

    class Config:
        ...


def create_schema_org_model(type_: Union[HealthcareConsiderationProperties, HealthcareConsiderationInheritedProperties, AllProperties] = AllProperties) -> Type[SchemaOrgBase]:
    model = create_model_from_typeddict(type_, __base__=SchemaOrgBase)
    model.__name__ = "HealthcareConsideration"
    return model
    

HealthcareConsideration = create_schema_org_model()


def create_healthcareconsideration_model(model: AllProperties):
    _type =  AllProperties.__annotations__.copy()
    for k in model.keys():
        if k not in _type.__annotations__:
            del _type.__annotations__[k]
    return create_schema_org_model(type_=_type)


def schema_json(model: AllProperties):
    pydantic_type =  create_healthcareconsideration_model(model=model)
    return pydantic_type(model).schema_json()


